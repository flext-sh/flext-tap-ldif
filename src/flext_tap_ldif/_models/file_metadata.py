"""LDIF file metadata model for the tap."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, ClassVar, Self

from flext_tap_ldif import c, t, u
from flext_tap_ldif.models import m


class FlextTapLdifModelsLdifFile:
    """MRO mixin containing the LdifFile model."""

    class LdifFile(m.EnforcedModel):
        """Represents an LDIF file with processing metadata."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF file with complete processing support",
                "examples": [
                    {
                        "file_path": "/data/directory-export.ldif",
                        "file_size": 1048576,
                        "encoding": c.DEFAULT_ENCODING,
                    },
                ],
            },
        )

        file_path: Annotated[str, u.Field(..., description="Path to LDIF file")]
        file_size: Annotated[
            t.NonNegativeInt, u.Field(description="File size in bytes")
        ] = 0
        encoding: Annotated[str, u.Field(description="File encoding")] = (
            c.DEFAULT_ENCODING
        )

        created_at: Annotated[
            datetime | None,
            u.Field(description="File creation time"),
        ] = None
        modified_at: Annotated[
            datetime | None,
            u.Field(description="File modification time"),
        ] = None

        total_lines: Annotated[
            t.NonNegativeInt, u.Field(description="Total lines in file")
        ] = 0
        entry_count: Annotated[
            t.NonNegativeInt, u.Field(description="Number of entries")
        ] = 0
        change_record_count: Annotated[
            t.NonNegativeInt,
            u.Field(description="Number of change records"),
        ] = 0
        comment_lines: Annotated[
            t.NonNegativeInt, u.Field(description="Number of comment lines")
        ] = 0

        processing_status: Annotated[
            str,
            u.Field(description="Processing status"),
        ] = "pending"
        last_processed_line: Annotated[
            t.NonNegativeInt,
            u.Field(description="Last processed line number"),
        ] = 0
        processing_errors: Annotated[
            t.StrSequence,
            u.Field(description="Processing errors"),
        ] = u.Field(default_factory=tuple)

        is_valid_ldif: Annotated[bool, u.Field(description="LDIF format validity")] = (
            True
        )
        validation_errors: Annotated[
            t.StrSequence,
            u.Field(description="Format validation errors"),
        ] = u.Field(default_factory=tuple)

        @u.computed_field()
        @property
        def ldif_file_summary(self) -> t.JsonMapping:
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

        @u.model_validator(mode="after")
        def validate_ldif_file(self) -> Self:
            """Validate LDIF file configuration."""
            if not self.file_path:
                msg = "LDIF file path is required"
                raise ValueError(msg)
            if self.file_size < 0:
                msg = "File size cannot be negative"
                raise ValueError(msg)
            return self
