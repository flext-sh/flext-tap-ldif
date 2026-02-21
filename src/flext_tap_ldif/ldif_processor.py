"""LDIF file processing module for FLEXT Tap LDIF using flext-ldif infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project.
"""

from __future__ import annotations

from collections.abc import Generator
from pathlib import Path
from typing import NoReturn, override

from flext_core import FlextLogger, FlextResult, FlextTypes as t
from flext_ldif import FlextLdif

logger = FlextLogger(__name__)
# Use flext-ldif processor instead of reimplementing LDIF functionality
LDIFProcessor = FlextLdif
# Backward compatibility alias removed (causes self-assignment warning)


class FlextLdifProcessorWrapper:
    """Wrapper for FlextLdifProcessor to maintain API compatibility."""

    @override
    def __init__(self, config: dict[str, t.GeneralValueType]) -> None:
        """Initialize the LDIF processor using flext-ldif infrastructure.

        Args:
        config: Configuration dictionary from the tap.

        Returns:
        object: Description of return value.

        """
        self.config: dict[str, t.GeneralValueType] = config
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
            p = Path(file_path) if isinstance(file_path, str) else file_path
            if not p.exists():
                return FlextResult[list[Path]].fail(f"File not found: {p}")
            if p.stat().st_size > max_size_bytes:
                return FlextResult[list[Path]].fail(f"File exceeds max size: {p}")
            discovered.append(p)
            return FlextResult[list[Path]].ok(discovered)

        # Directory mode
        if directory_path is not None:
            d = (
                Path(directory_path)
                if isinstance(directory_path, str)
                else directory_path
            )
            if not d.exists() or not d.is_dir():
                return FlextResult[list[Path]].fail(f"Directory not found: {d}")
            discovered.extend(
                f
                for f in sorted(d.glob(file_pattern))
                if f.is_file() and f.stat().st_size <= max_size_bytes
            )
            return FlextResult[list[Path]].ok(discovered)

        return FlextResult[list[Path]].fail("No file_path or directory_path specified")

    def process_file(self, file_path: Path) -> Generator[dict[str, t.GeneralValueType]]:
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
            if not isinstance(encoding, str):
                encoding = "utf-8"
            with file_path.open("r", encoding=encoding) as file:
                content = file.read()
                parse_result: FlextResult[list[t.GeneralValueType]] = self._api.parse(
                    content
                )
                if parse_result.is_failure:
                    msg: str = f"Failed to parse LDIF: {parse_result.error}"
                    self._raise_parse_error(msg)
                    return
                entries = parse_result.value
                if entries is None:
                    return
                for entry in entries:
                    # Convert entry to expected dictionary format
                    dn_val = getattr(entry, "dn", "")
                    attrs_obj = getattr(entry, "attributes", None)
                    attrs_dict: dict[str, list[str]] = (
                        getattr(attrs_obj, "attributes", {}) if attrs_obj else {}
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
