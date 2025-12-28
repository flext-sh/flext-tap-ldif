"""FLEXT Tap LDIF Protocols - Domain-specific LDIF tap protocol definitions.

This module provides LDIF tap-specific protocol definitions extending p.
Follows FLEXT standards:
- Domain-specific protocols extending parent protocols
- Protocol composition with multiple inheritance
- Runtime-checkable protocols where applicable

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextTypes as t
from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoProtocols


class FlextMeltanoTapLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
    """LDIF tap-specific protocol definitions extending p.

    Domain-specific protocol system for LDIF data extraction operations.
    Contains ONLY complex LDIF tap-specific protocols extending parent protocols.
    """

    class TapLdif:
        """Tap LDIF namespace for protocol definitions.

        Contains all LDIF tap-specific protocol definitions
        organized by functional domains.
        """

        @runtime_checkable
        class LdifConnectionProtocol(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF file connection management."""

            def open_ldif_file(
                self, file_path: str
            ) -> FlextMeltanoProtocols.Result[object]:
                """Open LDIF file for reading."""
                ...

            def close_ldif_file(self) -> FlextMeltanoProtocols.Result[bool]:
                """Close LDIF file."""
                ...

            def validate_ldif_format(
                self, content: str
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Validate LDIF file format."""
                ...

        @runtime_checkable
        class LdifParsingProtocol(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF parsing operations."""

            def parse_ldif_entry(
                self, entry_text: str
            ) -> FlextMeltanoProtocols.Result[dict[str, t.GeneralValueType]]:
                """Parse single LDIF entry."""
                ...

            def parse_ldif_file(
                self, file_path: str
            ) -> FlextMeltanoProtocols.Result[list[dict[str, t.GeneralValueType]]]:
                """Parse entire LDIF file."""
                ...

            def extract_entry_dn(
                self, entry_lines: list[str]
            ) -> FlextMeltanoProtocols.Result[str]:
                """Extract DN from LDIF entry lines."""
                ...

        @runtime_checkable
        class LdifExtractionProtocol(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF data extraction."""

            def extract_entries_by_filter(
                self,
                entries: list[dict[str, t.GeneralValueType]],
                filter_criteria: dict[str, t.GeneralValueType],
            ) -> FlextMeltanoProtocols.Result[list[dict[str, t.GeneralValueType]]]:
                """Extract LDIF entries matching filter criteria."""
                ...

            def extract_entry_attributes(
                self,
                entry: dict[str, t.GeneralValueType],
                attributes: list[str] | None = None,
            ) -> FlextMeltanoProtocols.Result[dict[str, t.GeneralValueType]]:
                """Extract specific attributes from LDIF entry."""
                ...

        @runtime_checkable
        class LdifTransformationProtocol(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF data transformation."""

            def transform_ldif_to_singer(
                self, ldif_entry: dict[str, t.GeneralValueType]
            ) -> FlextMeltanoProtocols.Result[dict[str, t.GeneralValueType]]:
                """Transform LDIF entry to Singer record format."""
                ...

            def normalize_ldif_attributes(
                self, attributes: dict[str, list[t.GeneralValueType]]
            ) -> FlextMeltanoProtocols.Result[dict[str, t.GeneralValueType]]:
                """Normalize LDIF attribute values."""
                ...

        @runtime_checkable
        class StreamGenerationProtocol(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def generate_streams_from_ldif(
                self,
                ldif_entries: list[dict[str, t.GeneralValueType]],
                config: dict[str, t.GeneralValueType],
            ) -> FlextMeltanoProtocols.Result[list[dict[str, t.GeneralValueType]]]:
                """Generate Singer streams from LDIF entries."""
                ...

            def sync_ldif_stream(
                self,
                stream_name: str,
                ldif_entries: list[dict[str, t.GeneralValueType]],
                state: dict[str, t.GeneralValueType],
            ) -> FlextMeltanoProtocols.Result[dict[str, t.GeneralValueType]]:
                """Sync Singer stream from LDIF entries."""
                ...


# Runtime alias for simplified usage
p = FlextMeltanoTapLdifProtocols

__all__ = [
    "FlextMeltanoTapLdifProtocols",
    "p",
]
