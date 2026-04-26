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

from collections.abc import (
    Mapping,
    Sequence,
)
from typing import Protocol, runtime_checkable

from flext_ldif import FlextLdifProtocols
from flext_meltano import m, p
from flext_tap_ldif import t


class FlextTapLdifProtocols(p, FlextLdifProtocols):
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
        class LdifConnection(FlextLdifProtocols.Service[t.JsonValue], Protocol):
            """Protocol for LDIF file connection management."""

            def close_ldif_file(self) -> p.Result[bool]:
                """Close LDIF file."""
                ...

            def open_ldif_file(
                self,
                file_path: str,
            ) -> p.Result[t.JsonValue]:
                """Open LDIF file for reading."""
                ...

            def validate_ldif_format(
                self,
                content: str,
            ) -> p.Result[bool]:
                """Validate LDIF file format."""
                ...

        @runtime_checkable
        class LdifParsing(FlextLdifProtocols.Service[t.JsonValue], Protocol):
            """Protocol for LDIF parsing operations."""

            def extract_entry_dn(
                self,
                entry_lines: t.StrSequence,
            ) -> p.Result[str]:
                """Extract DN from LDIF entry lines."""
                ...

            def parse_ldif_entry(
                self,
                entry_text: str,
            ) -> p.Result[t.JsonValue]:
                """Parse single LDIF entry."""
                ...

            def parse_ldif_file(
                self,
                file_path: str,
            ) -> p.Result[t.JsonList]:
                """Parse entire LDIF file."""
                ...

        @runtime_checkable
        class LdifExtraction(FlextLdifProtocols.Service[t.JsonValue], Protocol):
            """Protocol for LDIF data extraction."""

            def extract_entries_by_filter(
                self,
                entries: Sequence[t.JsonMapping],
                filter_criteria: t.JsonMapping,
            ) -> p.Result[t.JsonList]:
                """Extract LDIF entries matching filter criteria."""
                ...

            def extract_entry_attributes(
                self,
                entry: t.JsonMapping,
                attributes: t.StrSequence | None = None,
            ) -> p.Result[t.JsonValue]:
                """Extract specific attributes from LDIF entry."""
                ...

        @runtime_checkable
        class LdifTransformation(FlextLdifProtocols.Service[t.JsonValue], Protocol):
            """Protocol for LDIF data transformation."""

            def normalize_ldif_attributes(
                self,
                attributes: Mapping[str, t.JsonList],
            ) -> p.Result[t.JsonValue]:
                """Normalize LDIF attribute values."""
                ...

            def transform_ldif_to_singer(
                self,
                ldif_entry: t.JsonMapping,
            ) -> p.Result[m.Meltano.SingerRecordMessage]:
                """Transform LDIF entry to Singer record format."""
                ...

        @runtime_checkable
        class StreamGeneration(FlextLdifProtocols.Service[t.JsonValue], Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def generate_streams_from_ldif(
                self,
                ldif_entries: Sequence[t.JsonMapping],
                settings: t.JsonMapping,
            ) -> p.Result[m.Meltano.SingerCatalog]:
                """Generate Singer streams from LDIF entries."""
                ...

            def sync_ldif_stream(
                self,
                stream_name: str,
                ldif_entries: Sequence[t.JsonMapping],
                state: t.JsonMapping,
            ) -> p.Result[m.Meltano.SingerStateMessage]:
                """Sync Singer stream from LDIF entries."""
                ...


p = FlextTapLdifProtocols
__all__: list[str] = ["FlextTapLdifProtocols", "p"]
