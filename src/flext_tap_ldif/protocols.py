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

from collections.abc import Mapping, Sequence
from typing import Protocol, runtime_checkable

from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoModels, FlextMeltanoProtocols

from flext_tap_ldif import t


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
        class LdifConnection(FlextLdifProtocols.Service[t.Container], Protocol):
            """Protocol for LDIF file connection management."""

            def close_ldif_file(self) -> FlextMeltanoProtocols.Result[bool]:
                """Close LDIF file."""
                ...

            def open_ldif_file(
                self,
                file_path: str,
            ) -> FlextMeltanoProtocols.Result[t.Container]:
                """Open LDIF file for reading."""
                ...

            def validate_ldif_format(
                self,
                content: str,
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Validate LDIF file format."""
                ...

        @runtime_checkable
        class LdifParsing(FlextLdifProtocols.Service[t.Container], Protocol):
            """Protocol for LDIF parsing operations."""

            def extract_entry_dn(
                self,
                entry_lines: t.StrSequence,
            ) -> FlextMeltanoProtocols.Result[str]:
                """Extract DN from LDIF entry lines."""
                ...

            def parse_ldif_entry(
                self,
                entry_text: str,
            ) -> FlextMeltanoProtocols.Result[t.Container]:
                """Parse single LDIF entry."""
                ...

            def parse_ldif_file(
                self,
                file_path: str,
            ) -> FlextMeltanoProtocols.Result[t.ContainerValueList]:
                """Parse entire LDIF file."""
                ...

        @runtime_checkable
        class LdifExtraction(FlextLdifProtocols.Service[t.Container], Protocol):
            """Protocol for LDIF data extraction."""

            def extract_entries_by_filter(
                self,
                entries: Sequence[Mapping[str, t.ContainerValue]],
                filter_criteria: Mapping[str, t.ContainerValue],
            ) -> FlextMeltanoProtocols.Result[t.ContainerValueList]:
                """Extract LDIF entries matching filter criteria."""
                ...

            def extract_entry_attributes(
                self,
                entry: Mapping[str, t.ContainerValue],
                attributes: t.StrSequence | None = None,
            ) -> FlextMeltanoProtocols.Result[t.Container]:
                """Extract specific attributes from LDIF entry."""
                ...

        @runtime_checkable
        class LdifTransformation(FlextLdifProtocols.Service[t.Container], Protocol):
            """Protocol for LDIF data transformation."""

            def normalize_ldif_attributes(
                self,
                attributes: Mapping[str, Sequence[t.ContainerValue]],
            ) -> FlextMeltanoProtocols.Result[t.Container]:
                """Normalize LDIF attribute values."""
                ...

            def transform_ldif_to_singer(
                self,
                ldif_entry: Mapping[str, t.ContainerValue],
            ) -> FlextMeltanoProtocols.Result[
                FlextMeltanoModels.Meltano.SingerRecordMessage
            ]:
                """Transform LDIF entry to Singer record format."""
                ...

        @runtime_checkable
        class StreamGeneration(FlextLdifProtocols.Service[t.Container], Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def generate_streams_from_ldif(
                self,
                ldif_entries: Sequence[Mapping[str, t.ContainerValue]],
                config: Mapping[str, t.ContainerValue],
            ) -> FlextMeltanoProtocols.Result[FlextMeltanoModels.Meltano.SingerCatalog]:
                """Generate Singer streams from LDIF entries."""
                ...

            def sync_ldif_stream(
                self,
                stream_name: str,
                ldif_entries: Sequence[Mapping[str, t.ContainerValue]],
                state: Mapping[str, t.ContainerValue],
            ) -> FlextMeltanoProtocols.Result[
                FlextMeltanoModels.Meltano.SingerStateMessage
            ]:
                """Sync Singer stream from LDIF entries."""
                ...


p = FlextTapLdifProtocols
__all__ = ["FlextTapLdifProtocols", "p"]
