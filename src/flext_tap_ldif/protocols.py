"""Singer LDIF tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_ldif.protocols import FlextLdifProtocols as p_ldif
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano


class FlextMeltanoTapLdifProtocols(p_meltano, p_ldif):
    """Singer Tap LDIF protocols extending LDIF and Meltano protocols.

    Extends both FlextLdifProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all LDIF protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextLdifProtocols (inherits .Ldif.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Tap LDIF-specific protocols in TapLdif namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_tap_ldif.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # LDIF protocols (inherited)
    entry: p.Ldif.Models.EntryProtocol

    # Meltano protocols (inherited)
    tap: p.Meltano.TapProtocol

    # Tap LDIF-specific protocols
    parsing: p.TapLdif.LdifParsingProtocol
    """

    class TapLdif:
        """Singer Tap LDIF domain protocols for LDIF file processing and extraction."""

        @runtime_checkable
        class LdifParsingProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF file parsing operations."""

            def parse_ldif_file(
                self,
                file_path: str,
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Parse LDIF file to list of entries."""
                ...

            def parse_ldif_entry(
                self,
                entry_string: str,
            ) -> p_meltano.Result[dict[str, object]]:
                """Parse single LDIF entry."""
                ...

            def handle_change_records(
                self,
                entry: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Handle LDIF change record entries."""
                ...

            def decode_base64_attributes(
                self,
                entry: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Decode base64-encoded LDIF attributes."""
                ...

        @runtime_checkable
        class LdifTransformationProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF data transformation operations."""

            def transform_to_singer_record(
                self,
                ldif_entry: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Transform LDIF entry to Singer record format."""
                ...

            def normalize_attribute_names(
                self,
                entry: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Normalize LDIF attribute names."""
                ...

            def convert_data_types(
                self,
                entry: dict[str, object],
                schema: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Convert LDIF data types to schema types."""
                ...

            def apply_field_mappings(
                self,
                entry: dict[str, object],
                mappings: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Apply field name mappings."""
                ...

        @runtime_checkable
        class StreamGenerationProtocol(p_ldif.Service[object], Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def discover_streams(
                self,
                ldif_files: list[str],
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Discover available streams from LDIF files."""
                ...

            def get_stream_schema(
                self,
                stream_name: str,
            ) -> p_meltano.Result[dict[str, object]]:
                """Get schema for LDIF stream."""
                ...

            def sync_stream(
                self,
                stream_name: str,
                state: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Sync LDIF stream data."""
                ...

            def emit_singer_messages(
                self,
                records: list[dict[str, object]],
                stream_name: str,
            ) -> p_meltano.Result[bool]:
                """Emit Singer messages for records."""
                ...

        @runtime_checkable
        class ValidationProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF validation operations."""

            def validate_ldif_syntax(self, file_path: str) -> p_meltano.Result[bool]:
                """Validate LDIF file syntax."""
                ...

            def validate_entry_schema(
                self,
                entry: dict[str, object],
                schema: dict[str, object],
            ) -> p_meltano.Result[bool]:
                """Validate entry against schema."""
                ...

            def check_referential_integrity(
                self,
                entries: list[dict[str, object]],
            ) -> p_meltano.Result[dict[str, object]]:
                """Check referential integrity."""
                ...

            def validate_attribute_values(
                self,
                entry: dict[str, object],
                rules: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Validate attribute values."""
                ...

        @runtime_checkable
        class FileProcessingProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF file processing operations."""

            def process_file_stream(
                self,
                file_path: str,
                batch_size: int,
            ) -> p_meltano.Result[object]:
                """Process LDIF file as stream."""
                ...

            def handle_large_files(
                self,
                file_path: str,
                chunk_size: int,
            ) -> p_meltano.Result[object]:
                """Handle large LDIF files."""
                ...

            def process_directory(
                self,
                directory_path: str,
                pattern: str,
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Process directory of LDIF files."""
                ...

            def merge_multiple_files(
                self,
                file_paths: list[str],
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Merge multiple LDIF files."""
                ...

        @runtime_checkable
        class PerformanceProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF processing performance operations."""

            def optimize_parsing(
                self,
                config: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Optimize LDIF parsing performance."""
                ...

            def enable_parallel_processing(
                self, num_workers: int
            ) -> p_meltano.Result[bool]:
                """Enable parallel file processing."""
                ...

            def configure_memory_limits(
                self, max_memory_mb: int
            ) -> p_meltano.Result[bool]:
                """Configure memory usage limits."""
                ...

            def monitor_processing_speed(
                self,
            ) -> p_meltano.Result[dict[str, object]]:
                """Monitor processing speed metrics."""
                ...

        @runtime_checkable
        class MonitoringProtocol(p_ldif.Service[object], Protocol):
            """Protocol for LDIF processing monitoring."""

            def track_file_progress(
                self,
                file_path: str,
                progress: float,
            ) -> p_meltano.Result[bool]:
                """Track file processing progress."""
                ...

            def log_parsing_errors(
                self,
                error: str,
                _context: dict[str, object],
            ) -> p_meltano.Result[bool]:
                """Log parsing errors."""
                ...

            def get_processing_statistics(
                self,
            ) -> p_meltano.Result[dict[str, object]]:
                """Get processing statistics."""
                ...

            def monitor_resource_usage(
                self,
            ) -> p_meltano.Result[dict[str, object]]:
                """Monitor resource usage."""
                ...


# Runtime alias for simplified usage
p = FlextMeltanoTapLdifProtocols

__all__ = [
    "FlextMeltanoTapLdifProtocols",
    "p",
]
