"""LDIF file processor utilities for the tap namespace."""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path
from typing import NoReturn

from flext_ldif import ldif
from flext_meltano import u
from flext_tap_ldif import c, m, p, r, t


class FlextTapLdifUtilitiesProcessor:
    """MRO mixin exposing Processor under u.TapLdif."""

    logger = u.fetch_logger(__name__)

    class Processor:
        """LDIF file processor using flext-ldif infrastructure."""

        def __init__(self, settings: t.ConfigurationMapping) -> None:
            """Initialize the LDIF processor."""
            self.settings = settings
            self._api = ldif()

        def discover_files(
            self,
            directory_path: str | Path | None = None,
            file_pattern: str = "*.ldif",
            file_path: str | Path | None = None,
            max_file_size_mb: int = 100,
        ) -> p.Result[t.SequenceOf[Path]]:
            """Discover LDIF files using local file discovery."""
            max_size_bytes = max_file_size_mb * 1024 * 1024
            discovered: t.MutableSequenceOf[Path] = []
            if file_path is not None:
                match file_path:
                    case str() as file_path_text:
                        p = Path(file_path_text)
                    case _:
                        p = file_path
                if not p.exists():
                    return r[t.SequenceOf[Path]].fail(f"File not found: {p}")
                if p.stat().st_size > max_size_bytes:
                    return r[t.SequenceOf[Path]].fail(f"File exceeds max size: {p}")
                discovered.append(p)
                return r[t.SequenceOf[Path]].ok(discovered)
            if directory_path is not None:
                match directory_path:
                    case str() as directory_path_text:
                        d = Path(directory_path_text)
                    case _:
                        d = directory_path
                if not d.exists() or not d.is_dir():
                    return r[t.SequenceOf[Path]].fail(f"Directory not found: {d}")
                discovered.extend(
                    f
                    for f in sorted(d.glob(file_pattern))
                    if f.is_file() and f.stat().st_size <= max_size_bytes
                )
                return r[t.SequenceOf[Path]].ok(discovered)
            return r[t.SequenceOf[Path]].fail(
                "No file_path or directory_path specified"
            )

        def process_file(
            self,
            file_path: Path,
        ) -> Generator[t.JsonMapping]:
            """Process a single LDIF file and yield records using flext-ldif."""
            FlextTapLdifUtilitiesProcessor.logger.info(
                "Processing LDIF file: %s",
                str(file_path),
            )
            try:
                yield from self._yield_records(file_path)
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                FlextTapLdifUtilitiesProcessor.logger.exception(
                    "Failed to process LDIF file: %s",
                    str(file_path),
                )
                if self.settings.get("strict_parsing", True):
                    raise

        def _yield_records(
            self,
            file_path: Path,
        ) -> Generator[t.JsonMapping]:
            """Yield parsed Singer records from a file."""
            encoding = self.settings.get("encoding", c.DEFAULT_ENCODING)
            match encoding:
                case str() as text_encoding:
                    file_encoding = text_encoding
                case _:
                    file_encoding = c.DEFAULT_ENCODING
            with file_path.open("r", encoding=file_encoding) as file:
                content = file.read()
            parse_result = self._api.parse_ldif(content)
            if parse_result.failure:
                msg: str = f"Failed to parse LDIF: {parse_result.error}"
                self._raise_parse_error(msg)
            for raw_entry in parse_result.value.entries:
                entry = m.Ldif.Entry.model_validate(raw_entry)
                dn_val = entry.dn.value if entry.dn is not None else ""
                attrs_dict: t.JsonMapping = t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                    {k: list(v) for k, v in entry.attributes.attributes.items()}
                    if entry.attributes is not None
                    else {},
                )
                yield t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                    {
                        c.TapLdif.EntrySchema.DN_FIELD: dn_val,
                        c.TapLdif.EntrySchema.ATTRIBUTES_FIELD: attrs_dict,
                        c.TapLdif.EntrySchema.OBJECT_CLASS_FIELD: attrs_dict.get(
                            "objectClass",
                            [],
                        ),
                        c.TapLdif.EntrySchema.CHANGE_TYPE_FIELD: c.TapLdif.EntrySchema.DEFAULT_CHANGE_TYPE,
                        c.TapLdif.EntrySchema.SOURCE_FILE_FIELD: str(file_path),
                        c.TapLdif.EntrySchema.LINE_NUMBER_FIELD: c.TapLdif.EntrySchema.DEFAULT_LINE_NUMBER,
                        c.TapLdif.EntrySchema.ENTRY_SIZE_FIELD: len(
                            str(entry).encode(c.DEFAULT_ENCODING)
                        ),
                    },
                )

        def _raise_parse_error(self, msg: str) -> NoReturn:
            """Raise parse error with message."""
            raise ValueError(msg)
