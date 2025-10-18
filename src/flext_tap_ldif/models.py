"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Self

from flext_core import FlextConstants, FlextModels
from pydantic import (
    ConfigDict,
    Field,
    FieldSerializationInfo,
    computed_field,
    field_serializer,
    model_validator,
)

from flext_tap_ldif.utilities import FlextMeltanoTapLdifUtilities


class FlextMeltanoTapLdifModels(FlextModels):
    """Comprehensive models for LDIF tap operations extending FlextModels.

    Provides standardized models for all LDIF tap domain entities including:
    - Singer stream metadata and LDIF file configuration
    - LDIF file parsing and change record processing
    - Entry validation and transformation operations
    - Performance monitoring and batch processing metrics
    - LDIF format compliance and schema validation
    - All utility functions for LDIF data processing

    All nested classes inherit FlextModels validation and patterns.
    Consolidates ALL models for LDIF file extraction and processing.
    """

    # Pydantic 2.11 Configuration - Enterprise Singer LDIF Tap Features
    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        frozen=False,
        validate_return=True,
        ser_json_timedelta="iso8601",
        ser_json_bytes="base64",
        hide_input_in_errors=True,
        json_schema_extra={
            "title": "FLEXT Singer LDIF Tap Models",
            "description": "Enterprise LDIF file extraction models with Singer protocol compliance",
            "examples": [
                {
                    "tap_name": "tap-ldif",
                    "extraction_mode": "batch_file_processing",
                    "ldif_source": "/data/directory-export.ldif",
                }
            ],
            "tags": ["singer", "ldif", "tap", "extraction", "file-processing"],
            "version": "2.11.0",
        },
    )

    # Advanced Pydantic 2.11 Features - Singer LDIF Tap Domain

    @computed_field
    def active_ldif_tap_models_count(self) -> int:
        """Count of active LDIF tap models with file processing capabilities."""
        count = 0
        # Count core Singer LDIF tap models
        if hasattr(self, "LdifEntry"):
            count += 1
        if hasattr(self, "LdifChangeRecord"):
            count += 1
        if hasattr(self, "LdifFile"):
            count += 1
        if hasattr(self, "LdifStream"):
            count += 1
        if hasattr(self, "LdifBatch"):
            count += 1
        if hasattr(self, "LdifProcessingState"):
            count += 1
        if hasattr(self, "LdifTapConfig"):
            count += 1
        if hasattr(self, "LdifRecord"):
            count += 1
        if hasattr(self, "LdifValidationResult"):
            count += 1
        if hasattr(self, "LdifPerformanceMetrics"):
            count += 1
        return count

    @computed_field
    def ldif_tap_system_summary(self) -> dict[str, object]:
        """Comprehensive Singer LDIF tap system summary with file processing capabilities."""
        return {
            "total_models": self.active_ldif_tap_models_count,
            "tap_type": "singer_ldif_file_extractor",
            "extraction_features": [
                "ldif_file_parsing",
                "change_record_processing",
                "entry_validation",
                "batch_file_processing",
                "format_compliance_checking",
                "performance_monitoring",
            ],
            "singer_compliance": {
                "protocol_version": "singer_v1",
                "stream_discovery": True,
                "catalog_generation": True,
                "state_management": True,
                "file_bookmarking": True,
            },
            "ldif_capabilities": {
                "format_validation": True,
                "change_record_support": True,
                "batch_processing": True,
                "error_recovery": True,
                "schema_inference": True,
            },
        }

    @model_validator(mode="after")
    def validate_ldif_tap_system_consistency(self) -> Self:
        """Validate Singer LDIF tap system consistency and configuration."""
        # Singer LDIF tap file validation
        if (
            hasattr(self, "_ldif_files")
            and self._ldif_files
            and not hasattr(self, "LdifFile")
        ):
            msg = "LdifFile model required when LDIF files configured"
            raise ValueError(msg)

        # LDIF processing validation
        if (
            hasattr(self, "_batch_processing")
            and self._batch_processing
            and not hasattr(self, "LdifBatch")
        ):
            msg = "LdifBatch model required for batch processing"
            raise ValueError(msg)

        # Singer protocol compliance validation
        if hasattr(self, "_singer_mode") and self._singer_mode:
            required_models = ["LdifStream", "LdifRecord", "LdifProcessingState"]
            for model in required_models:
                if not hasattr(self, model):
                    msg = f"{model} required for Singer protocol compliance"
                    raise ValueError(msg)

        return self

    @field_serializer("*", when_used="json")
    def serialize_with_ldif_metadata(
        self, value: object, _info: FieldSerializationInfo
    ) -> object:
        """Add Singer LDIF tap metadata to all serialized fields."""
        if isinstance(value, dict):
            return {
                **value,
                "_ldif_tap_metadata": {
                    "extraction_timestamp": datetime.now(UTC).isoformat(),
                    "tap_type": "ldif_file_extractor",
                    "singer_protocol": "v1.0",
                    "data_source": "ldif_files",
                },
            }
        if isinstance(value, (str, int, float, bool)) and hasattr(
            self, "_include_ldif_metadata"
        ):
            return {
                "value": value,
                "_ldif_context": {
                    "extracted_at": datetime.now(UTC).isoformat(),
                    "tap_name": "flext-tap-ldif",
                },
            }
        return value

    # Legacy type aliases for backward compatibility
    LdifRecord = dict[str, object]
    LdifRecords = list[LdifRecord]

    class UtilityFunctions:
        """Utility functions for LDIF data processing."""

        @staticmethod
        def parse_dn(dn: str) -> dict[str, str]:
            """Parse Distinguished Name into components."""
            components = {}
            parts = dn.split(",")
            for part in parts:
                if "=" in part:
                    key, value = part.strip().split("=", 1)
                    components[key.strip()] = value.strip()
            return components

        @staticmethod
        def validate_ldif_line(line: str) -> bool:
            """Validate LDIF line format."""
            if not line or line.startswith("#"):
                return True  # Comment or empty line
            return ":" in line or line.startswith(" ")

        @staticmethod
        def decode_base64_value(value: str) -> str:
            """Decode base64 encoded LDIF value."""
            try:
                import base64

                return base64.b64decode(value).decode("utf-8")
            except Exception:
                return value

        @staticmethod
        def normalize_attribute_name(name: str) -> str:
            """Normalize LDIF attribute name."""
            return name.lower().strip()

    class LdifEntry(FlextModels.Entity):
        """Represents an LDIF entry with comprehensive parsing support."""

        # Pydantic 2.11 Configuration - LDIF Entry Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF directory entry with full attribute support",
                "examples": [
                    {
                        "dn": "cn=John Doe,ou=users,dc=example,dc=com",
                        "object_classes": ["inetOrgPerson", "organizationalPerson"],
                    }
                ],
            },
        )

        dn: str = Field(..., description="Distinguished Name")
        attributes: dict[str, list[str]] = Field(
            default_factory=dict, description="Entry attributes"
        )
        object_classes: list[str] = Field(
            default_factory=list, description="Object classes"
        )

        # LDIF metadata
        line_number: int = Field(
            default=0, description="Source line number in LDIF file"
        )
        source_file: str | None = Field(
            default=None, description="Source LDIF file path"
        )
        entry_type: str = Field(default="entry", description="Type of LDIF entry")

        # Processing metadata
        extracted_at: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Extraction timestamp",
        )
        processed: bool = Field(default=False, description="Processing status")
        validation_errors: list[str] = Field(
            default_factory=list, description="Validation errors"
        )

        @computed_field
        def ldif_entry_summary(self) -> dict[str, object]:
            """LDIF entry analysis summary."""
            return {
                "dn": self.dn,
                "attribute_count": len(self.attributes),
                "object_class_count": len(self.object_classes),
                "primary_object_class": self.object_classes[0]
                if self.object_classes
                else None,
                "entry_type": self.entry_type,
                "is_valid": len(self.validation_errors) == 0,
                "source_location": {"file": self.source_file, "line": self.line_number},
            }

        @model_validator(mode="after")
        def validate_ldif_entry(self) -> Self:
            """Validate LDIF entry structure."""
            if not self.dn:
                msg = "DN cannot be empty"
                raise ValueError(msg)

            # Validate object classes are in attributes
            if self.object_classes and "objectClass" not in self.attributes:
                self.attributes["objectClass"] = self.object_classes

            return self

        def get_attribute_values(self, name: str) -> list[str]:
            """Get attribute values by name (case-insensitive)."""
            normalized_name = name.lower()
            for attr_name, values in self.attributes.items():
                if attr_name.lower() == normalized_name:
                    return values
            return []

        def get_first_attribute_value(self, name: str) -> str | None:
            """Get first attribute value by name."""
            values = self.get_attribute_values(name)
            return values[0] if values else None

    class LdifChangeRecord(FlextModels.Entity):
        """Represents an LDIF change record for modify operations."""

        # Pydantic 2.11 Configuration - Change Record Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF change record with modification tracking",
                "examples": [
                    {
                        "dn": "cn=John Doe,ou=users,dc=example,dc=com",
                        "change_type": "modify",
                        "changes": [{"action": "replace", "attribute": "mail"}],
                    }
                ],
            },
        )

        dn: str = Field(..., description="Distinguished Name")
        change_type: str = Field(
            ..., description="Type of change (add, modify, delete, modrdn)"
        )
        changes: list[dict[str, object]] = Field(
            default_factory=list, description="List of changes"
        )

        # Change metadata
        changetype: str | None = Field(
            default=None, description="LDIF changetype directive"
        )
        line_number: int = Field(default=0, description="Source line number")
        source_file: str | None = Field(default=None, description="Source LDIF file")

        # Processing metadata
        extracted_at: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Extraction timestamp",
        )
        applied: bool = Field(default=False, description="Change application status")
        application_errors: list[str] = Field(
            default_factory=list, description="Application errors"
        )

        @computed_field
        def change_record_summary(self) -> dict[str, object]:
            """LDIF change record summary."""
            return {
                "dn": self.dn,
                "change_type": self.change_type,
                "change_count": len(self.changes),
                "has_errors": len(self.application_errors) > 0,
                "applied": self.applied,
                "source_location": {"file": self.source_file, "line": self.line_number},
            }

        @model_validator(mode="after")
        def validate_change_record(self) -> Self:
            """Validate LDIF change record."""
            if not self.dn:
                msg = "Change record DN cannot be empty"
                raise ValueError(msg)

            valid_types = ["add", "modify", "delete", "modrdn"]
            if self.change_type not in valid_types:
                msg = f"Invalid change type: {self.change_type}"
                raise ValueError(msg)

            return self

    class LdifFile(FlextModels.Entity):
        """Represents an LDIF file with processing metadata."""

        # Pydantic 2.11 Configuration - File Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF file with comprehensive processing support",
                "examples": [
                    {
                        "file_path": "/data/directory-export.ldif",
                        "file_size": 1048576,
                        "encoding": "utf-8",
                    }
                ],
            },
        )

        file_path: str = Field(..., description="Path to LDIF file")
        file_size: int = Field(default=0, description="File size in bytes")
        encoding: str = Field(default="utf-8", description="File encoding")

        # File metadata
        created_at: datetime | None = Field(
            default=None, description="File creation time"
        )
        modified_at: datetime | None = Field(
            default=None, description="File modification time"
        )

        # Processing statistics
        total_lines: int = Field(default=0, description="Total lines in file")
        entry_count: int = Field(default=0, description="Number of entries")
        change_record_count: int = Field(
            default=0, description="Number of change records"
        )
        comment_lines: int = Field(default=0, description="Number of comment lines")

        # Processing state
        processing_status: str = Field(
            default="pending", description="Processing status"
        )
        last_processed_line: int = Field(
            default=0, description="Last processed line number"
        )
        processing_errors: list[str] = Field(
            default_factory=list, description="Processing errors"
        )

        # Validation results
        is_valid_ldif: bool = Field(default=True, description="LDIF format validity")
        validation_errors: list[str] = Field(
            default_factory=list, description="Format validation errors"
        )

        @computed_field
        def ldif_file_summary(self) -> dict[str, object]:
            """LDIF file processing summary."""
            progress = 0.0
            if self.total_lines > 0:
                progress = self.last_processed_line / self.total_lines

            return {
                "file_path": self.file_path,
                "file_stats": {
                    "size_bytes": self.file_size,
                    "total_lines": self.total_lines,
                    "entries": self.entry_count,
                    "change_records": self.change_record_count,
                },
                "processing": {
                    "status": self.processing_status,
                    "progress_percent": progress * 100,
                    "errors": len(self.processing_errors),
                },
                "validation": {
                    "is_valid": self.is_valid_ldif,
                    "validation_errors": len(self.validation_errors),
                },
            }

        @model_validator(mode="after")
        def validate_ldif_file(self) -> Self:
            """Validate LDIF file configuration."""
            if not self.file_path:
                msg = "LDIF file path is required"
                raise ValueError(msg)
            if self.file_size < 0:
                msg = "File size cannot be negative"
                raise ValueError(msg)
            return self

    class LdifStream(FlextModels.Entity):
        """Singer stream configuration for LDIF file processing."""

        # Pydantic 2.11 Configuration - Stream Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Singer stream for LDIF file extraction",
                "examples": [
                    {
                        "stream_name": "ldif_entries",
                        "file_path": "/data/users.ldif",
                        "replication_method": "FULL_TABLE",
                    }
                ],
            },
        )

        stream_name: str = Field(..., description="Singer stream name")
        file_path: str = Field(..., description="LDIF file path")

        # Singer stream configuration
        tap_stream_id: str = Field(..., description="Singer tap stream ID")
        replication_method: str = Field(
            default="FULL_TABLE", description="Replication method"
        )
        key_properties: list[str] = Field(
            default_factory=lambda: ["dn"], description="Key properties"
        )

        # LDIF-specific settings
        include_change_records: bool = Field(
            default=True, description="Include LDIF change records"
        )
        filter_object_classes: list[str] = Field(
            default_factory=list, description="Filter by object classes"
        )
        batch_size: int = Field(
            default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE,
            description="Processing batch size",
        )

        # Stream schema
        schema: dict[str, object] = Field(
            default_factory=dict, description="JSON schema"
        )
        metadata: list[dict[str, object]] = Field(
            default_factory=list, description="Stream metadata"
        )

        @computed_field
        def ldif_stream_summary(self) -> dict[str, object]:
            """LDIF stream configuration summary."""
            return {
                "stream_id": self.tap_stream_id,
                "extraction_type": self.replication_method,
                "ldif_settings": {
                    "file_path": self.file_path,
                    "batch_size": self.batch_size,
                    "include_changes": self.include_change_records,
                },
                "filtering": {
                    "object_class_filters": len(self.filter_object_classes),
                    "has_filters": bool(self.filter_object_classes),
                },
                "has_schema": bool(self.schema),
            }

        @model_validator(mode="after")
        def validate_ldif_stream(self) -> Self:
            """Validate LDIF stream configuration."""
            if not self.stream_name:
                msg = "Stream name is required"
                raise ValueError(msg)
            if not self.file_path:
                msg = "LDIF file path is required"
                raise ValueError(msg)
            return self

    class LdifBatch(FlextModels.Entity):
        """LDIF batch processing configuration and state."""

        # Pydantic 2.11 Configuration - Batch Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF batch processing with performance optimization",
                "examples": [
                    {
                        "batch_id": "batch_001",
                        "file_paths": ["/data/users.ldif", "/data/groups.ldif"],
                        "batch_size": 1000,
                    }
                ],
            },
        )

        batch_id: str = Field(..., description="Unique batch identifier")
        file_paths: list[str] = Field(..., description="List of LDIF files to process")
        batch_size: int = Field(
            default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE,
            description="Processing batch size",
        )

        # Processing configuration
        parallel_processing: bool = Field(
            default=False, description="Enable parallel processing"
        )
        max_workers: int = Field(default=4, description="Maximum worker threads")
        error_threshold: int = Field(
            default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 10,
            description="Maximum errors before stopping",
        )

        # Batch state
        status: str = Field(default="pending", description="Batch processing status")
        started_at: datetime | None = Field(
            default=None, description="Batch start time"
        )
        completed_at: datetime | None = Field(
            default=None, description="Batch completion time"
        )

        # Processing metrics
        files_processed: int = Field(default=0, description="Number of files processed")
        entries_processed: int = Field(default=0, description="Total entries processed")
        errors_encountered: int = Field(
            default=0, description="Total errors encountered"
        )

        # Error tracking
        file_errors: dict[str, list[str]] = Field(
            default_factory=dict, description="Errors by file"
        )

        @computed_field
        def batch_processing_summary(self) -> dict[str, object]:
            """LDIF batch processing summary."""
            duration = 0.0
            if self.started_at and self.completed_at:
                duration = (self.completed_at - self.started_at).total_seconds()

            return {
                "batch_id": self.batch_id,
                "configuration": {
                    "file_count": len(self.file_paths),
                    "batch_size": self.batch_size,
                    "parallel": self.parallel_processing,
                    "max_workers": self.max_workers,
                },
                "progress": {
                    "status": self.status,
                    "files_processed": self.files_processed,
                    "entries_processed": self.entries_processed,
                    "duration_seconds": duration,
                },
                "quality": {
                    "errors_encountered": self.errors_encountered,
                    "error_rate": self.errors_encountered / self.entries_processed
                    if self.entries_processed > 0
                    else 0,
                    "files_with_errors": len(self.file_errors),
                },
            }

        @model_validator(mode="after")
        def validate_batch_config(self) -> Self:
            """Validate LDIF batch configuration."""
            if not self.batch_id:
                msg = "Batch ID is required"
                raise ValueError(msg)
            if not self.file_paths:
                msg = "At least one LDIF file is required"
                raise ValueError(msg)
            if self.batch_size <= 0:
                msg = "Batch size must be positive"
                raise ValueError(msg)
            return self

    class LdifProcessingState(FlextModels.Entity):
        """LDIF processing state and progress tracking."""

        # Pydantic 2.11 Configuration - State Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF processing state with comprehensive tracking",
                "examples": [
                    {
                        "file_path": "/data/users.ldif",
                        "entries_processed": 5000,
                        "processing_status": "in_progress",
                    }
                ],
            },
        )

        file_path: str = Field(..., description="LDIF file being processed")
        processing_status: str = Field(
            default="pending", description="Processing status"
        )

        # Progress tracking
        current_line: int = Field(default=0, description="Current line being processed")
        entries_processed: int = Field(default=0, description="Entries processed")
        change_records_processed: int = Field(
            default=0, description="Change records processed"
        )

        # Timing information
        started_at: datetime | None = Field(
            default=None, description="Processing start time"
        )
        last_update: datetime = Field(
            default_factory=lambda: datetime.now(UTC), description="Last state update"
        )
        estimated_completion: datetime | None = Field(
            default=None, description="Estimated completion time"
        )

        # Error tracking
        processing_errors: list[dict[str, object]] = Field(
            default_factory=list, description="Processing errors with context"
        )
        recoverable_errors: int = Field(
            default=0, description="Recoverable error count"
        )
        fatal_errors: int = Field(default=0, description="Fatal error count")

        # Performance metrics
        processing_rate: float = Field(default=0.0, description="Entries per second")
        memory_usage: int = Field(default=0, description="Memory usage in bytes")

        @computed_field
        def processing_progress_summary(self) -> dict[str, object]:
            """LDIF processing progress summary."""
            total_errors = self.recoverable_errors + self.fatal_errors
            duration = 0.0
            if self.started_at:
                duration = (datetime.now(UTC) - self.started_at).total_seconds()

            return {
                "file_path": self.file_path,
                "status": self.processing_status,
                "progress": {
                    "current_line": self.current_line,
                    "entries_processed": self.entries_processed,
                    "change_records": self.change_records_processed,
                    "processing_rate": self.processing_rate,
                },
                "timing": {
                    "duration_seconds": duration,
                    "estimated_completion": self.estimated_completion.isoformat()
                    if self.estimated_completion
                    else None,
                },
                "quality": {
                    "total_errors": total_errors,
                    "recoverable_errors": self.recoverable_errors,
                    "fatal_errors": self.fatal_errors,
                    "error_rate": total_errors / self.entries_processed
                    if self.entries_processed > 0
                    else 0,
                },
                "resources": {"memory_usage_mb": self.memory_usage / (1024 * 1024)},
            }

        @model_validator(mode="after")
        def validate_processing_state(self) -> Self:
            """Validate LDIF processing state."""
            if not self.file_path:
                msg = "File path is required"
                raise ValueError(msg)
            if self.current_line < 0:
                msg = "Current line cannot be negative"
                raise ValueError(msg)
            return self

    class LdifTapConfig(FlextModels.BaseConfig):
        """Configuration for LDIF tap operations."""

        # Pydantic 2.11 Configuration - Config Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF tap configuration with comprehensive settings",
                "examples": [
                    {
                        "ldif_directory": "/data/ldif",
                        "file_patterns": ["*.ldif"],
                        "batch_size": 1000,
                    }
                ],
            },
        )

        # File configuration
        ldif_directory: str | None = Field(
            default=None, description="LDIF files directory"
        )
        file_patterns: list[str] = Field(
            default_factory=lambda: ["*.ldif"], description="LDIF file patterns"
        )
        recursive_search: bool = Field(
            default=False, description="Recursive directory search"
        )

        # Processing configuration
        batch_size: int = Field(
            default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE,
            description="Processing batch size",
        )
        parallel_processing: bool = Field(
            default=False, description="Enable parallel processing"
        )
        max_workers: int = Field(default=4, description="Maximum worker threads")

        # Error handling
        continue_on_error: bool = Field(
            default=True, description="Continue processing on errors"
        )
        max_errors: int = Field(
            default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE,
            description="Maximum errors before stopping",
        )
        error_file: str | None = Field(default=None, description="Error output file")

        # Output configuration
        output_format: str = Field(default="jsonl", description="Output format")
        include_metadata: bool = Field(
            default=True, description="Include processing metadata"
        )
        compress_output: bool = Field(
            default=False, description="Compress output files"
        )

        @computed_field
        def tap_config_summary(self) -> dict[str, object]:
            """LDIF tap configuration summary."""
            return {
                "source": {
                    "directory": self.ldif_directory,
                    "patterns": self.file_patterns,
                    "recursive": self.recursive_search,
                },
                "processing": {
                    "batch_size": self.batch_size,
                    "parallel": self.parallel_processing,
                    "max_workers": self.max_workers,
                },
                "error_handling": {
                    "continue_on_error": self.continue_on_error,
                    "max_errors": self.max_errors,
                    "has_error_file": bool(self.error_file),
                },
                "output": {
                    "format": self.output_format,
                    "include_metadata": self.include_metadata,
                    "compressed": self.compress_output,
                },
            }

        @model_validator(mode="after")
        def validate_tap_config(self) -> Self:
            """Validate LDIF tap configuration."""
            if self.batch_size <= 0:
                msg = "Batch size must be positive"
                raise ValueError(msg)
            if self.max_workers <= 0:
                msg = "Max workers must be positive"
                raise ValueError(msg)
            return self

    class LdifRecord(FlextModels.StrictArbitraryTypesModel):
        """Individual LDIF record for Singer output."""

        stream: str = Field(..., description="Source stream name")
        record: dict[str, object] = Field(..., description="LDIF record data")
        record_type: str = Field(default="entry", description="Type of LDIF record")

        # Source metadata
        source_file: str | None = Field(default=None, description="Source LDIF file")
        line_number: int = Field(default=0, description="Source line number")

        # Extraction metadata
        time_extracted: datetime = Field(
            default_factory=lambda: datetime.now(UTC),
            description="Extraction timestamp",
        )
        processing_time: float = Field(
            default=0.0, description="Processing time in seconds"
        )

        @computed_field
        def ldif_record_summary(self) -> dict[str, object]:
            """LDIF record analysis summary."""
            return {
                "stream": self.stream,
                "record_type": self.record_type,
                "field_count": len(self.record),
                "has_dn": "dn" in self.record,
                "source": {"file": self.source_file, "line": self.line_number},
                "extraction_time": self.time_extracted.isoformat(),
                "processing_time_ms": self.processing_time * 1000,
                "record_size_bytes": len(str(self.record).encode("utf-8")),
            }

        @model_validator(mode="after")
        def validate_ldif_record(self) -> Self:
            """Validate LDIF record structure."""
            if not self.stream:
                msg = "Stream name is required"
                raise ValueError(msg)
            if not self.record:
                msg = "Record data cannot be empty"
                raise ValueError(msg)
            return self

    class LdifValidationResult(FlextModels.StrictArbitraryTypesModel):
        """LDIF validation result with detailed error reporting."""

        file_path: str = Field(..., description="Validated LDIF file path")
        is_valid: bool = Field(..., description="Overall validation result")

        # Validation results
        validation_errors: list[dict[str, object]] = Field(
            default_factory=list, description="Validation errors with details"
        )
        warnings: list[dict[str, object]] = Field(
            default_factory=list, description="Validation warnings"
        )

        # Statistics
        total_entries: int = Field(default=0, description="Total entries validated")
        valid_entries: int = Field(default=0, description="Valid entries count")
        invalid_entries: int = Field(default=0, description="Invalid entries count")

        # Validation metadata
        validation_time: float = Field(
            default=0.0, description="Validation time in seconds"
        )
        validator_version: str = Field(default="1.0", description="Validator version")

        @computed_field
        def validation_summary(self) -> dict[str, object]:
            """LDIF validation comprehensive summary."""
            success_rate = 0.0
            if self.total_entries > 0:
                success_rate = self.valid_entries / self.total_entries

            return {
                "file_path": self.file_path,
                "validation_result": "valid" if self.is_valid else "invalid",
                "statistics": {
                    "total_entries": self.total_entries,
                    "valid_entries": self.valid_entries,
                    "invalid_entries": self.invalid_entries,
                    "success_rate": success_rate,
                },
                "issues": {
                    "error_count": len(self.validation_errors),
                    "warning_count": len(self.warnings),
                    "has_critical_errors": any(
                        error.get("severity") == "critical"
                        for error in self.validation_errors
                    ),
                },
                "performance": {
                    "validation_time_seconds": self.validation_time,
                    "entries_per_second": self.total_entries / self.validation_time
                    if self.validation_time > 0
                    else 0,
                },
            }

        @model_validator(mode="after")
        def validate_result_consistency(self) -> Self:
            """Validate result consistency."""
            if self.valid_entries + self.invalid_entries != self.total_entries:
                msg = "Valid + invalid entries must equal total entries"
                raise ValueError(msg)
            if self.is_valid and self.validation_errors:
                msg = "Cannot be valid with validation errors"
                raise ValueError(msg)
            return self

    class LdifPerformanceMetrics(FlextModels.StrictArbitraryTypesModel):
        """Performance metrics for LDIF tap operations."""

        # File processing metrics
        files_processed: int = Field(default=0, description="Number of files processed")
        total_file_size: int = Field(default=0, description="Total file size in bytes")
        average_file_size: float = Field(default=0.0, description="Average file size")

        # Entry processing metrics
        total_entries: int = Field(default=0, description="Total entries processed")
        entries_per_file: float = Field(
            default=0.0, description="Average entries per file"
        )
        processing_rate: float = Field(default=0.0, description="Entries per second")

        # Time metrics
        total_processing_time: float = Field(
            default=0.0, description="Total processing time"
        )
        average_processing_time: float = Field(
            default=0.0, description="Average time per file"
        )
        parsing_time: float = Field(default=0.0, description="Time spent parsing")
        validation_time: float = Field(default=0.0, description="Time spent validating")

        # Quality metrics
        successful_files: int = Field(
            default=0, description="Successfully processed files"
        )
        failed_files: int = Field(default=0, description="Failed file processing")
        total_errors: int = Field(default=0, description="Total processing errors")

        # Resource metrics
        peak_memory_usage: int = Field(
            default=0, description="Peak memory usage in bytes"
        )
        average_memory_usage: int = Field(default=0, description="Average memory usage")

        @computed_field
        def performance_analysis_summary(self) -> dict[str, object]:
            """LDIF tap performance analysis summary."""
            success_rate = 0.0
            if self.files_processed > 0:
                success_rate = self.successful_files / self.files_processed

            return {
                "file_processing": {
                    "files_processed": self.files_processed,
                    "success_rate": success_rate,
                    "total_size_mb": self.total_file_size / (1024 * 1024),
                    "average_size_mb": self.average_file_size / (1024 * 1024),
                },
                "entry_processing": {
                    "total_entries": self.total_entries,
                    "processing_rate": self.processing_rate,
                    "entries_per_file": self.entries_per_file,
                },
                "performance": {
                    "total_time_seconds": self.total_processing_time,
                    "parsing_time_seconds": self.parsing_time,
                    "validation_time_seconds": self.validation_time,
                    "time_per_file": self.average_processing_time,
                },
                "quality": {
                    "successful_files": self.successful_files,
                    "failed_files": self.failed_files,
                    "total_errors": self.total_errors,
                    "error_rate": self.total_errors / self.total_entries
                    if self.total_entries > 0
                    else 0,
                },
                "resources": {
                    "peak_memory_mb": self.peak_memory_usage / (1024 * 1024),
                    "average_memory_mb": self.average_memory_usage / (1024 * 1024),
                },
            }

        @model_validator(mode="after")
        def validate_performance_metrics(self) -> Self:
            """Validate performance metrics consistency."""
            if self.files_processed < 0:
                msg = "Files processed cannot be negative"
                raise ValueError(msg)
            if self.successful_files + self.failed_files > self.files_processed:
                msg = "Successful + failed files cannot exceed total files"
                raise ValueError(msg)
            return self


# ZERO TOLERANCE CONSOLIDATION - FlextMeltanoTapLdifUtilities moved to utilities.py
#
# CRITICAL: FlextMeltanoTapLdifUtilities was DUPLICATED between models.py and utilities.py.
# This was a ZERO TOLERANCE violation of the user's explicit requirements.
#
# Note: FlextMeltanoTapLdifUtilities imported at top for proper organization


# Public API exports following FLEXT standardized patterns
__all__ = [
    "FlextMeltanoTapLdifModels",  # Unified models class
    "FlextMeltanoTapLdifUtilities",  # Standardized [Project]Utilities pattern
]
