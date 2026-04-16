"""File and stream models for LDIF tap."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
from typing import Annotated, ClassVar, Self

from pydantic import (
    ConfigDict,
    model_validator,
)

from flext_core import FlextConstants
from flext_tap_ldif import m, t, u


class FlextTapLdifModelsFile:
    """MRO mixin: LdifFile and LdifStream models."""

    class LdifFile(m.BaseModel):
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

        file_path: Annotated[str, m.Field(..., description="Path to LDIF file")]
        file_size: Annotated[
            t.NonNegativeInt, m.Field(description="File size in bytes")
        ] = 0
        encoding: Annotated[str, m.Field(description="File encoding")] = "utf-8"

        # File metadata
        created_at: Annotated[
            datetime | None,
            m.Field(
                description="File creation time",
            ),
        ] = None
        modified_at: Annotated[
            datetime | None,
            m.Field(
                description="File modification time",
            ),
        ] = None

        # Processing statistics
        total_lines: Annotated[
            t.NonNegativeInt, m.Field(description="Total lines in file")
        ] = 0
        entry_count: Annotated[
            t.NonNegativeInt, m.Field(description="Number of entries")
        ] = 0
        change_record_count: Annotated[
            t.NonNegativeInt,
            m.Field(
                description="Number of change records",
            ),
        ] = 0
        comment_lines: Annotated[
            t.NonNegativeInt, m.Field(description="Number of comment lines")
        ] = 0

        # Processing state
        processing_status: Annotated[
            str,
            m.Field(
                description="Processing status",
            ),
        ] = "pending"
        last_processed_line: Annotated[
            t.NonNegativeInt,
            m.Field(
                description="Last processed line number",
            ),
        ] = 0
        processing_errors: Annotated[
            t.StrSequence,
            m.Field(
                description="Processing errors",
            ),
        ] = m.Field(default_factory=list)

        # Validation results
        is_valid_ldif: Annotated[bool, m.Field(description="LDIF format validity")] = (
            True
        )
        validation_errors: Annotated[
            t.StrSequence,
            m.Field(
                description="Format validation errors",
            ),
        ] = m.Field(default_factory=list)

        @u.computed_field()
        @property
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

    class LdifStream(m.BaseModel):
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

        stream_name: Annotated[str, m.Field(..., description="Singer stream name")]
        file_path: Annotated[str, m.Field(..., description="LDIF file path")]

        # Singer stream configuration
        tap_stream_id: Annotated[str, m.Field(..., description="Singer tap stream ID")]
        replication_method: Annotated[
            str,
            m.Field(
                description="Replication method",
            ),
        ] = "FULL_TABLE"
        key_properties: Annotated[
            t.StrSequence,
            m.Field(
                description="Key properties",
            ),
        ] = m.Field(default_factory=lambda: ["dn"])

        # LDIF-specific settings
        include_change_records: Annotated[
            bool,
            m.Field(
                description="Include LDIF change records",
            ),
        ] = True
        filter_object_classes: Annotated[
            t.StrSequence,
            m.Field(
                description="Filter by object classes",
            ),
        ] = m.Field(default_factory=list)
        batch_size: Annotated[
            int,
            m.Field(
                description="Processing batch size",
            ),
        ] = FlextConstants.DEFAULT_SIZE

        # Stream schema
        stream_schema: Annotated[
            t.ContainerValueMapping,
            m.Field(
                description="JSON schema",
            ),
        ] = m.Field(default_factory=dict)
        stream_metadata: Annotated[
            Sequence[t.StrMapping],
            m.Field(
                description="Stream metadata",
            ),
        ] = m.Field(default_factory=lambda: list[t.StrMapping]())

        @u.computed_field()
        @property
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
