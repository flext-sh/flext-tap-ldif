"""File and stream models for LDIF tap."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
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


class FlextTapLdifModelsFile:
    """MRO mixin: LdifFile and LdifStream models."""

    class LdifFile(BaseModel):
        """Represents an LDIF file with processing metadata."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF file with complete processing support",
                "examples": [
                    {
                        "file_path": "/data/directory-export.ldif",
                        "file_size": 1048576,
                        "encoding": "utf-8",
                    },
                ],
            },
        )

        file_path: Annotated[str, Field(..., description="Path to LDIF file")]
        file_size: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="File size in bytes"),
        ]
        encoding: Annotated[str, Field(default="utf-8", description="File encoding")]

        # File metadata
        created_at: Annotated[
            datetime | None,
            Field(
                default=None,
                description="File creation time",
            ),
        ]
        modified_at: Annotated[
            datetime | None,
            Field(
                default=None,
                description="File modification time",
            ),
        ]

        # Processing statistics
        total_lines: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Total lines in file"),
        ]
        entry_count: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Number of entries"),
        ]
        change_record_count: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Number of change records",
            ),
        ]
        comment_lines: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Number of comment lines"),
        ]

        # Processing state
        processing_status: Annotated[
            str,
            Field(
                default="pending",
                description="Processing status",
            ),
        ]
        last_processed_line: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Last processed line number",
            ),
        ]
        processing_errors: Annotated[
            t.StrSequence,
            Field(
                description="Processing errors",
            ),
        ] = Field(default_factory=list)

        # Validation results
        is_valid_ldif: Annotated[
            bool,
            Field(default=True, description="LDIF format validity"),
        ]
        validation_errors: Annotated[
            t.StrSequence,
            Field(
                description="Format validation errors",
            ),
        ] = Field(default_factory=list)

        @computed_field
        def ldif_file_summary(self) -> t.RecursiveContainerMapping:
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
                    "valid": self.is_valid_ldif,
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

    class LdifStream(BaseModel):
        """Singer stream configuration for LDIF file processing."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
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
                    },
                ],
            },
        )

        stream_name: Annotated[str, Field(..., description="Singer stream name")]
        file_path: Annotated[str, Field(..., description="LDIF file path")]

        # Singer stream configuration
        tap_stream_id: Annotated[str, Field(..., description="Singer tap stream ID")]
        replication_method: Annotated[
            str,
            Field(
                default="FULL_TABLE",
                description="Replication method",
            ),
        ]
        key_properties: Annotated[
            t.StrSequence,
            Field(
                description="Key properties",
            ),
        ] = Field(default_factory=lambda: ["dn"])

        # LDIF-specific settings
        include_change_records: Annotated[
            bool,
            Field(
                default=True,
                description="Include LDIF change records",
            ),
        ]
        filter_object_classes: Annotated[
            t.StrSequence,
            Field(
                description="Filter by object classes",
            ),
        ] = Field(default_factory=list)
        batch_size: Annotated[
            int,
            Field(
                default=FlextConstants.DEFAULT_SIZE,
                description="Processing batch size",
            ),
        ]

        # Stream schema
        stream_schema: Annotated[
            t.ContainerValueMapping,
            Field(
                description="JSON schema",
            ),
        ] = Field(default_factory=dict)
        stream_metadata: Annotated[
            Sequence[t.StrMapping],
            Field(
                description="Stream metadata",
            ),
        ] = Field(default_factory=lambda: list[t.StrMapping]())

        @computed_field
        def ldif_stream_summary(self) -> t.RecursiveContainerMapping:
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
                "has_schema": bool(self.stream_schema),
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
