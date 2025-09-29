"""Singer LDIF tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


class FlextTapLdifProtocols(FlextProtocols):
    """Singer LDIF tap protocols extending FlextProtocols with LDIF file processing interfaces.

    This class provides protocol definitions for Singer LDIF tap operations including
    LDIF file parsing, validation, transformation, and stream generation for analytics.
    """

    @runtime_checkable
    class LdifParsingProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF file parsing operations."""

        def parse_ldif_file(
            self,
            file_path: str,
            parsing_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Parse LDIF file and extract entries.

            Args:
                file_path: Path to LDIF file
                parsing_config: LDIF parsing configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Parsed LDIF entries or error

            """
            ...

        def parse_ldif_stream(
            self,
            stream_data: str,
            parsing_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Parse LDIF data from stream.

            Args:
                stream_data: LDIF data as string
                parsing_config: LDIF parsing configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Parsed LDIF entries or error

            """
            ...

        def validate_ldif_format(
            self, file_path: str
        ) -> FlextResult[dict[str, object]]:
            """Validate LDIF file format compliance.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """
            ...

        def extract_ldif_metadata(
            self, file_path: str
        ) -> FlextResult[dict[str, object]]:
            """Extract metadata from LDIF file.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[dict[str, object]]: LDIF metadata or error

            """
            ...

    @runtime_checkable
    class LdifTransformationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF data transformation operations."""

        def transform_to_singer_format(
            self,
            ldif_entries: list[dict[str, object]],
            transformation_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Transform LDIF entries to Singer format.

            Args:
                ldif_entries: Raw LDIF entries
                transformation_config: Transformation parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Transformed entries or error

            """
            ...

        def normalize_attribute_values(
            self,
            entries: list[dict[str, object]],
            normalization_rules: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Normalize LDIF attribute values for consistency.

            Args:
                entries: LDIF entries to normalize
                normalization_rules: Normalization configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Normalized entries or error

            """
            ...

        def resolve_change_records(
            self,
            entries: list[dict[str, object]],
            resolution_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Resolve LDIF change records into final state.

            Args:
                entries: LDIF entries with change records
                resolution_config: Change resolution configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Resolved entries or error

            """
            ...

        def apply_schema_mapping(
            self,
            entries: list[dict[str, object]],
            schema_mapping: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Apply schema mapping to LDIF entries.

            Args:
                entries: LDIF entries to map
                schema_mapping: Schema mapping configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Mapped entries or error

            """
            ...

    @runtime_checkable
    class StreamGenerationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Singer stream generation from LDIF data."""

        def discover_streams_from_ldif(
            self, file_path: str, discovery_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Discover Singer streams from LDIF file structure.

            Args:
                file_path: Path to LDIF file
                discovery_config: Stream discovery configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Discovered stream definitions or error

            """
            ...

        def generate_schema_from_ldif(
            self,
            ldif_entries: list[dict[str, object]],
            schema_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Generate JSON schema from LDIF entries.

            Args:
                ldif_entries: Sample LDIF entries
                schema_config: Schema generation configuration

            Returns:
                FlextResult[dict[str, object]]: Generated JSON schema or error

            """
            ...

        def create_entry_stream(
            self,
            ldif_entries: list[dict[str, object]],
            stream_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Create Singer stream for LDIF entries.

            Args:
                ldif_entries: LDIF entries for stream
                stream_config: Stream configuration

            Returns:
                FlextResult[dict[str, object]]: Stream definition or error

            """
            ...

        def create_change_stream(
            self,
            change_records: list[dict[str, object]],
            stream_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Create Singer stream for LDIF change records.

            Args:
                change_records: LDIF change records
                stream_config: Stream configuration

            Returns:
                FlextResult[dict[str, object]]: Change stream definition or error

            """
            ...

    @runtime_checkable
    class ValidationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF data validation operations."""

        def validate_entry_structure(
            self,
            entries: list[dict[str, object]],
            validation_rules: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate LDIF entry structure and required attributes.

            Args:
                entries: LDIF entries to validate
                validation_rules: Validation configuration

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """
            ...

        def validate_dn_syntax(
            self, entries: list[dict[str, object]]
        ) -> FlextResult[dict[str, object]]:
            """Validate DN syntax in LDIF entries.

            Args:
                entries: LDIF entries to validate

            Returns:
                FlextResult[dict[str, object]]: DN validation results or error

            """
            ...

        def check_referential_integrity(
            self,
            entries: list[dict[str, object]],
            integrity_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Check referential integrity in LDIF entries.

            Args:
                entries: LDIF entries to check
                integrity_config: Integrity check configuration

            Returns:
                FlextResult[dict[str, object]]: Integrity check results or error

            """
            ...

        def detect_duplicate_entries(
            self, entries: list[dict[str, object]]
        ) -> FlextResult[list[dict[str, object]]]:
            """Detect duplicate entries in LDIF data.

            Args:
                entries: LDIF entries to analyze

            Returns:
                FlextResult[list[dict[str, object]]]: Detected duplicates or error

            """
            ...

    @runtime_checkable
    class FileProcessingProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF file processing operations."""

        def process_single_file(
            self, file_path: str, processing_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Process single LDIF file for extraction.

            Args:
                file_path: Path to LDIF file
                processing_config: File processing configuration

            Returns:
                FlextResult[dict[str, object]]: Processing results or error

            """
            ...

        def process_directory(
            self, directory_path: str, processing_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Process all LDIF files in directory.

            Args:
                directory_path: Directory containing LDIF files
                processing_config: Directory processing configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Processing results or error

            """
            ...

        def handle_large_files(
            self, file_path: str, streaming_config: dict[str, object]
        ) -> FlextResult[object]:
            """Handle large LDIF files with streaming processing.

            Args:
                file_path: Path to large LDIF file
                streaming_config: Streaming processing configuration

            Returns:
                FlextResult[object]: Streaming processor or error

            """
            ...

        def monitor_file_processing(
            self, processing_id: str
        ) -> FlextResult[dict[str, object]]:
            """Monitor file processing progress.

            Args:
                processing_id: Processing operation identifier

            Returns:
                FlextResult[dict[str, object]]: Processing status or error

            """
            ...

    @runtime_checkable
    class PerformanceProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF tap performance optimization operations."""

        def optimize_parsing_performance(
            self, parsing_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize LDIF parsing for performance.

            Args:
                parsing_config: Current parsing configuration

            Returns:
                FlextResult[dict[str, object]]: Optimized configuration or error

            """
            ...

        def configure_memory_management(
            self, memory_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Configure memory management for large LDIF files.

            Args:
                memory_config: Memory management configuration

            Returns:
                FlextResult[dict[str, object]]: Memory configuration result or error

            """
            ...

        def monitor_processing_performance(
            self, performance_metrics: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Monitor LDIF processing performance metrics.

            Args:
                performance_metrics: Performance monitoring data

            Returns:
                FlextResult[dict[str, object]]: Performance analysis or error

            """
            ...

        def optimize_stream_generation(
            self, stream_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize Singer stream generation performance.

            Args:
                stream_config: Stream generation configuration

            Returns:
                FlextResult[dict[str, object]]: Optimization results or error

            """
            ...

    @runtime_checkable
    class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for LDIF tap monitoring operations."""

        def track_processing_metrics(
            self, processing_id: str, metrics: dict[str, object]
        ) -> FlextResult[bool]:
            """Track LDIF processing metrics.

            Args:
                processing_id: Processing identifier
                metrics: Processing metrics data

            Returns:
                FlextResult[bool]: Metric tracking success status

            """
            ...

        def monitor_file_health(self, file_path: str) -> FlextResult[dict[str, object]]:
            """Monitor LDIF file health status.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[dict[str, object]]: File health status or error

            """
            ...

        def get_processing_status(
            self, processing_id: str
        ) -> FlextResult[dict[str, object]]:
            """Get LDIF processing status.

            Args:
                processing_id: Processing identifier

            Returns:
                FlextResult[dict[str, object]]: Processing status or error

            """
            ...

        def create_monitoring_dashboard(
            self, dashboard_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Create monitoring dashboard for LDIF tap operations.

            Args:
                dashboard_config: Dashboard configuration

            Returns:
                FlextResult[dict[str, object]]: Dashboard creation result or error

            """
            ...

    # Convenience aliases for easier downstream usage
    TapLdifParsingProtocol = LdifParsingProtocol
    TapLdifTransformationProtocol = LdifTransformationProtocol
    TapLdifStreamGenerationProtocol = StreamGenerationProtocol
    TapLdifValidationProtocol = ValidationProtocol
    TapLdifFileProcessingProtocol = FileProcessingProtocol
    TapLdifPerformanceProtocol = PerformanceProtocol
    TapLdifMonitoringProtocol = MonitoringProtocol


__all__ = [
    "FlextTapLdifProtocols",
]
