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

from flext_core import FlextLogger, FlextResult
from flext_ldif import FlextLdif

logger = FlextLogger(__name__)

# Use flext-ldif processor instead of reimplementing LDIF functionality
LDIFProcessor = FlextLdif

# Backward compatibility alias removed (causes self-assignment warning)


class FlextLdifProcessorWrapper:
    """Wrapper for FlextLdifProcessor to maintain API compatibility."""

    @override
    def __init__(self, config: dict[str, object]) -> None:
        """Initialize the LDIF processor using flext-ldif infrastructure.

        Args:
            config: Configuration dictionary from the tap.

        Returns:
            object: Description of return value.

        """
        self.config: dict[str, object] = config
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
        """Discover LDIF files using generic flext-ldif functionality.

        Args:
            directory_path: Directory to search for LDIF files
            file_pattern: Glob pattern for file matching
            file_path: Single file path (alternative to directory_path)
            max_file_size_mb: Maximum file size in MB

        Returns:
            FlextResult[list[Path]]: Success with discovered files or failure with error

        """
        # Delegate to flext-ldif generic file discovery - NO local duplication
        return self._api.discover_ldif_files(
            directory_path=directory_path,
            file_pattern=file_pattern,
            file_path=file_path,
            max_file_size_mb=max_file_size_mb,
        )

    def process_file(self, file_path: Path) -> Generator[dict[str, object]]:
        """Process a single LDIF file and yield records using flext-ldif.

        Args:
            file_path: Path to the LDIF file.

        Yields:
            Dictionary records representing LDIF entries.

        Returns:
            Generator[dict["str", "object"]]: Dictionary records representing LDIF entries.

        """
        logger.info("Processing LDIF file: %s", file_path)
        try:
            # Ensure encoding is properly typed
            encoding = self.config.get("encoding", "utf-8")
            if not isinstance(encoding, str):
                encoding = "utf-8"

            with file_path.open("r", encoding=encoding) as file:
                content = file.read()
                parse_result: FlextResult[object] = self._api.parse(content)
                if parse_result.is_failure:
                    msg: str = f"Failed to parse LDIF: {parse_result.error}"
                    self._raise_parse_error(msg)
                    return
                entries = parse_result.value

                for entry in entries:
                    # Convert FlextLdifEntry to expected dictionary format
                    yield {
                        "dn": str(entry.dn),
                        "attributes": entry.attributes.attributes,
                        "object_class": entry.attributes.attributes.get(
                            "objectClass",
                            [],
                        ),
                        "change_type": "None",  # Change records not supported in simple parse
                        "source_file": str(file_path),
                        "line_number": 0,  # Line numbers not available in simplified parse
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
