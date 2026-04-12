"""Record, validation, and performance models for LDIF tap."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import UTC, datetime
from typing import Annotated, Self

from pydantic import (
    BaseModel,
    Field,
    computed_field,
    model_validator,
)

from flext_tap_ldif import t


class FlextTapLdifModelsRecord:
    """MRO mixin: LdifRecord, LdifValidationResult, LdifPerformanceMetrics."""

    class LdifRecord(BaseModel):
        """Individual LDIF record for Singer output."""

        stream: Annotated[str, Field(..., description="Source stream name")]
        record: Annotated[
            t.ContainerValueMapping,
            Field(
                ...,
                description="LDIF record data",
            ),
        ]
        record_type: Annotated[
            str,
            Field(default="entry", description="Type of LDIF record"),
        ]

        # Source metadata
        source_file: Annotated[
            str | None,
            Field(default=None, description="Source LDIF file"),
        ]
        line_number: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Source line number"),
        ]

        # Extraction metadata
        time_extracted: Annotated[
            datetime,
            Field(
                description="Extraction timestamp",
            ),
        ] = Field(default_factory=lambda: datetime.now(UTC))
        processing_time: Annotated[
            t.NonNegativeFloat,
            Field(
                default=0.0,
                description="Processing time in seconds",
            ),
        ]

        @computed_field
        def ldif_record_summary(self) -> t.RecursiveContainerMapping:
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

    class LdifValidationResult(BaseModel):
        """LDIF validation result with detailed error reporting."""

        file_path: Annotated[str, Field(..., description="Validated LDIF file path")]
        valid: Annotated[bool, Field(..., description="Overall validation result")]

        # Validation results
        validation_errors: Annotated[
            Sequence[t.StrMapping],
            Field(
                description="Validation errors with details",
            ),
        ] = Field(default_factory=lambda: list[t.StrMapping]())
        warnings: Annotated[
            Sequence[t.StrMapping],
            Field(
                description="Validation warnings",
            ),
        ] = Field(default_factory=lambda: list[t.StrMapping]())

        # Statistics
        total_entries: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Total entries validated"),
        ]
        valid_entries: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Valid entries count"),
        ]
        invalid_entries: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Invalid entries count"),
        ]

        # Validation metadata
        validation_time: Annotated[
            t.NonNegativeFloat,
            Field(
                default=0.0,
                description="Validation time in seconds",
            ),
        ]
        validator_version: Annotated[
            str,
            Field(default="1.0", description="Validator version"),
        ]

        @computed_field
        def validation_summary(self) -> t.RecursiveContainerMapping:
            """LDIF validation complete summary."""
            success_rate = 0.0
            if self.total_entries > 0:
                success_rate = self.valid_entries / self.total_entries

            return {
                "file_path": self.file_path,
                "validation_result": "valid" if self.valid else "invalid",
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
            if self.valid and self.validation_errors:
                msg = "Cannot be valid with validation errors"
                raise ValueError(msg)
            return self

    class LdifPerformanceMetrics(BaseModel):
        """Performance metrics for LDIF tap operations."""

        # File processing metrics
        files_processed: Annotated[
            int,
            Field(default=0, description="Number of files processed"),
        ]
        total_file_size: Annotated[
            int,
            Field(default=0, description="Total file size in bytes"),
        ]
        average_file_size: Annotated[
            float,
            Field(default=0.0, description="Average file size"),
        ]

        # Entry processing metrics
        total_entries: Annotated[
            int,
            Field(default=0, description="Total entries processed"),
        ]
        entries_per_file: Annotated[
            float,
            Field(
                default=0.0,
                description="Average entries per file",
            ),
        ]
        processing_rate: Annotated[
            float,
            Field(default=0.0, description="Entries per second"),
        ]

        # Time metrics
        total_processing_time: Annotated[
            float,
            Field(
                default=0.0,
                description="Total processing time",
            ),
        ]
        average_processing_time: Annotated[
            float,
            Field(
                default=0.0,
                description="Average time per file",
            ),
        ]
        parsing_time: Annotated[
            float,
            Field(default=0.0, description="Time spent parsing"),
        ]
        validation_time: Annotated[
            float,
            Field(default=0.0, description="Time spent validating"),
        ]

        # Quality metrics
        successful_files: Annotated[
            int,
            Field(
                default=0,
                description="Successfully processed files",
            ),
        ]
        failed_files: Annotated[
            int,
            Field(default=0, description="Failed file processing"),
        ]
        total_errors: Annotated[
            int,
            Field(default=0, description="Total processing errors"),
        ]

        # Resource metrics
        peak_memory_usage: Annotated[
            int,
            Field(
                default=0,
                description="Peak memory usage in bytes",
            ),
        ]
        average_memory_usage: Annotated[
            int,
            Field(default=0, description="Average memory usage"),
        ]

        @computed_field
        def performance_analysis_summary(self) -> t.RecursiveContainerMapping:
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
