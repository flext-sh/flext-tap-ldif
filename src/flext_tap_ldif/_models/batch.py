"""Batch processing and state tracking models for LDIF tap."""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)
from datetime import UTC, datetime
from typing import Annotated, ClassVar, Self

from flext_core import FlextConstants

from flext_tap_ldif import m, t, u


class FlextTapLdifModelsBatch:
    """MRO mixin: LdifBatch and LdifProcessingState models."""

    class LdifBatch(m.BaseModel):
        """LDIF batch processing configuration and state."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
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
                    },
                ],
            },
        )

        batch_id: Annotated[str, u.Field(..., description="Unique batch identifier")]
        file_paths: Annotated[
            t.StrSequence,
            u.Field(..., description="List of LDIF files to process"),
        ]
        batch_size: Annotated[
            int,
            u.Field(
                description="Processing batch size",
            ),
        ] = FlextConstants.DEFAULT_SIZE

        # Processing configuration
        parallel_processing: Annotated[
            bool,
            u.Field(
                description="Enable parallel processing",
            ),
        ] = False
        max_workers: Annotated[
            t.WorkerCount, u.Field(description="Maximum worker threads")
        ] = 4
        error_threshold: Annotated[
            t.PositiveInt,
            u.Field(
                description="Maximum errors before stopping",
            ),
        ] = FlextConstants.DEFAULT_SIZE // 10

        # Batch state
        status: Annotated[str, u.Field(description="Batch processing status")] = (
            "pending"
        )
        started_at: Annotated[
            datetime | None,
            u.Field(
                description="Batch start time",
            ),
        ] = None
        completed_at: Annotated[
            datetime | None,
            u.Field(
                description="Batch completion time",
            ),
        ] = None

        # Processing metrics
        files_processed: Annotated[
            t.NonNegativeInt, u.Field(description="Number of files processed")
        ] = 0
        entries_processed: Annotated[
            t.NonNegativeInt, u.Field(description="Total entries processed")
        ] = 0
        errors_encountered: Annotated[
            t.NonNegativeInt,
            u.Field(
                description="Total errors encountered",
            ),
        ] = 0

        # Error tracking
        file_errors: Annotated[
            Mapping[str, t.StrSequence],
            u.Field(
                description="Errors by file",
            ),
        ] = u.Field(default_factory=dict)

        @u.computed_field()
        @property
        def batch_processing_summary(self) -> t.JsonMapping:
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

        @u.model_validator(mode="after")
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

    class LdifProcessingState(m.BaseModel):
        """LDIF processing state and progress tracking."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF processing state with complete tracking",
                "examples": [
                    {
                        "file_path": "/data/users.ldif",
                        "entries_processed": 5000,
                        "processing_status": "in_progress",
                    },
                ],
            },
        )

        file_path: Annotated[str, u.Field(..., description="LDIF file being processed")]
        processing_status: Annotated[
            str,
            u.Field(
                description="Processing status",
            ),
        ] = "pending"

        # Progress tracking
        current_line: Annotated[
            t.NonNegativeInt, u.Field(description="Current line being processed")
        ] = 0
        entries_processed: Annotated[
            t.NonNegativeInt, u.Field(description="Entries processed")
        ] = 0
        change_records_processed: Annotated[
            t.NonNegativeInt,
            u.Field(
                description="Change records processed",
            ),
        ] = 0

        # Timing information
        started_at: Annotated[
            datetime | None,
            u.Field(
                description="Processing start time",
            ),
        ] = None
        last_update: Annotated[
            datetime,
            u.Field(
                description="Last state update",
            ),
        ] = u.Field(default_factory=lambda: datetime.now(UTC))
        estimated_completion: Annotated[
            datetime | None,
            u.Field(
                description="Estimated completion time",
            ),
        ] = None

        # Error tracking
        processing_errors: Annotated[
            Sequence[t.StrMapping],
            u.Field(
                description="Processing errors with context",
            ),
        ] = u.Field(default_factory=lambda: list[t.StrMapping]())
        recoverable_errors: Annotated[
            t.NonNegativeInt,
            u.Field(
                description="Recoverable error count",
            ),
        ] = 0
        fatal_errors: Annotated[
            t.NonNegativeInt, u.Field(description="Fatal error count")
        ] = 0

        # Performance metrics
        processing_rate: Annotated[
            t.NonNegativeFloat, u.Field(description="Entries per second")
        ] = 0.0
        memory_usage: Annotated[
            t.NonNegativeInt, u.Field(description="Memory usage in bytes")
        ] = 0

        @u.computed_field()
        @property
        def processing_progress_summary(self) -> t.JsonMapping:
            """LDIF processing progress summary."""
            total_errors = self.recoverable_errors + self.fatal_errors
            duration = 0.0
            if self.started_at:
                duration = (datetime.now(UTC) - self.started_at).total_seconds()

            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                u.Cli.normalize_json_value({
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
                })
            )

        @u.model_validator(mode="after")
        def validate_processing_state(self) -> Self:
            """Validate LDIF processing state."""
            if not self.file_path:
                msg = "File path is required"
                raise ValueError(msg)
            if self.current_line < 0:
                msg = "Current line cannot be negative"
                raise ValueError(msg)
            return self
