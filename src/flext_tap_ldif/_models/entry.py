"""Entry and change record models for LDIF tap."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping
from datetime import UTC, datetime
from typing import Annotated, ClassVar, Self

from flext_tap_ldif import m, t, u


class FlextTapLdifModelsEntry:
    """MRO mixin: LdifEntry and LdifChangeRecord models."""

    class LdifEntry(m.BaseModel):
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
            MutableMapping[str, t.StrSequence],
            u.Field(
                description="Entry attributes",
            ),
        ] = u.Field(default_factory=dict)
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
        ] = u.Field(default_factory=lambda: datetime.now(UTC))
        processed: Annotated[bool, u.Field(description="Processing status")] = False
        validation_errors: Annotated[
            t.StrSequence,
            u.Field(
                description="Validation errors",
            ),
        ] = u.Field(default_factory=tuple)

        @u.computed_field()
        @property
        def ldif_entry_summary(self) -> Mapping[str, t.Container]:
            """LDIF entry analysis summary."""
            return {
                "dn": self.dn,
                "attribute_count": len(self.attributes),
                "object_class_count": len(self.object_classes),
                "primary_object_class": self.object_classes[0]
                if self.object_classes
                else None,
                "entry_type": self.entry_type,
                "valid": not self.validation_errors,
                "source_location": {
                    "file": self.source_file,
                    "line": self.line_number,
                },
            }

        def resolve_attribute_values(self, name: str) -> t.StrSequence:
            """Get attribute values by name (case-insensitive)."""
            normalized_name = name.lower()
            for attr_name, values in self.attributes.items():
                if attr_name.lower() == normalized_name:
                    return values
            return []

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
                self.attributes["objectClass"] = self.object_classes

            return self

    class LdifChangeRecord(m.BaseModel):
        """Represents an LDIF change record for modify operations."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
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
                    },
                ],
            },
        )

        dn: Annotated[str, u.Field(..., description="Distinguished Name")]
        change_type: Annotated[
            str,
            u.Field(
                ...,
                description="Type of change (add, modify, delete, modrdn)",
            ),
        ]
        changes: Annotated[
            list[t.StrMapping],
            u.Field(
                description="List of changes",
            ),
        ] = u.Field(default_factory=lambda: list[t.StrMapping]())

        # Change metadata
        changetype: Annotated[
            str | None,
            u.Field(
                description="LDIF changetype directive",
            ),
        ] = None
        line_number: Annotated[
            t.NonNegativeInt, u.Field(description="Source line number")
        ] = 0
        source_file: Annotated[str | None, u.Field(description="Source LDIF file")] = (
            None
        )

        # Processing metadata
        extracted_at: Annotated[
            datetime,
            u.Field(
                description="Extraction timestamp",
            ),
        ] = u.Field(default_factory=lambda: datetime.now(UTC))
        applied: Annotated[bool, u.Field(description="Change application status")] = (
            False
        )
        application_errors: Annotated[
            t.StrSequence,
            u.Field(
                description="Application errors",
            ),
        ] = u.Field(default_factory=tuple)

        @u.computed_field()
        @property
        def change_record_summary(self) -> Mapping[str, t.Container]:
            """LDIF change record summary."""
            return {
                "dn": self.dn,
                "change_type": self.change_type,
                "change_count": len(self.changes),
                "has_errors": self.application_errors,
                "applied": self.applied,
                "source_location": {
                    "file": self.source_file,
                    "line": self.line_number,
                },
            }

        @u.model_validator(mode="after")
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
