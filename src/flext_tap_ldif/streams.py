"""LDIF streams for flext-tap-ldif using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Iterable, MutableMapping
from typing import override

from flext_core import FlextLogger
from flext_meltano.singer.sdk import (
    FlextMeltanoSingerContext,
    FlextMeltanoSingerRecord,
    FlextMeltanoSingerStreamBase,
    FlextMeltanoSingerTapBase,
)

from flext_tap_ldif import FlextLdifProcessor, c, t

logger = FlextLogger(__name__)


class FlextTapLdifEntriesStream(FlextMeltanoSingerStreamBase):
    """LDIF entries stream using flext-ldif for ALL processing."""

    @override
    def __init__(self, tap: FlextMeltanoSingerTapBase) -> None:
        """Initialize LDIF entries stream.

        Args:
            tap: The parent tap instance.

        """
        super().__init__(tap, name="ldif_entries", schema=self._get_schema())
        self._processor = FlextLdifProcessor(dict(tap.config))
        self._tap: FlextMeltanoSingerTapBase = tap

    @override
    def get_records(
        self,
        context: FlextMeltanoSingerContext | None = None,
    ) -> Iterable[FlextMeltanoSingerRecord]:
        """Return a generator of record-type dictionary objects.

        Args:
            context: Stream partition or context dictionary (unused).

        Yields:
            Dictionary representations of LDIF entries.

        """
        _ = context
        config: MutableMapping[str, t.ContainerValue] = dict(self._tap.config)
        dir_path_raw = config.get("directory_path")
        dir_path = dir_path_raw if isinstance(dir_path_raw, str) else None
        pattern_raw = config.get("file_pattern", "*.ldif")
        pattern = pattern_raw if isinstance(pattern_raw, str) else "*.ldif"
        fp_raw = config.get("file_path")
        fp_val = fp_raw if isinstance(fp_raw, str) else None
        max_size_raw = config.get("max_file_size_mb", c.TapLdif.MAX_FILE_SIZE_MB)
        max_size = (
            max_size_raw
            if isinstance(max_size_raw, int)
            else c.TapLdif.MAX_FILE_SIZE_MB
        )
        files_result = self._processor.discover_files(
            directory_path=dir_path,
            file_pattern=pattern,
            file_path=fp_val,
            max_file_size_mb=max_size,
        )
        if files_result.is_failure:
            error_msg = files_result.error or "LDIF file discovery failed"
            if bool(config.get("strict_parsing", True)):
                raise RuntimeError(error_msg)
            logger.error("File discovery failed: %s", error_msg)
            return
        files_to_process = files_result.value or []
        logger.info("Processing %d LDIF files", len(files_to_process))
        if not files_to_process:
            error_msg = "No LDIF files discovered"
            if bool(config.get("strict_parsing", True)):
                raise RuntimeError(error_msg)
            logger.warning(error_msg)
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
