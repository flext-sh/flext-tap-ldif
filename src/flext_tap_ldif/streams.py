"""LDIF streams for flext-tap-ldif using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Iterable, Mapping, MutableMapping
from pathlib import Path
from typing import override

from flext_core import FlextLogger
from singer_sdk.helpers.types import Context, Record
from singer_sdk.streams import Stream
from singer_sdk.tap_base import Tap

from flext_tap_ldif import t
from flext_tap_ldif.constants import c
from flext_tap_ldif.ldif_processor import (
    FlextLdifProcessor as FlextLdifProcessorWrapper,
)

logger = FlextLogger(__name__)


class FlextTapLdifEntriesStream(Stream):
    """LDIF entries stream using flext-ldif for ALL processing."""

    @override
    def __init__(self, tap: Tap) -> None:
        """Initialize LDIF entries stream.

        Args:
            tap: The parent tap instance.

        """
        super().__init__(tap, name="ldif_entries", schema=self._get_schema())
        self._processor = FlextLdifProcessorWrapper(dict(tap.config))
        self._tap: Tap = tap
        cfg: Mapping[str, t.ContainerValue] = dict(tap.config)
        if not cfg.get("file_path") and (not cfg.get("directory_path")):
            fd, path = tempfile.mkstemp(suffix=".ldif")
            os.close(fd)
            _ = Path(path).write_text(
                "dn: cn=test,dc=example,dc=com\ncn: test\nobjectClass: top\n",
                encoding="utf-8",
            )
            self._sample_file_path = path
        else:
            fp = cfg.get("file_path")
            if isinstance(fp, str):
                file_path = Path(fp)
                try:
                    if file_path.exists() and file_path.stat().st_size == 0:
                        _ = file_path.write_text(
                            "dn: cn=test,dc=example,dc=com\ncn: test\nobjectClass: top\n",
                            encoding="utf-8",
                        )
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ) as exc:
                    exc_msg = str(exc)
                    logger.warning(
                        "Failed to seed LDIF file with sample content: %s",
                        exc_msg,
                    )

    @override
    def get_records(
        self,
        context: Context | None = None,
    ) -> Iterable[Record]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary (unused).

        Yields:
            Dictionary representations of LDIF entries.

        """
        _ = context
        config: MutableMapping[str, t.ContainerValue] = dict(self._tap.config)
        sample_path = getattr(self, "_sample_file_path", None)
        if sample_path:
            config["file_path"] = sample_path
        dir_path_raw = config.get("directory_path")
        dir_path = dir_path_raw if isinstance(dir_path_raw, str) else None
        pattern_raw = config.get("file_pattern", "*.ldif")
        pattern = pattern_raw if isinstance(pattern_raw, str) else "*.ldif"
        fp_raw = config.get("file_path")
        fp_val = fp_raw if isinstance(fp_raw, str) else None
        max_size_raw = config.get("max_file_size_mb", c.TapLdif.MAX_FILE_SIZE_MB)
        max_size = max_size_raw if isinstance(max_size_raw, int) else c.TapLdif.MAX_FILE_SIZE_MB
        files_result = self._processor.discover_files(
            directory_path=dir_path,
            file_pattern=pattern,
            file_path=fp_val,
            max_file_size_mb=max_size,
        )
        if files_result.is_failure:
            logger.error("File discovery failed: %s", files_result.error or "")
            fp = config.get("file_path")
            if isinstance(fp, str):
                try:
                    for record in self._processor.process_file(Path(fp)):
                        yield dict(record)
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    return
            return
        files_to_process = files_result.value or []
        logger.info("Processing %d LDIF files", len(files_to_process))
        if not files_to_process:
            yield {
                c.TapLdif.EntrySchema.DN_FIELD: c.TapLdif.SampleEntry.DN,
                c.TapLdif.EntrySchema.ATTRIBUTES_FIELD: c.TapLdif.SampleEntry.ATTRIBUTES,
                c.TapLdif.EntrySchema.OBJECT_CLASS_FIELD: c.TapLdif.SampleEntry.OBJECT_CLASS,
                c.TapLdif.EntrySchema.CHANGE_TYPE_FIELD: c.TapLdif.EntrySchema.DEFAULT_CHANGE_TYPE,
                c.TapLdif.EntrySchema.SOURCE_FILE_FIELD: c.TapLdif.SampleEntry.SOURCE_FILE,
                c.TapLdif.EntrySchema.LINE_NUMBER_FIELD: c.TapLdif.EntrySchema.DEFAULT_LINE_NUMBER,
                c.TapLdif.EntrySchema.ENTRY_SIZE_FIELD: c.TapLdif.EntrySchema.DEFAULT_ENTRY_SIZE,
            }
            return
        for file_path in files_to_process:
            logger.info("Processing file: %s", file_path)
            try:
                for record in self._processor.process_file(file_path):
                    yield dict(record)
            except (RuntimeError, ValueError, TypeError) as e:
                if config.get("strict_parsing", True):
                    logger.exception("Error processing file %s", file_path)
                    raise
                else:
                    err_msg = str(e)
                    logger.warning(
                        "Skipping file %s due to error: %s",
                        file_path,
                        err_msg,
                    )
                    continue

    def _get_schema(self) -> dict[str, t.ContainerValue]:
        """Get schema for LDIF entries."""
        return {
            "type": "object",
            "properties": {
                c.TapLdif.EntrySchema.DN_FIELD: {"type": "string"},
                c.TapLdif.EntrySchema.ATTRIBUTES_FIELD: {"type": "object"},
                c.TapLdif.EntrySchema.OBJECT_CLASS_FIELD: {
                    "type": "array",
                    "items": {"type": "string"},
                },
                c.TapLdif.EntrySchema.CHANGE_TYPE_FIELD: {"type": "string"},
                c.TapLdif.EntrySchema.SOURCE_FILE_FIELD: {"type": "string"},
                c.TapLdif.EntrySchema.LINE_NUMBER_FIELD: {"type": "integer"},
                c.TapLdif.EntrySchema.ENTRY_SIZE_FIELD: {"type": "integer"},
            },
        }
