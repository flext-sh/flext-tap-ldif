"""LDIF file processing module for FLEXT Tap LDIF using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project.
"""

from __future__ import annotations

from collections.abc import Generator, Mapping
from pathlib import Path
from typing import NoReturn, override

from flext_core import FlextLogger, FlextResult
from flext_ldif import FlextLdif
from flext_ldif.models import m

logger = FlextLogger(__name__)
# Use flext-ldif processor instead of reimplementing LDIF functionality
LDIFProcessor = FlextLdif
# Backward compatibility alias removed (causes self-assignment warning)


class FlextLdifProcessorWrapper:
    """Wrapper for FlextLdifProcessor to maintain API compatibility."""

    @override
    def __init__(self, config: Mapping[str, str | int | bool]) -> None:
        """Initialize the LDIF processor using flext-ldif infrastructure.

        Args:
        config: Configuration dictionary from the tap.

        """
        super().__init__()
        self.config = config
        self._api = FlextLdif()

    def _raise_parse_error(self, msg: str) -> NoReturn:
        """Raise parse error with message."""
        raise ValueError(msg)

    def discover_files(
        self,
        directory_path: str | Path | None = None,
        file_pattern: str = "*.ldif",
        file_path: str | Path | None = None,
        max_file_size_mb: int = 100,
    ) -> FlextResult[list[Path]]:
        """Discover LDIF files using local file discovery.

        Args:
            directory_path: Directory to search for LDIF files
            file_pattern: Glob pattern for file matching
            file_path: Single file path (alternative to directory_path)
            max_file_size_mb: Maximum file size in MB

        Returns:
            FlextResult[list[Path]]: Success with discovered files or failure with error

        """
        max_size_bytes = max_file_size_mb * 1024 * 1024
        discovered: list[Path] = []

        # Single file mode
        if file_path is not None:
            match file_path:
                case str() as file_path_text:
                    p = Path(file_path_text)
                case _:
                    p = file_path
            if not p.exists():
                return FlextResult[list[Path]].fail(f"File not found: {p}")
            if p.stat().st_size > max_size_bytes:
                return FlextResult[list[Path]].fail(f"File exceeds max size: {p}")
            discovered.append(p)
            return FlextResult[list[Path]].ok(discovered)

        # Directory mode
        if directory_path is not None:
            match directory_path:
                case str() as directory_path_text:
                    d = Path(directory_path_text)
                case _:
                    d = directory_path
            if not d.exists() or not d.is_dir():
                return FlextResult[list[Path]].fail(f"Directory not found: {d}")
            discovered.extend(
                f
                for f in sorted(d.glob(file_pattern))
                if f.is_file() and f.stat().st_size <= max_size_bytes
            )
            return FlextResult[list[Path]].ok(discovered)

        return FlextResult[list[Path]].fail("No file_path or directory_path specified")

    def process_file(
        self,
        file_path: Path,
    ) -> Generator[Mapping[str, str | int | Mapping[str, list[str]] | list[str]]]:
        """Process a single LDIF file and yield records using flext-ldif.

        Args:
            file_path: Path to the LDIF file.

        Yields:
            Dictionary records representing LDIF entries.

        """
        logger.info("Processing LDIF file: %s", file_path)
        try:
            # Ensure encoding is properly typed
            encoding = self.config.get("encoding", "utf-8")
            match encoding:
                case str() as text_encoding:
                    file_encoding = text_encoding
                case _:
                    file_encoding = "utf-8"
            with file_path.open("r", encoding=file_encoding) as file:
                content = file.read()
                parse_result = self._api.parse(content)
                if parse_result.is_failure:
                    msg: str = f"Failed to parse LDIF: {parse_result.error}"
                    self._raise_parse_error(msg)
                for raw_entry in parse_result.value:
                    entry = m.Ldif.Entry.model_validate(raw_entry)
                    # Convert entry to expected dictionary format
                    dn_val = entry.dn.value if entry.dn is not None else ""
                    attrs_dict = (
                        dict(entry.attributes.attributes)
                        if entry.attributes is not None
                        else {}
                    )
                    yield {
                        "dn": str(dn_val),
                        "attributes": attrs_dict,
                        "object_class": attrs_dict.get("objectClass", []),
                        "change_type": "None",
                        "source_file": str(file_path),
                        "line_number": 0,
                        "entry_size": len(str(entry).encode("utf-8")),
                    }
        except (RuntimeError, ValueError, TypeError):
            logger.exception("Failed to process LDIF file: %s", file_path)
            if self.config.get("strict_parsing", True):
                raise


# Create the original class name for backward compatibility
FlextLdifProcessor: type[FlextLdifProcessorWrapper] = FlextLdifProcessorWrapper
__all__: list[str] = [
    "FlextLdifProcessor",
    "LDIFProcessor",
]
