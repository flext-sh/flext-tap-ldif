"""Singer entries stream utilities for the LDIF tap."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from flext_meltano import u
from flext_tap_ldif import c, m, t
from flext_tap_ldif._utilities.processor import FlextTapLdifUtilitiesProcessor

if TYPE_CHECKING:
    from collections.abc import Iterable


class FlextTapLdifUtilitiesEntriesStream:
    """MRO mixin exposing EntriesStream under u.TapLdif."""

    logger = u.fetch_logger(__name__)

    class EntriesStream(m.Meltano.SingerStreamBase):
        """LDIF entries stream using flext-ldif for ALL processing."""

        @override
        def __init__(self, tap: m.Meltano.SingerTapBase) -> None:
            """Initialize LDIF entries stream."""
            super().__init__(tap, name="ldif_entries", schema=self._get_schema())
            self._processor = FlextTapLdifUtilitiesProcessor.Processor(
                t.scalar_mapping_adapter().validate_python(tap.config),
            )
            self._tap: m.Meltano.SingerTapBase = tap

        @override
        def get_records(
            self,
            context: t.JsonMapping | None = None,
        ) -> Iterable[m.Meltano.SingerRecord]:
            """Return a generator of record-type dictionary objects."""
            _ = context
            settings = t.json_dict_adapter().validate_python(self._tap.config)
            dir_path_raw = settings.get("directory_path")
            dir_path = dir_path_raw if isinstance(dir_path_raw, str) else None
            pattern_raw = settings.get("file_pattern", "*.ldif")
            pattern = pattern_raw if isinstance(pattern_raw, str) else "*.ldif"
            fp_raw = settings.get("file_path")
            fp_val = fp_raw if isinstance(fp_raw, str) else None
            max_size_raw = settings.get("max_file_size_mb", c.TapLdif.MAX_FILE_SIZE_MB)
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
            if files_result.failure:
                error_msg = files_result.error or "LDIF file discovery failed"
                if bool(settings.get("strict_parsing", True)):
                    raise RuntimeError(error_msg)
                FlextTapLdifUtilitiesEntriesStream.logger.error(
                    "File discovery failed: %s",
                    error_msg,
                )
                return
            files_to_process = files_result.value or []
            FlextTapLdifUtilitiesEntriesStream.logger.info(
                "Processing %d LDIF files",
                len(files_to_process),
            )
            if not files_to_process:
                error_msg = "No LDIF files discovered"
                if bool(settings.get("strict_parsing", True)):
                    raise RuntimeError(error_msg)
                FlextTapLdifUtilitiesEntriesStream.logger.warning(error_msg)
                return
            for file_path in files_to_process:
                FlextTapLdifUtilitiesEntriesStream.logger.info(
                    "Processing file: %s",
                    str(file_path),
                )
                try:
                    for record in self._processor.process_file(file_path):
                        yield m.Meltano.SingerRecord(record)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    if settings.get("strict_parsing", True):
                        FlextTapLdifUtilitiesEntriesStream.logger.exception(
                            "Error processing file %s",
                            str(file_path),
                        )
                        raise
                    err_msg = str(e)
                    FlextTapLdifUtilitiesEntriesStream.logger.warning(
                        "Skipping file %s due to error: %s",
                        str(file_path),
                        err_msg,
                    )
                    continue

        def _get_schema(self) -> t.JsonDict:
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
