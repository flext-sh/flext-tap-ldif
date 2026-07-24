"""LDIF Singer stream model for the tap."""

from __future__ import annotations

from types import MappingProxyType
from typing import Annotated, ClassVar, Self

from flext_tap_ldif import c, m, t, u


class FlextTapLdifModelsLdifStream:
    """MRO mixin containing the LdifStream model."""

    class LdifStream(m.EnforcedModel):
        """Singer stream configuration for LDIF file processing."""

        model_config: ClassVar[t.ConfigDict] = m.ConfigDict(
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

        stream_name: Annotated[str, u.Field(..., description="Singer stream name")]
        file_path: Annotated[str, u.Field(..., description="LDIF file path")]

        tap_stream_id: Annotated[str, u.Field(..., description="Singer tap stream ID")]
        replication_method: Annotated[
            str, u.Field(description="Replication method")
        ] = "FULL_TABLE"
        key_properties: Annotated[
            t.StrSequence, u.Field(description="Key properties")
        ] = u.Field(default_factory=lambda: ("dn",))

        include_change_records: Annotated[
            bool, u.Field(description="Include LDIF change records")
        ] = True
        filter_object_classes: Annotated[
            t.StrSequence, u.Field(description="Filter by object classes")
        ] = u.Field(default_factory=tuple)
        batch_size: Annotated[int, u.Field(description="Processing batch size")] = (
            c.DEFAULT_SIZE
        )

        stream_schema: Annotated[t.JsonMapping, u.Field(description="JSON schema")] = (
            u.Field(default_factory=lambda: MappingProxyType({}))
        )
        stream_metadata: Annotated[
            t.SequenceOf[t.StrMapping], u.Field(description="Stream metadata")
        ] = u.Field(default_factory=tuple)

        @u.computed_field()
        @property
        def ldif_stream_summary(self) -> t.JsonMapping:
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

        @u.model_validator(mode="after")
        def validate_ldif_stream(self) -> Self:
            """Validate LDIF stream configuration."""
            if not self.stream_name:
                msg = "Stream name is required"
                raise ValueError(msg)
            if not self.file_path:
                msg = "LDIF file path is required"
                raise ValueError(msg)
            return self
