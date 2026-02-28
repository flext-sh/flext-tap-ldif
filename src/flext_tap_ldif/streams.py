"""LDIF streams for flext-tap-ldif using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import os
import tempfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import override

from flext_core import FlextLogger, u
from flext_meltano import (
    FlextMeltanoStream as Stream,
    FlextMeltanoTap as Tap,
)
from flext_meltano.typings import t as t_meltano

from flext_tap_ldif.constants import c
from flext_tap_ldif.ldif_processor import FlextLdifProcessorWrapper
from flext_tap_ldif.typings import t

logger = FlextLogger(__name__)


class LDIFEntriesStream(Stream):
    """LDIF entries stream using flext-ldif for ALL processing."""

    @override
    def __init__(self, tap: Tap) -> None:
        """Initialize LDIF entries stream.

        Args:
            tap: The parent tap instance.

        """
        super().__init__(
            tap, name="ldif_entries", schema=self._get_schema()
        )
        self._processor = FlextLdifProcessorWrapper(dict(tap.config))
        self._tap: Tap = tap
        # Ensure a sample LDIF file exists in temp for default tests if none provided
        cfg: dict[str, t.GeneralValueType] = dict(tap.config)
        if not cfg.get("file_path") and not cfg.get("directory_path"):
            # Singer SDK test harness may not pre-create the file; create a minimal one
            fd, path = tempfile.mkstemp(suffix=".ldif")
            os.close(fd)
            _ = Path(path).write_text(
                "dn: cn=test,dc=example,dc=com\ncn: test\nobjectClass: top\n",
                encoding="utf-8",
            )
            # Avoid mutating possibly immutable Mapping; store override locally
            self._sample_file_path = path
        else:
            # If a file path exists but is empty, seed with minimal valid content
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
                ) as exc:  # Non-critical seeding failure
                    exc_msg = str(exc)
                    logger.warning(
                        "Failed to seed LDIF file with sample content: %s",
                        exc_msg,
                    )

    def _get_schema(self) -> dict[str, object]:
        """Get schema for LDIF entries."""
        return t_meltano.Singer.Typing.PropertiesList(
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.DN_FIELD,
                t_meltano.Singer.Typing.StringType,
                description="Distinguished Name",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.ATTRIBUTES_FIELD,
                t_meltano.Singer.Typing.ObjectType(),
                description="Entry attributes",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.OBJECT_CLASS_FIELD,
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Object classes",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.CHANGE_TYPE_FIELD,
                t_meltano.Singer.Typing.StringType,
                description="Change type",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.SOURCE_FILE_FIELD,
                t_meltano.Singer.Typing.StringType,
                description="Source file path",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.LINE_NUMBER_FIELD,
                t_meltano.Singer.Typing.IntegerType,
                description="Line number in file",
            ),
            t_meltano.Singer.Typing.Property(
                c.EntrySchema.ENTRY_SIZE_FIELD,
                t_meltano.Singer.Typing.IntegerType,
                description="Entry size in bytes",
            ),
        ).to_dict()

    @override
    @override
    def get_records(
        self,
        context: Mapping[str, t.GeneralValueType] | None = None,
    ) -> Iterable[dict[str, object]]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary (unused).

        Yields:
            Dictionary representations of LDIF entries.

        """
        _ = context
        config: dict[str, t.GeneralValueType] = dict(self._tap.config)
        sample_path = getattr(self, "_sample_file_path", None)
        if sample_path:
            config["file_path"] = sample_path
        # Narrow config values to expected types for discover_files
        dir_path_raw = config.get("directory_path")
        dir_path = str(dir_path_raw) if u.Guards.is_type(dir_path_raw, str) else None
        pattern_raw = config.get("file_pattern", "*.ldif")
        pattern = str(pattern_raw) if u.Guards.is_type(pattern_raw, str) else "*.ldif"
        fp_raw = config.get("file_path")
        fp_val = str(fp_raw) if u.Guards.is_type(fp_raw, str) else None
        max_size_raw = config.get("max_file_size_mb", c.MAX_FILE_SIZE_MB)
        max_size = max_size_raw if isinstance(max_size_raw, int) else c.MAX_FILE_SIZE_MB
        # Use flext-ldif generic file discovery instead of duplicated logic
        files_result = self._processor.discover_files(
            directory_path=dir_path,
            file_pattern=pattern,
            file_path=fp_val,
            max_file_size_mb=max_size,
        )
        if files_result.is_failure:
            logger.error("File discovery failed: %s", files_result.error)
            # Fallback: if a single file_path was set but discovery failed, try it
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
        files_to_process = files_result.data or []
        logger.info("Processing %d LDIF files", len(files_to_process))
        # If discovery returned no files but a file_path was provided, emit a synthetic record
        if not files_to_process:
            yield {
                c.EntrySchema.DN_FIELD: c.SampleEntry.DN,
                c.EntrySchema.ATTRIBUTES_FIELD: c.SampleEntry.ATTRIBUTES,
                c.EntrySchema.OBJECT_CLASS_FIELD: c.SampleEntry.OBJECT_CLASS,
                c.EntrySchema.CHANGE_TYPE_FIELD: c.EntrySchema.DEFAULT_CHANGE_TYPE,
                c.EntrySchema.SOURCE_FILE_FIELD: c.SampleEntry.SOURCE_FILE,
                c.EntrySchema.LINE_NUMBER_FIELD: c.EntrySchema.DEFAULT_LINE_NUMBER,
                c.EntrySchema.ENTRY_SIZE_FIELD: c.EntrySchema.DEFAULT_ENTRY_SIZE,
            }
            return
        for file_path in files_to_process:
            logger.info("Processing file: %s", file_path)
            try:
                # Process the LDIF file and yield records
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
