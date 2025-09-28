"""Module docstring."""

from __future__ import annotations

import os
from pathlib import Path

"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from flext_core import FlextModels


class FlextTapLdifModels(FlextModels):
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
    @property
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
    @property
    def ldif_tap_system_summary(self) -> dict[str, Any]:
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
        if hasattr(self, "_ldif_files") and self._ldif_files:
            if not hasattr(self, "LdifFile"):
                msg = "LdifFile model required when LDIF files configured"
                raise ValueError(msg)

        # LDIF processing validation
        if hasattr(self, "_batch_processing") and self._batch_processing:
            if not hasattr(self, "LdifBatch"):
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
    def serialize_with_ldif_metadata(self, value: Any, _info) -> Any:
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
        @property
        def ldif_entry_summary(self) -> dict[str, Any]:
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
        changes: list[dict[str, Any]] = Field(
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
        @property
        def change_record_summary(self) -> dict[str, Any]:
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
        @property
        def ldif_file_summary(self) -> dict[str, Any]:
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
        batch_size: int = Field(default=1000, description="Processing batch size")

        # Stream schema
        schema: dict[str, Any] = Field(default_factory=dict, description="JSON schema")
        metadata: list[dict[str, Any]] = Field(
            default_factory=list, description="Stream metadata"
        )

        @computed_field
        @property
        def ldif_stream_summary(self) -> dict[str, Any]:
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
        batch_size: int = Field(default=1000, description="Processing batch size")

        # Processing configuration
        parallel_processing: bool = Field(
            default=False, description="Enable parallel processing"
        )
        max_workers: int = Field(default=4, description="Maximum worker threads")
        error_threshold: int = Field(
            default=100, description="Maximum errors before stopping"
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
        @property
        def batch_processing_summary(self) -> dict[str, Any]:
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
        processing_errors: list[dict[str, Any]] = Field(
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
        @property
        def processing_progress_summary(self) -> dict[str, Any]:
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
        batch_size: int = Field(default=1000, description="Processing batch size")
        parallel_processing: bool = Field(
            default=False, description="Enable parallel processing"
        )
        max_workers: int = Field(default=4, description="Maximum worker threads")

        # Error handling
        continue_on_error: bool = Field(
            default=True, description="Continue processing on errors"
        )
        max_errors: int = Field(
            default=1000, description="Maximum errors before stopping"
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
        @property
        def tap_config_summary(self) -> dict[str, Any]:
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

    class LdifRecord(FlextModels.BaseModel):
        """Individual LDIF record for Singer output."""

        # Pydantic 2.11 Configuration - Record Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Singer LDIF record with extraction metadata",
                "examples": [
                    {
                        "stream": "ldif_entries",
                        "record": {"dn": "cn=John,dc=example,dc=com"},
                        "time_extracted": "2023-01-01T00:00:00Z",
                    }
                ],
            },
        )

        stream: str = Field(..., description="Source stream name")
        record: dict[str, Any] = Field(..., description="LDIF record data")
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
        @property
        def ldif_record_summary(self) -> dict[str, Any]:
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

    class LdifValidationResult(FlextModels.BaseModel):
        """LDIF validation result with detailed error reporting."""

        # Pydantic 2.11 Configuration - Validation Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF validation result with comprehensive error analysis",
                "examples": [
                    {
                        "file_path": "/data/users.ldif",
                        "is_valid": True,
                        "validation_errors": [],
                    }
                ],
            },
        )

        file_path: str = Field(..., description="Validated LDIF file path")
        is_valid: bool = Field(..., description="Overall validation result")

        # Validation results
        validation_errors: list[dict[str, Any]] = Field(
            default_factory=list, description="Validation errors with details"
        )
        warnings: list[dict[str, Any]] = Field(
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
        @property
        def validation_summary(self) -> dict[str, Any]:
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

    class LdifPerformanceMetrics(FlextModels.BaseModel):
        """Performance metrics for LDIF tap operations."""

        # Pydantic 2.11 Configuration - Metrics Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF tap performance metrics with comprehensive monitoring",
                "examples": [
                    {
                        "files_processed": 10,
                        "total_entries": 50000,
                        "processing_rate": 1000.0,
                    }
                ],
            },
        )

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
        @property
        def performance_analysis_summary(self) -> dict[str, Any]:
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


