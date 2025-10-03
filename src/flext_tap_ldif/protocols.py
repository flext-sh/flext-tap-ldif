"""Singer LDIF tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult, FlextTypes


class FlextTapLdifProtocols:
    """Singer Tap LDIF protocols with explicit re-exports from FlextProtocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextProtocols.Foundation
    Domain = FlextProtocols.Domain
    Application = FlextProtocols.Application
    Infrastructure = FlextProtocols.Infrastructure
    Extensions = FlextProtocols.Extensions
    Commands = FlextProtocols.Commands

    # ============================================================================
    # SINGER TAP LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TapLdif:
        """Singer Tap LDIF domain protocols for LDIF file processing and extraction."""

        @runtime_checkable
        class LdifParsingProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF file parsing operations."""

            def parse_ldif_file(
                self, file_path: str
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Parse LDIF file to list of entries."""

            def parse_ldif_entry(
                self, entry_string: str
            ) -> FlextResult[FlextTypes.Dict]:
                """Parse single LDIF entry."""

            def handle_change_records(
                self, entry: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Handle LDIF change record entries."""

            def decode_base64_attributes(
                self, entry: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Decode base64-encoded LDIF attributes."""

        @runtime_checkable
        class LdifTransformationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF data transformation operations."""

            def transform_to_singer_record(
                self, ldif_entry: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Transform LDIF entry to Singer record format."""

            def normalize_attribute_names(
                self, entry: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Normalize LDIF attribute names."""

            def convert_data_types(
                self, entry: FlextTypes.Dict, schema: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Convert LDIF data types to schema types."""

            def apply_field_mappings(
                self, entry: FlextTypes.Dict, mappings: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Apply field name mappings."""

        @runtime_checkable
        class StreamGenerationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def discover_streams(
                self, ldif_files: list[str]
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Discover available streams from LDIF files."""

            def get_stream_schema(
                self, stream_name: str
            ) -> FlextResult[FlextTypes.Dict]:
                """Get schema for LDIF stream."""

            def sync_stream(
                self, stream_name: str, state: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Sync LDIF stream data."""

            def emit_singer_messages(
                self, records: list[FlextTypes.Dict], stream_name: str
            ) -> FlextResult[None]:
                """Emit Singer messages for records."""

        @runtime_checkable
        class ValidationProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF validation operations."""

            def validate_ldif_syntax(self, file_path: str) -> FlextResult[bool]:
                """Validate LDIF file syntax."""

            def validate_entry_schema(
                self, entry: FlextTypes.Dict, schema: FlextTypes.Dict
            ) -> FlextResult[bool]:
                """Validate entry against schema."""

            def check_referential_integrity(
                self, entries: list[FlextTypes.Dict]
            ) -> FlextResult[FlextTypes.Dict]:
                """Check referential integrity."""

            def validate_attribute_values(
                self, entry: FlextTypes.Dict, rules: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Validate attribute values."""

        @runtime_checkable
        class FileProcessingProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF file processing operations."""

            def process_file_stream(
                self, file_path: str, batch_size: int
            ) -> FlextResult[FlextTypes.Any]:
                """Process LDIF file as stream."""

            def handle_large_files(
                self, file_path: str, chunk_size: int
            ) -> FlextResult[FlextTypes.Any]:
                """Handle large LDIF files."""

            def process_directory(
                self, directory_path: str, pattern: str
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Process directory of LDIF files."""

            def merge_multiple_files(
                self, file_paths: list[str]
            ) -> FlextResult[list[FlextTypes.Dict]]:
                """Merge multiple LDIF files."""

        @runtime_checkable
        class PerformanceProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF processing performance operations."""

            def optimize_parsing(
                self, config: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]:
                """Optimize LDIF parsing performance."""

            def enable_parallel_processing(self, num_workers: int) -> FlextResult[bool]:
                """Enable parallel file processing."""

            def configure_memory_limits(self, max_memory_mb: int) -> FlextResult[bool]:
                """Configure memory usage limits."""

            def monitor_processing_speed(self) -> FlextResult[FlextTypes.Dict]:
                """Monitor processing speed metrics."""

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
            """Protocol for LDIF processing monitoring."""

            def track_file_progress(
                self, file_path: str, progress: float
            ) -> FlextResult[None]:
                """Track file processing progress."""

            def log_parsing_errors(
                self, error: str, context: FlextTypes.Dict
            ) -> FlextResult[None]:
                """Log parsing errors."""

            def get_processing_statistics(self) -> FlextResult[FlextTypes.Dict]:
                """Get processing statistics."""

            def monitor_resource_usage(self) -> FlextResult[FlextTypes.Dict]:
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
    "FlextTapLdifProtocols",
]
