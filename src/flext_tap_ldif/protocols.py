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

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoModels as m, FlextMeltanoProtocols


class FlextTapLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
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
        class LdifConnection(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF file connection management."""

            def close_ldif_file(self) -> FlextMeltanoProtocols.Result[bool]:
                """Close LDIF file."""
                ...

            def open_ldif_file(
                self, file_path: str
            ) -> FlextMeltanoProtocols.Result[object]:
                """Open LDIF file for reading."""
                ...

            def validate_ldif_format(
                self, content: str
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Validate LDIF file format."""
                ...

        @runtime_checkable
        class LdifParsing(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF parsing operations."""

            def extract_entry_dn(
                self, entry_lines: list[str]
            ) -> FlextMeltanoProtocols.Result[str]:
                """Extract DN from LDIF entry lines."""
                ...

            def parse_ldif_entry(
                self, entry_text: str
            ) -> FlextMeltanoProtocols.Result[object]:
                """Parse single LDIF entry."""
                ...

            def parse_ldif_file(
                self, file_path: str
            ) -> FlextMeltanoProtocols.Result[list[object]]:
                """Parse entire LDIF file."""
                ...

        @runtime_checkable
        class LdifExtraction(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF data extraction."""

            def extract_entries_by_filter(
                self,
                entries: list[Mapping[str, object]],
                filter_criteria: Mapping[str, object],
            ) -> FlextMeltanoProtocols.Result[list[object]]:
                """Extract LDIF entries matching filter criteria."""
                ...

            def extract_entry_attributes(
                self,
                entry: Mapping[str, object],
                attributes: list[str] | None = None,
            ) -> FlextMeltanoProtocols.Result[object]:
                """Extract specific attributes from LDIF entry."""
                ...

        @runtime_checkable
        class LdifTransformation(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for LDIF data transformation."""

            def normalize_ldif_attributes(
                self, attributes: Mapping[str, list[object]]
            ) -> FlextMeltanoProtocols.Result[object]:
                """Normalize LDIF attribute values."""
                ...

            def transform_ldif_to_singer(
                self, ldif_entry: Mapping[str, object]
            ) -> FlextMeltanoProtocols.Result[m.Meltano.SingerRecordMessage]:
                """Transform LDIF entry to Singer record format."""
                ...

        @runtime_checkable
        class StreamGeneration(FlextLdifProtocols.Service[object], Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def generate_streams_from_ldif(
                self,
                ldif_entries: list[Mapping[str, object]],
                config: Mapping[str, object],
            ) -> FlextMeltanoProtocols.Result[m.Meltano.SingerCatalog]:
                """Generate Singer streams from LDIF entries."""
                ...

            def sync_ldif_stream(
                self,
                stream_name: str,
                ldif_entries: list[Mapping[str, object]],
                state: Mapping[str, object],
            ) -> FlextMeltanoProtocols.Result[m.Meltano.SingerStateMessage]:
                """Sync Singer stream from LDIF entries."""
                ...


p = FlextTapLdifProtocols
__all__ = ["FlextTapLdifProtocols", "p"]
