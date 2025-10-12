"""Singer LDIF tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextMeltanoTapLdifProtocols:
    """Singer Tap LDIF protocols with explicit re-exports from FlextCore.Protocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # SINGER TAP LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TapLdif:
        """Singer Tap LDIF domain protocols for LDIF file processing and extraction."""

        @runtime_checkable
        class LdifParsingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF file parsing operations."""

            def parse_ldif_file(
                self, file_path: str
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Parse LDIF file to list of entries."""

            def parse_ldif_entry(
                self, entry_string: str
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Parse single LDIF entry."""

            def handle_change_records(
                self, entry: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Handle LDIF change record entries."""

            def decode_base64_attributes(
                self, entry: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Decode base64-encoded LDIF attributes."""

        @runtime_checkable
        class LdifTransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF data transformation operations."""

            def transform_to_singer_record(
                self, ldif_entry: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Transform LDIF entry to Singer record format."""

            def normalize_attribute_names(
                self, entry: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Normalize LDIF attribute names."""

            def convert_data_types(
                self, entry: FlextCore.Types.Dict, schema: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Convert LDIF data types to schema types."""

            def apply_field_mappings(
                self, entry: FlextCore.Types.Dict, mappings: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Apply field name mappings."""

        @runtime_checkable
        class StreamGenerationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def discover_streams(
                self, ldif_files: FlextCore.Types.StringList
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Discover available streams from LDIF files."""

            def get_stream_schema(
                self, stream_name: str
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get schema for LDIF stream."""

            def sync_stream(
                self, stream_name: str, state: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Sync LDIF stream data."""

            def emit_singer_messages(
                self, records: list[FlextCore.Types.Dict], stream_name: str
            ) -> FlextCore.Result[None]:
                """Emit Singer messages for records."""

        @runtime_checkable
        class ValidationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF validation operations."""

            def validate_ldif_syntax(self, file_path: str) -> FlextCore.Result[bool]:
                """Validate LDIF file syntax."""

            def validate_entry_schema(
                self, entry: FlextCore.Types.Dict, schema: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]:
                """Validate entry against schema."""

            def check_referential_integrity(
                self, entries: list[FlextCore.Types.Dict]
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Check referential integrity."""

            def validate_attribute_values(
                self, entry: FlextCore.Types.Dict, rules: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Validate attribute values."""

        @runtime_checkable
        class FileProcessingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF file processing operations."""

            def process_file_stream(
                self, file_path: str, batch_size: int
            ) -> FlextCore.Result[object]:
                """Process LDIF file as stream."""

            def handle_large_files(
                self, file_path: str, chunk_size: int
            ) -> FlextCore.Result[object]:
                """Handle large LDIF files."""

            def process_directory(
                self, directory_path: str, pattern: str
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Process directory of LDIF files."""

            def merge_multiple_files(
                self, file_paths: FlextCore.Types.StringList
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]:
                """Merge multiple LDIF files."""

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF processing performance operations."""

            def optimize_parsing(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Optimize LDIF parsing performance."""

            def enable_parallel_processing(
                self, num_workers: int
            ) -> FlextCore.Result[bool]:
                """Enable parallel file processing."""

            def configure_memory_limits(
                self, max_memory_mb: int
            ) -> FlextCore.Result[bool]:
                """Configure memory usage limits."""

            def monitor_processing_speed(
                self,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor processing speed metrics."""

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for LDIF processing monitoring."""

            def track_file_progress(
                self, file_path: str, progress: float
            ) -> FlextCore.Result[None]:
                """Track file processing progress."""

            def log_parsing_errors(
                self, error: str, context: FlextCore.Types.Dict
            ) -> FlextCore.Result[None]:
                """Log parsing errors."""

            def get_processing_statistics(
                self,
            ) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Get processing statistics."""

            def monitor_resource_usage(self) -> FlextCore.Result[FlextCore.Types.Dict]:
                """Monitor resource usage."""

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # Core protocols
    LdifParsingProtocol = TapLdif.LdifParsingProtocol
    LdifTransformationProtocol = TapLdif.LdifTransformationProtocol
    StreamGenerationProtocol = TapLdif.StreamGenerationProtocol
    ValidationProtocol = TapLdif.ValidationProtocol
    FileProcessingProtocol = TapLdif.FileProcessingProtocol
    PerformanceProtocol = TapLdif.PerformanceProtocol
    MonitoringProtocol = TapLdif.MonitoringProtocol

    # Convenience aliases
    TapLdifParsingProtocol = TapLdif.LdifParsingProtocol
    TapLdifTransformationProtocol = TapLdif.LdifTransformationProtocol
    TapLdifStreamGenerationProtocol = TapLdif.StreamGenerationProtocol
    TapLdifValidationProtocol = TapLdif.ValidationProtocol
    TapLdifFileProcessingProtocol = TapLdif.FileProcessingProtocol
    TapLdifPerformanceProtocol = TapLdif.PerformanceProtocol
    TapLdifMonitoringProtocol = TapLdif.MonitoringProtocol


__all__ = [
    "FlextMeltanoTapLdifProtocols",
]
