"""Record, validation, and performance models for LDIF tap."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from typing import Annotated, Self

from flext_tap_ldif import m, t, u


class FlextTapLdifModelsRecord:
    """MRO mixin: LdifRecord, LdifValidationResult, LdifPerformanceMetrics."""

    class LdifRecord(m.BaseModel):
        """Individual LDIF record for Singer output."""

        stream: Annotated[str, u.Field(..., description="Source stream name")]
        record: Annotated[
            t.ContainerValueMapping,
            u.Field(
                ...,
                description="LDIF record data",
            ),
        ]
        record_type: Annotated[str, u.Field(description="Type of LDIF record")] = (
            "entry"
        )

        # Source metadata
        source_file: Annotated[str | None, u.Field(description="Source LDIF file")] = (
            None
        )
        line_number: Annotated[
            t.NonNegativeInt, u.Field(description="Source line number")
        ] = 0

        # Extraction metadata
        time_extracted: Annotated[
            datetime,
            u.Field(
                description="Extraction timestamp",
            ),
        ] = u.Field(default_factory=lambda: datetime.now(UTC))
        processing_time: Annotated[
            t.NonNegativeFloat,
            u.Field(
                description="Processing time in seconds",
            ),
        ] = 0.0

        @u.computed_field()
        @property
        def ldif_record_summary(self) -> Mapping[str, t.Container]:
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

        @u.model_validator(mode="after")
        def validate_ldif_record(self) -> Self:
            """Validate LDIF record structure."""
            if not self.stream:
                msg = "Stream name is required"
                raise ValueError(msg)
            if not self.record:
                msg = "Record data cannot be empty"
                raise ValueError(msg)
            return self

    class LdifValidationResult(m.BaseModel):
        """LDIF validation result with detailed error reporting."""

        file_path: Annotated[str, u.Field(..., description="Validated LDIF file path")]
        valid: Annotated[bool, u.Field(..., description="Overall validation result")]

        # Validation results
        validation_errors: Annotated[
            Sequence[t.StrMapping],
            u.Field(
                description="Validation errors with details",
            ),
        ] = u.Field(default_factory=lambda: list[t.StrMapping]())
        warnings: Annotated[
            Sequence[t.StrMapping],
            u.Field(
                description="Validation warnings",
            ),
        ] = u.Field(default_factory=lambda: list[t.StrMapping]())

        # Statistics
        total_entries: Annotated[
            t.NonNegativeInt, u.Field(description="Total entries validated")
        ] = 0
        valid_entries: Annotated[
            t.NonNegativeInt, u.Field(description="Valid entries count")
        ] = 0
        invalid_entries: Annotated[
            t.NonNegativeInt, u.Field(description="Invalid entries count")
        ] = 0

        # Validation metadata
        validation_time: Annotated[
            t.NonNegativeFloat,
            u.Field(
                description="Validation time in seconds",
            ),
        ] = 0.0
        validator_version: Annotated[str, u.Field(description="Validator version")] = (
            "1.0"
        )

        @u.computed_field()
        @property
        def validation_summary(self) -> Mapping[str, t.Container]:
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

        @u.model_validator(mode="after")
        def validate_result_consistency(self) -> Self:
            """Validate result consistency."""
            if self.valid_entries + self.invalid_entries != self.total_entries:
                msg = "Valid + invalid entries must equal total entries"
                raise ValueError(msg)
            if self.valid and self.validation_errors:
                msg = "Cannot be valid with validation errors"
                raise ValueError(msg)
            return self

    class LdifPerformanceMetrics(m.BaseModel):
        """Performance metrics for LDIF tap operations."""

        # File processing metrics
        files_processed: Annotated[
            int, u.Field(description="Number of files processed")
        ] = 0
        total_file_size: Annotated[
            int, u.Field(description="Total file size in bytes")
        ] = 0
        average_file_size: Annotated[
            float, u.Field(description="Average file size")
        ] = 0.0

        # Entry processing metrics
        total_entries: Annotated[
            int, u.Field(description="Total entries processed")
        ] = 0
        entries_per_file: Annotated[
            float,
            u.Field(
                description="Average entries per file",
            ),
        ] = 0.0
        processing_rate: Annotated[float, u.Field(description="Entries per second")] = (
            0.0
        )

        # Time metrics
        total_processing_time: Annotated[
            float,
            u.Field(
                description="Total processing time",
            ),
        ] = 0.0
        average_processing_time: Annotated[
            float,
            u.Field(
                description="Average time per file",
            ),
        ] = 0.0
        parsing_time: Annotated[float, u.Field(description="Time spent parsing")] = 0.0
        validation_time: Annotated[
            float, u.Field(description="Time spent validating")
        ] = 0.0

        # Quality metrics
        successful_files: Annotated[
            int,
            u.Field(
                description="Successfully processed files",
            ),
        ] = 0
        failed_files: Annotated[int, u.Field(description="Failed file processing")] = 0
        total_errors: Annotated[int, u.Field(description="Total processing errors")] = 0

        # Resource metrics
        peak_memory_usage: Annotated[
            int,
            u.Field(
                description="Peak memory usage in bytes",
            ),
        ] = 0
        average_memory_usage: Annotated[
            int, u.Field(description="Average memory usage")
        ] = 0

        @u.computed_field()
        @property
        def performance_analysis_summary(self) -> Mapping[str, t.Container]:
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

        @u.model_validator(mode="after")
        def validate_performance_metrics(self) -> Self:
            """Validate performance metrics consistency."""
            if self.files_processed < 0:
                msg = "Files processed cannot be negative"
                raise ValueError(msg)
            if self.successful_files + self.failed_files > self.files_processed:
                msg = "Successful + failed files cannot exceed total files"
                raise ValueError(msg)
            return self
