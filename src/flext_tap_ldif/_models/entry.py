"""Entry and change record models for LDIF tap."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_tap_ldif import m, t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapLdifModelsEntry:
    """MRO mixin: LdifEntry and LdifChangeRecord models."""

    class LdifEntry(m.EnforcedModel):
        """Represents an LDIF entry with complete parsing support."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF directory entry with full attribute support",
                "examples": [
                    {
                        "dn": "cn=John Doe,ou=users,dc=example,dc=com",
                        "object_classes": ["inetOrgPerson", "organizationalPerson"],
                    },
                ],
            },
        )

        dn: Annotated[str, u.Field(..., description="Distinguished Name")]
        attributes: Annotated[
            t.MappingKV[str, t.StrSequence],
            u.Field(
                description="Entry attributes",
            ),
        ] = u.Field(default_factory=lambda: MappingProxyType({}))
        object_classes: Annotated[
            t.StrSequence,
            u.Field(
                description="Object classes",
            ),
        ] = u.Field(default_factory=tuple)

        # LDIF metadata
        line_number: Annotated[
            t.NonNegativeInt,
            u.Field(
                description="Source line number in LDIF file",
            ),
        ] = 0
        source_file: Annotated[
            str | None,
            u.Field(
                description="Source LDIF file path",
            ),
        ] = None
        entry_type: Annotated[str, u.Field(description="Type of LDIF entry")] = "entry"

        # Processing metadata
        extracted_at: Annotated[
            datetime,
            u.Field(
                description="Extraction timestamp",
            ),
        ] = u.Field(default_factory=u.now)
        processed: Annotated[bool, u.Field(description="Processing status")] = False
        validation_errors: Annotated[
            t.StrSequence,
            u.Field(
                description="Validation errors",
            ),
        ] = u.Field(default_factory=tuple)

        @u.computed_field()
        @property
        def ldif_entry_summary(self) -> t.JsonMapping:
            """LDIF entry analysis summary."""
            primary_object_class = self.object_classes[0] if self.object_classes else ""
            source_file = self.source_file or ""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                u.normalize_to_json_value({
                    "dn": self.dn,
                    "attribute_count": len(self.attributes),
                    "object_class_count": len(self.object_classes),
                    "primary_object_class": primary_object_class,
                    "entry_type": self.entry_type,
                    "valid": not self.validation_errors,
                    "source_location": {
                        "file": source_file,
                        "line": self.line_number,
                    },
                }),
            )

        def resolve_attribute_values(self, name: str) -> t.StrSequence:
            """Get attribute values by name (case-insensitive)."""
            normalized_name = name.lower()
            for attr_name, values in self.attributes.items():
                if attr_name.lower() == normalized_name:
                    return values
            return ()

        def resolve_first_attribute_value(self, name: str) -> str | None:
            """Get first attribute value by name."""
            values = self.resolve_attribute_values(name)
            return values[0] if values else None

        @u.model_validator(mode="after")
        def validate_ldif_entry(self) -> Self:
            """Validate LDIF entry structure."""
            if not self.dn:
                msg = "DN cannot be empty"
                raise ValueError(msg)

            # Validate object classes are in attributes
            if self.object_classes and "objectClass" not in self.attributes:
                attributes = dict(self.attributes)
                attributes["objectClass"] = self.object_classes
                self.attributes = MappingProxyType(attributes)

            return self
