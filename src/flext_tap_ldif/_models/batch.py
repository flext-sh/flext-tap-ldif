"""Batch processing and state tracking models for LDIF tap."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from typing import Annotated, ClassVar, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
    model_validator,
)

from flext_core import FlextConstants
from flext_tap_ldif import t


class FlextTapLdifModelsBatch:
    """MRO mixin: LdifBatch and LdifProcessingState models."""

    class LdifBatch(BaseModel):
        """LDIF batch processing configuration and state."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
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

        batch_id: Annotated[str, Field(..., description="Unique batch identifier")]
        file_paths: Annotated[
            t.StrSequence,
            Field(..., description="List of LDIF files to process"),
        ]
        batch_size: Annotated[
            int,
            Field(
                default=FlextConstants.DEFAULT_SIZE,
                description="Processing batch size",
            ),
        ]

        # Processing configuration
        parallel_processing: Annotated[
            bool,
            Field(
                default=False,
                description="Enable parallel processing",
            ),
        ]
        max_workers: Annotated[
            t.WorkerCount,
            Field(default=4, description="Maximum worker threads"),
        ]
        error_threshold: Annotated[
            t.PositiveInt,
            Field(
                default=FlextConstants.DEFAULT_SIZE // 10,
                description="Maximum errors before stopping",
            ),
        ]

        # Batch state
        status: Annotated[
            str,
            Field(default="pending", description="Batch processing status"),
        ]
        started_at: Annotated[
            datetime | None,
            Field(
                default=None,
                description="Batch start time",
            ),
        ]
        completed_at: Annotated[
            datetime | None,
            Field(
                default=None,
                description="Batch completion time",
            ),
        ]

        # Processing metrics
        files_processed: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Number of files processed"),
        ]
        entries_processed: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Total entries processed"),
        ]
        errors_encountered: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Total errors encountered",
            ),
        ]

        # Error tracking
        file_errors: Annotated[
            Mapping[str, t.StrSequence],
            Field(
                description="Errors by file",
            ),
        ] = Field(default_factory=dict)

        @computed_field
        def batch_processing_summary(self) -> t.ContainerMapping:
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

    class LdifProcessingState(BaseModel):
        """LDIF processing state and progress tracking."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
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

        file_path: Annotated[str, Field(..., description="LDIF file being processed")]
        processing_status: Annotated[
            str,
            Field(
                default="pending",
                description="Processing status",
            ),
        ]

        # Progress tracking
        current_line: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Current line being processed"),
        ]
        entries_processed: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Entries processed"),
        ]
        change_records_processed: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Change records processed",
            ),
        ]

        # Timing information
        started_at: Annotated[
            datetime | None,
            Field(
                default=None,
                description="Processing start time",
            ),
        ]
        last_update: Annotated[
            datetime,
            Field(
                description="Last state update",
            ),
        ] = Field(default_factory=lambda: datetime.now(UTC))
        estimated_completion: Annotated[
            datetime | None,
            Field(
                default=None,
                description="Estimated completion time",
            ),
        ]

        # Error tracking
        processing_errors: Annotated[
            Sequence[t.StrMapping],
            Field(
                description="Processing errors with context",
            ),
        ] = Field(default_factory=lambda: list[t.StrMapping]())
        recoverable_errors: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Recoverable error count",
            ),
        ]
        fatal_errors: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Fatal error count"),
        ]

        # Performance metrics
        processing_rate: Annotated[
            t.NonNegativeFloat,
            Field(default=0.0, description="Entries per second"),
        ]
        memory_usage: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Memory usage in bytes"),
        ]

        @computed_field
        def processing_progress_summary(self) -> t.ContainerMapping:
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