import pathlib

from flext_core import FlextResult, FlextUtilities


class FlextTapLdifUtilities(FlextUtilities):
    """Unified LDIF tap utilities extending FlextUtilities.

    Provides comprehensive utilities for LDIF Singer tap operations including:
    - LDIF file validation and format checking
    - Singer tap configuration generation for LDIF processing
    - LDIF-to-Singer schema mapping and transformation
    - File size and encoding validation
    - Performance optimization for LDIF extraction operations
    - Error handling and recovery mechanisms for LDIF processing
    """

    class _LdifFileHelper:
        """Helper for LDIF file validation and management."""

        @staticmethod
        def validate_ldif_file_accessibility(file_path: str) -> FlextResult[dict]:
            """Validate LDIF file accessibility, size, and basic format."""
            if not isinstance(file_path, str) or not file_path.strip():
                return FlextResult[dict].fail(
                    "LDIF file path must be a non-empty string"
                )

            file_path_obj = Path(file_path)

            # Check file existence
            if not file_path_obj.exists():
                return FlextResult[dict].fail(f"LDIF file does not exist: {file_path}")

            # Check if it's a file (not directory)
            if not file_path_obj.is_file():
                return FlextResult[dict].fail(f"Path is not a file: {file_path}")

            # Check file readability
            if not os.access(file_path, os.R_OK):
                return FlextResult[dict].fail(f"LDIF file is not readable: {file_path}")

            try:
                # Get file stats
                file_stats = file_path_obj.stat()
                file_size_bytes = file_stats.st_size
                file_size_mb = file_size_bytes / (1024 * 1024)

                # Check if file is empty
                if file_size_bytes == 0:
                    return FlextResult[dict].fail(f"LDIF file is empty: {file_path}")

                # Basic format validation - check for LDIF characteristics
                format_validation = (
                    FlextTapLdifUtilities._LdifFileHelper._validate_basic_ldif_format(
                        file_path
                    )
                )
                if format_validation.is_failure:
                    return FlextResult[dict].fail(
                        f"LDIF format validation failed: {format_validation.error}"
                    )

                file_info = {
                    "file_path": str(file_path_obj.resolve()),
                    "file_size_bytes": file_size_bytes,
                    "file_size_mb": round(file_size_mb, 2),
                    "is_accessible": True,
                    "format_valid": True,
                    "modified_time": file_stats.st_mtime,
                }

                # Add warnings for large files
                if file_size_mb > 100:
                    file_info["warning"] = (
                        f"Large LDIF file detected ({file_size_mb:.1f}MB). Consider batch processing."
                    )
                elif file_size_mb > 500:
                    file_info["warning"] = (
                        f"Very large LDIF file detected ({file_size_mb:.1f}MB). Processing may be slow."
                    )

                return FlextResult[dict].ok(file_info)

            except OSError as e:
                return FlextResult[dict].fail(
                    f"Error accessing LDIF file {file_path}: {e}"
                )

        @staticmethod
        def _validate_basic_ldif_format(file_path: str) -> FlextResult[bool]:
            """Perform basic LDIF format validation by checking file content."""
            try:
                with pathlib.Path(file_path).open(
                    encoding="utf-8", errors="ignore"
                ) as f:
                    # Read first few lines to check LDIF characteristics
                    lines_checked = 0
                    has_dn_line = False

                    for line in f:
                        lines_checked += 1
                        line = line.strip()

                        # Skip empty lines and comments
                        if not line or line.startswith("#"):
                            continue

                        # Look for DN line (required in LDIF)
                        if line.lower().startswith("dn:"):
                            has_dn_line = True

                        # Look for attribute lines (name: value)
                        if ":" in line and not line.startswith("dn:"):
                            pass

                        # Check enough lines to validate format
                        if lines_checked > 50 and has_dn_line:
                            break

                        # Avoid reading entire large files
                        if lines_checked > 100:
                            break

                    if not has_dn_line:
                        return FlextResult[bool].fail(
                            "No valid DN entries found in LDIF file"
                        )

                    return FlextResult[bool].ok(True)

            except UnicodeDecodeError:
                # Try with different encoding
                try:
                    with pathlib.Path(file_path).open(encoding="iso-8859-1") as f:
                        # Basic check with fallback encoding
                        content_sample = f.read(1024)
                        if "dn:" in content_sample.lower():
                            return FlextResult[bool].ok(True)
                        return FlextResult[bool].fail(
                            "No DN entries found with fallback encoding"
                        )
                except Exception as e:
                    return FlextResult[bool].fail(
                        f"Encoding error reading LDIF file: {e}"
                    )

            except Exception as e:
                return FlextResult[bool].fail(f"Error validating LDIF format: {e}")

        @staticmethod
        def detect_ldif_encoding(file_path: str) -> FlextResult[str]:
            """Detect the encoding of an LDIF file."""
            import chardet

            try:
                # Read a sample of the file for encoding detection
                with pathlib.Path(file_path).open("rb") as f:
                    raw_data = f.read(
                        min(32768, pathlib.Path(file_path).stat().st_size)
                    )  # Read up to 32KB

                # Use chardet to detect encoding
                encoding_result = chardet.detect(raw_data)
                detected_encoding = encoding_result.get("encoding")
                confidence = encoding_result.get("confidence", 0)

                if detected_encoding and confidence > 0.7:
                    # Validate detected encoding by trying to read the file
                    try:
                        with pathlib.Path(file_path).open(
                            encoding=detected_encoding
                        ) as f:
                            f.read(1024)  # Try to read some content
                        return FlextResult[str].ok(detected_encoding)
                    except UnicodeDecodeError:
                        pass

                # Fallback to common encodings
                for encoding in ["utf-8", "iso-8859-1", "cp1252", "utf-16"]:
                    try:
                        with pathlib.Path(file_path).open(encoding=encoding) as f:
                            f.read(1024)  # Try to read some content
                        return FlextResult[str].ok(encoding)
                    except UnicodeDecodeError:
                        continue

                return FlextResult[str].fail(
                    "Could not detect valid encoding for LDIF file"
                )

            except Exception as e:
                return FlextResult[str].fail(f"Error detecting LDIF encoding: {e}")

    class _SingerLdifConfigHelper:
        """Helper for Singer tap configuration generation for LDIF processing."""

        @staticmethod
        def generate_ldif_singer_catalog(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Generate Singer catalog for LDIF tap with proper schema definitions."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            if not isinstance(config, dict):
                return FlextResult[dict].fail("Configuration must be a dictionary")

            # Analyze sample LDIF files for schema discovery
            schema_analysis = (
                FlextTapLdifUtilities._SingerLdifConfigHelper._analyze_ldif_schema(
                    file_paths[:3], config
                )
            )
            if schema_analysis.is_failure:
                return FlextResult[dict].fail(
                    f"Schema analysis failed: {schema_analysis.error}"
                )

            schema_info = schema_analysis.unwrap()

            # Generate Singer catalog stream
            catalog_stream = {
                "tap_stream_id": "ldif_entries",
                "stream": "ldif_entries",
                "schema": {
                    "type": "object",
                    "properties": {
                        "dn": {
                            "type": "string",
                            "description": "Distinguished Name (primary key)",
                        },
                        "objectClass": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "LDAP object classes",
                        },
                        "_ldif_file_path": {
                            "type": "string",
                            "description": "Source LDIF file path",
                        },
                        "_ldif_processing_timestamp": {
                            "type": "string",
                            "format": "date-time",
                            "description": "Processing timestamp",
                        },
                    },
                    "required": ["dn"],
                    "additionalProperties": True,
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "replication-method": "FULL_TABLE",
                            "inclusion": "available",
                            "selected": True,
                            "forced-replication-method": "FULL_TABLE",
                        },
                    }
                ],
            }

            # Add discovered attributes to schema
            for attr_name, attr_info in schema_info.get(
                "discovered_attributes", {}
            ).items():
                if attr_name not in catalog_stream["schema"]["properties"]:
                    catalog_stream["schema"]["properties"][attr_name] = {
                        "type": attr_info.get("type", "string"),
                        "description": f"LDIF attribute: {attr_name}",
                    }

            catalog = {"version": 1, "streams": [catalog_stream]}

            return FlextResult[dict].ok(catalog)

        @staticmethod
        def _analyze_ldif_schema(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Analyze LDIF files to discover schema information."""
            discovered_attributes = {}
            total_entries = 0
            object_classes = set()

            for file_path in file_paths:
                try:
                    # Detect encoding
                    encoding_result = (
                        FlextTapLdifUtilities._LdifFileHelper.detect_ldif_encoding(
                            file_path
                        )
                    )
                    encoding = (
                        encoding_result.unwrap()
                        if encoding_result.is_success
                        else "utf-8"
                    )

                    entries_analyzed = 0
                    with pathlib.Path(file_path).open(
                        encoding=encoding, errors="ignore"
                    ) as f:
                        current_entry = {}
                        current_attr = None

                        for line in f:
                            line = line.rstrip("\n\r")

                            # Skip comments and empty lines
                            if not line or line.startswith("#"):
                                continue

                            # Handle continuation lines
                            if line.startswith(" ") and current_attr:
                                current_entry[current_attr] = (
                                    current_entry.get(current_attr, "") + line[1:]
                                )
                                continue

                            # Parse attribute lines
                            if ":" in line:
                                attr_name, attr_value = line.split(":", 1)
                                attr_name = attr_name.strip()
                                attr_value = attr_value.strip()

                                if attr_name.lower() == "dn":
                                    # Process previous entry if exists
                                    if current_entry:
                                        FlextTapLdifUtilities._SingerLdifConfigHelper._process_entry_for_schema(
                                            current_entry,
                                            discovered_attributes,
                                            object_classes,
                                        )
                                        total_entries += 1

                                    # Start new entry
                                    current_entry = {"dn": attr_value}
                                    current_attr = "dn"
                                else:
                                    # Add attribute to current entry
                                    if attr_name in current_entry:
                                        # Convert to list if multiple values
                                        if not isinstance(
                                            current_entry[attr_name], list
                                        ):
                                            current_entry[attr_name] = [
                                                current_entry[attr_name]
                                            ]
                                        current_entry[attr_name].append(attr_value)
                                    else:
                                        current_entry[attr_name] = attr_value
                                    current_attr = attr_name

                            entries_analyzed += 1
                            # Limit analysis to avoid performance issues
                            if entries_analyzed > 1000:
                                break

                        # Process last entry
                        if current_entry:
                            FlextTapLdifUtilities._SingerLdifConfigHelper._process_entry_for_schema(
                                current_entry, discovered_attributes, object_classes
                            )
                            total_entries += 1

                except Exception:
                    continue  # Skip problematic files

            schema_info = {
                "discovered_attributes": discovered_attributes,
                "object_classes": list(object_classes),
                "total_entries_analyzed": total_entries,
                "files_analyzed": len(file_paths),
            }

            return FlextResult[dict].ok(schema_info)

        @staticmethod
        def _process_entry_for_schema(
            entry: dict, discovered_attributes: dict, object_classes: set
        ) -> None:
            """Process an LDIF entry to extract schema information."""
            for attr_name, attr_value in entry.items():
                if attr_name.lower() == "objectclass":
                    # Handle objectClass specially
                    if isinstance(attr_value, list):
                        object_classes.update(attr_value)
                    else:
                        object_classes.add(attr_value)

                # Track attribute types
                if attr_name not in discovered_attributes:
                    discovered_attributes[attr_name] = {
                        "type": "array" if isinstance(attr_value, list) else "string",
                        "count": 1,
                    }
                else:
                    discovered_attributes[attr_name]["count"] += 1

        @staticmethod
        def validate_ldif_tap_config(tap_config: dict) -> FlextResult[dict]:
            """Validate Singer tap configuration for LDIF processing."""
            if not isinstance(tap_config, dict):
                return FlextResult[dict].fail("LDIF tap config must be a dictionary")

            # Validate file path configuration (one of these must be specified)
            file_path = tap_config.get("file_path")
            directory_path = tap_config.get("directory_path")
            file_pattern = tap_config.get("file_pattern")

            file_config_count = sum(
                1 for path in [file_path, directory_path, file_pattern] if path
            )
            if file_config_count == 0:
                return FlextResult[dict].fail(
                    "Must specify one of: file_path, directory_path+file_pattern, or file_pattern"
                )

            # Validate file paths exist
            if file_path:
                validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if validation.is_failure:
                    return FlextResult[dict].fail(
                        f"File validation failed: {validation.error}"
                    )

            if directory_path:
                from pathlib import Path

                dir_path = Path(directory_path)
                if not dir_path.exists() or not dir_path.is_dir():
                    return FlextResult[dict].fail(
                        f"Directory does not exist: {directory_path}"
                    )

            # Validate processing configuration
            batch_size = tap_config.get("batch_size", 1000)
            if not isinstance(batch_size, int) or batch_size < 1 or batch_size > 10000:
                return FlextResult[dict].fail(
                    "batch_size must be an integer between 1 and 10000"
                )

            max_file_size_mb = tap_config.get("max_file_size_mb", 100)
            if (
                not isinstance(max_file_size_mb, int)
                or max_file_size_mb < 1
                or max_file_size_mb > 1000
            ):
                return FlextResult[dict].fail(
                    "max_file_size_mb must be an integer between 1 and 1000"
                )

            # Validate encoding
            encoding = tap_config.get("encoding", "utf-8")
            if not isinstance(encoding, str):
                return FlextResult[dict].fail("encoding must be a string")

            return FlextResult[dict].ok(tap_config)

    class _LdifProcessingHelper:
        """Helper for LDIF processing optimization and error handling."""

        @staticmethod
        def estimate_processing_performance(
            file_paths: list[str], config: dict
        ) -> FlextResult[dict]:
            """Estimate LDIF processing performance and resource requirements."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            total_size_mb = 0
            total_files = len(file_paths)
            file_analysis = []

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    file_info = file_validation.unwrap()
                    total_size_mb += file_info["file_size_mb"]
                    file_analysis.append({
                        "file_path": file_path,
                        "size_mb": file_info["file_size_mb"],
                        "processable": True,
                    })
                else:
                    file_analysis.append({
                        "file_path": file_path,
                        "size_mb": 0,
                        "processable": False,
                        "error": file_validation.error,
                    })

            # Performance estimation
            batch_size = config.get("batch_size", 1000)
            entries_per_mb = 1000  # Rough estimate
            estimated_entries = total_size_mb * entries_per_mb
            estimated_batches = max(1, int(estimated_entries / batch_size))

            # Processing time estimation (entries per second)
            processing_rate = 500  # Conservative estimate
            estimated_processing_seconds = estimated_entries / processing_rate
            estimated_processing_minutes = estimated_processing_seconds / 60

            # Memory estimation
            entry_memory_kb = 2  # Rough estimate per entry
            batch_memory_mb = (batch_size * entry_memory_kb) / 1024
            total_memory_estimate_mb = batch_memory_mb * 1.5  # Safety factor

            performance_estimate = {
                "total_files": total_files,
                "total_size_mb": round(total_size_mb, 2),
                "estimated_entries": int(estimated_entries),
                "estimated_batches": estimated_batches,
                "estimated_processing_seconds": round(estimated_processing_seconds, 1),
                "estimated_processing_minutes": round(estimated_processing_minutes, 1),
                "estimated_memory_mb": round(total_memory_estimate_mb, 1),
                "batch_size": batch_size,
                "processing_rate_eps": processing_rate,
                "file_analysis": file_analysis,
                "performance_warnings": [],
            }

            # Add performance warnings
            if total_size_mb > 500:
                performance_estimate["performance_warnings"].append(
                    f"Large dataset ({total_size_mb:.1f}MB) may require significant processing time"
                )

            if estimated_processing_minutes > 60:
                performance_estimate["performance_warnings"].append(
                    f"Estimated processing time ({estimated_processing_minutes:.1f} minutes) is substantial"
                )

            if total_memory_estimate_mb > 500:
                performance_estimate["performance_warnings"].append(
                    f"Estimated memory usage ({total_memory_estimate_mb:.1f}MB) is high"
                )

            return FlextResult[dict].ok(performance_estimate)

        @staticmethod
        def optimize_batch_size_for_files(
            file_paths: list[str], target_memory_mb: int = 50
        ) -> FlextResult[dict]:
            """Optimize batch size based on file characteristics and memory constraints."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            if (
                not isinstance(target_memory_mb, int)
                or target_memory_mb < 10
                or target_memory_mb > 1000
            ):
                return FlextResult[dict].fail(
                    "target_memory_mb must be between 10 and 1000"
                )

            total_size_mb = 0
            largest_file_mb = 0

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    file_info = file_validation.unwrap()
                    file_size = file_info["file_size_mb"]
                    total_size_mb += file_size
                    largest_file_mb = max(largest_file_mb, file_size)

            # Calculate optimal batch size
            # Assumption: 1MB of LDIF ≈ 1000 entries, 2KB memory per entry
            entries_per_mb = 1000
            memory_per_entry_kb = 2

            # Target memory in KB
            target_memory_kb = target_memory_mb * 1024

            # Calculate batch size to stay within memory target
            optimal_batch_size = int(target_memory_kb / memory_per_entry_kb)

            # Apply constraints
            min_batch_size = 100
            max_batch_size = 10000

            optimal_batch_size = max(
                min_batch_size, min(max_batch_size, optimal_batch_size)
            )

            # Performance analysis
            total_entries_estimate = total_size_mb * entries_per_mb
            total_batches = max(1, int(total_entries_estimate / optimal_batch_size))
            actual_memory_mb = (optimal_batch_size * memory_per_entry_kb) / 1024

            optimization_result = {
                "optimal_batch_size": optimal_batch_size,
                "target_memory_mb": target_memory_mb,
                "actual_memory_mb": round(actual_memory_mb, 1),
                "total_files": len(file_paths),
                "total_size_mb": round(total_size_mb, 2),
                "largest_file_mb": round(largest_file_mb, 2),
                "estimated_total_entries": int(total_entries_estimate),
                "estimated_total_batches": total_batches,
                "optimization_factors": {
                    "memory_constraint": f"{target_memory_mb}MB memory limit",
                    "file_size_influence": f"Largest file: {largest_file_mb:.1f}MB",
                    "batch_size_range": f"{min_batch_size}-{max_batch_size}",
                },
            }

            return FlextResult[dict].ok(optimization_result)

        @staticmethod
        def generate_error_recovery_config(file_paths: list[str]) -> FlextResult[dict]:
            """Generate error recovery configuration based on file analysis."""
            if not isinstance(file_paths, list) or not file_paths:
                return FlextResult[dict].fail("File paths must be a non-empty list")

            problematic_files = []
            total_files = len(file_paths)
            accessible_files = 0

            for file_path in file_paths:
                file_validation = FlextTapLdifUtilities._LdifFileHelper.validate_ldif_file_accessibility(
                    file_path
                )
                if file_validation.is_success:
                    accessible_files += 1
                else:
                    problematic_files.append({
                        "file_path": file_path,
                        "error": file_validation.error,
                    })

            # Determine recovery strategy
            if len(problematic_files) == 0:
                recovery_strategy = "strict"
                recommended_config = {
                    "strict_parsing": True,
                    "fail_on_first_error": True,
                    "max_errors_per_file": 0,
                }
            elif (
                len(problematic_files) / total_files < 0.1
            ):  # Less than 10% problematic
                recovery_strategy = "lenient"
                recommended_config = {
                    "strict_parsing": False,
                    "fail_on_first_error": False,
                    "max_errors_per_file": 10,
                    "skip_malformed_entries": True,
                }
            else:  # Many problematic files
                recovery_strategy = "diagnostic"
                recommended_config = {
                    "strict_parsing": False,
                    "fail_on_first_error": False,
                    "max_errors_per_file": 100,
                    "skip_malformed_entries": True,
                    "detailed_error_logging": True,
                }

            recovery_config = {
                "recovery_strategy": recovery_strategy,
                "total_files": total_files,
                "accessible_files": accessible_files,
                "problematic_files_count": len(problematic_files),
                "problematic_files": problematic_files,
                "recommended_config": recommended_config,
                "error_analysis": {
                    "file_access_issues": len(problematic_files),
                    "recovery_approach": recovery_strategy,
                    "risk_level": "low"
                    if len(problematic_files) == 0
                    else "medium"
                    if len(problematic_files) / total_files < 0.1
                    else "high",
                },
            }

            return FlextResult[dict].ok(recovery_config)


# Public API exports following FLEXT standardized patterns
__all__ = [
    "FlextTapLdifModels",  # Unified models class
    "FlextTapLdifUtilities",  # Standardized [Project]Utilities pattern
]
