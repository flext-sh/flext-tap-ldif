"""Singer LDIF tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, p


class FlextMeltanoTapLdifProtocols:
    """Singer Tap LDIF protocols with explicit re-exports from p foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapLdif namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    # ============================================================================
    # SINGER TAP LDIF-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TapLdif:
        """Singer Tap LDIF domain protocols for LDIF file processing and extraction."""

        @runtime_checkable
        class LdifParsingProtocol(p.Service, Protocol):
            """Protocol for LDIF file parsing operations."""

            def parse_ldif_file(
                self,
                file_path: str,
            ) -> FlextResult[list[dict[str, object]]]:
                """Parse LDIF file to list of entries."""

            def parse_ldif_entry(
                self,
                entry_string: str,
            ) -> FlextResult[dict[str, object]]:
                """Parse single LDIF entry."""

            def handle_change_records(
                self,
                entry: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Handle LDIF change record entries."""

            def decode_base64_attributes(
                self,
                entry: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Decode base64-encoded LDIF attributes."""

        @runtime_checkable
        class LdifTransformationProtocol(p.Service, Protocol):
            """Protocol for LDIF data transformation operations."""

            def transform_to_singer_record(
                self,
                ldif_entry: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Transform LDIF entry to Singer record format."""

            def normalize_attribute_names(
                self,
                entry: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Normalize LDIF attribute names."""

            def convert_data_types(
                self,
                entry: dict[str, object],
                schema: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Convert LDIF data types to schema types."""

            def apply_field_mappings(
                self,
                entry: dict[str, object],
                mappings: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Apply field name mappings."""

        @runtime_checkable
        class StreamGenerationProtocol(p.Service, Protocol):
            """Protocol for Singer stream generation from LDIF."""

            def discover_streams(
                self,
                ldif_files: list[str],
            ) -> FlextResult[list[dict[str, object]]]:
                """Discover available streams from LDIF files."""

            def get_stream_schema(
                self,
                stream_name: str,
            ) -> FlextResult[dict[str, object]]:
                """Get schema for LDIF stream."""

            def sync_stream(
                self,
                stream_name: str,
                state: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Sync LDIF stream data."""

            def emit_singer_messages(
                self,
                records: list[dict[str, object]],
                stream_name: str,
            ) -> FlextResult[None]:
                """Emit Singer messages for records."""

        @runtime_checkable
        class ValidationProtocol(p.Service, Protocol):
            """Protocol for LDIF validation operations."""

            def validate_ldif_syntax(self, file_path: str) -> FlextResult[bool]:
                """Validate LDIF file syntax."""

            def validate_entry_schema(
                self,
                entry: dict[str, object],
                schema: dict[str, object],
            ) -> FlextResult[bool]:
                """Validate entry against schema."""

            def check_referential_integrity(
                self,
                entries: list[dict[str, object]],
            ) -> FlextResult[dict[str, object]]:
                """Check referential integrity."""

            def validate_attribute_values(
                self,
                entry: dict[str, object],
                rules: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Validate attribute values."""

        @runtime_checkable
        class FileProcessingProtocol(p.Service, Protocol):
            """Protocol for LDIF file processing operations."""

            def process_file_stream(
                self,
                file_path: str,
                batch_size: int,
            ) -> FlextResult[object]:
                """Process LDIF file as stream."""

            def handle_large_files(
                self,
                file_path: str,
                chunk_size: int,
            ) -> FlextResult[object]:
                """Handle large LDIF files."""

            def process_directory(
                self,
                directory_path: str,
                pattern: str,
            ) -> FlextResult[list[dict[str, object]]]:
                """Process directory of LDIF files."""

            def merge_multiple_files(
                self,
                file_paths: list[str],
            ) -> FlextResult[list[dict[str, object]]]:
                """Merge multiple LDIF files."""

        @runtime_checkable
        class PerformanceProtocol(p.Service, Protocol):
            """Protocol for LDIF processing performance operations."""

            def optimize_parsing(
                self,
                config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Optimize LDIF parsing performance."""

            def enable_parallel_processing(self, num_workers: int) -> FlextResult[bool]:
                """Enable parallel file processing."""

            def configure_memory_limits(self, max_memory_mb: int) -> FlextResult[bool]:
                """Configure memory usage limits."""

            def monitor_processing_speed(
                self,
            ) -> FlextResult[dict[str, object]]:
                """Monitor processing speed metrics."""

        @runtime_checkable
        class MonitoringProtocol(p.Service, Protocol):
            """Protocol for LDIF processing monitoring."""

            def track_file_progress(
                self,
                file_path: str,
                progress: float,
            ) -> FlextResult[None]:
                """Track file processing progress."""

            def log_parsing_errors(
                self,
                error: str,
                _context: dict[str, object],
            ) -> FlextResult[None]:
                """Log parsing errors."""

            def get_processing_statistics(
                self,
            ) -> FlextResult[dict[str, object]]:
                """Get processing statistics."""

            def monitor_resource_usage(self) -> FlextResult[dict[str, object]]:
                """Monitor resource usage."""

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    # Core protocols
    @runtime_checkable
    class LdifParsingProtocol(TapLdif.LdifParsingProtocol):
        """LdifParsingProtocol - real inheritance."""

    @runtime_checkable
    class LdifTransformationProtocol(TapLdif.LdifTransformationProtocol):
        """LdifTransformationProtocol - real inheritance."""

    @runtime_checkable
    class StreamGenerationProtocol(TapLdif.StreamGenerationProtocol):
        """StreamGenerationProtocol - real inheritance."""

    @runtime_checkable
    class ValidationProtocol(TapLdif.ValidationProtocol):
        """ValidationProtocol - real inheritance."""

    @runtime_checkable
    class FileProcessingProtocol(TapLdif.FileProcessingProtocol):
        """FileProcessingProtocol - real inheritance."""

    @runtime_checkable
    class PerformanceProtocol(TapLdif.PerformanceProtocol):
        """PerformanceProtocol - real inheritance."""

    @runtime_checkable
    class MonitoringProtocol(TapLdif.MonitoringProtocol):
        """MonitoringProtocol - real inheritance."""

    # Convenience aliases
    @runtime_checkable
    class TapLdifParsingProtocol(TapLdif.LdifParsingProtocol):
        """TapLdifParsingProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifTransformationProtocol(TapLdif.LdifTransformationProtocol):
        """TapLdifTransformationProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifStreamGenerationProtocol(TapLdif.StreamGenerationProtocol):
        """TapLdifStreamGenerationProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifValidationProtocol(TapLdif.ValidationProtocol):
        """TapLdifValidationProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifFileProcessingProtocol(TapLdif.FileProcessingProtocol):
        """TapLdifFileProcessingProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifPerformanceProtocol(TapLdif.PerformanceProtocol):
        """TapLdifPerformanceProtocol - real inheritance."""

    @runtime_checkable
    class TapLdifMonitoringProtocol(TapLdif.MonitoringProtocol):
        """TapLdifMonitoringProtocol - real inheritance."""


__all__ = [
    "FlextMeltanoTapLdifProtocols",
]
