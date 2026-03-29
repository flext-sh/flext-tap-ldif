"""Entry and change record models for LDIF tap."""

from __future__ import annotations

from collections.abc import MutableMapping
from datetime import UTC, datetime
from typing import Annotated, ClassVar, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
    model_validator,
)

from flext_tap_ldif import t


class FlextTapLdifModelsEntry:
    """MRO mixin: LdifEntry and LdifChangeRecord models."""

    class LdifEntry(BaseModel):
        """Represents an LDIF entry with complete parsing support."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
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

        dn: Annotated[str, Field(..., description="Distinguished Name")]
        attributes: Annotated[
            MutableMapping[str, t.StrSequence],
            Field(
                description="Entry attributes",
            ),
        ] = Field(default_factory=dict)
        object_classes: Annotated[
            t.StrSequence,
            Field(
                description="Object classes",
            ),
        ] = Field(default_factory=list)

        # LDIF metadata
        line_number: Annotated[
            t.NonNegativeInt,
            Field(
                default=0,
                description="Source line number in LDIF file",
            ),
        ]
        source_file: Annotated[
            str | None,
            Field(
                default=None,
                description="Source LDIF file path",
            ),
        ]
        entry_type: Annotated[
            str,
            Field(default="entry", description="Type of LDIF entry"),
        ]

        # Processing metadata
        extracted_at: Annotated[
            datetime,
            Field(
                description="Extraction timestamp",
            ),
        ] = Field(default_factory=lambda: datetime.now(UTC))
        processed: Annotated[
            bool,
            Field(default=False, description="Processing status"),
        ]
        validation_errors: Annotated[
            t.StrSequence,
            Field(
                description="Validation errors",
            ),
        ] = Field(default_factory=list)

        @computed_field
        def ldif_entry_summary(self) -> t.ContainerMapping:
            """LDIF entry analysis summary."""
            return {
                "dn": self.dn,
                "attribute_count": len(self.attributes),
                "object_class_count": len(self.object_classes),
                "primary_object_class": self.object_classes[0]
                if self.object_classes
                else None,
                "entry_type": self.entry_type,
                "is_valid": not self.validation_errors,
                "source_location": {
                    "file": self.source_file,
                    "line": self.line_number,
                },
            }

        def get_attribute_values(self, name: str) -> t.StrSequence:
            """Get attribute values by name (case-insensitive)."""
            normalized_name = name.lower()
            for attr_name, values in self.attributes.items():
                if attr_name.lower() == normalized_name:
                    return values
            return []

        def get_first_attribute_value(self, name: str) -> str | None:
            """Get first attribute value by name."""
            values = self.get_attribute_values(name)
            return values[0] if values else None

        @model_validator(mode="after")
        def validate_ldif_entry(self) -> Self:
            """Validate LDIF entry structure."""
            if not self.dn:
                msg = "DN cannot be empty"
                raise ValueError(msg)

            # Validate object classes are in attributes
            if self.object_classes and "objectClass" not in self.attributes:
                self.attributes["objectClass"] = self.object_classes

            return self

    class LdifChangeRecord(BaseModel):
        """Represents an LDIF change record for modify operations."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
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

        dn: Annotated[str, Field(..., description="Distinguished Name")]
        change_type: Annotated[
            str,
            Field(
                ...,
                description="Type of change (add, modify, delete, modrdn)",
            ),
        ]
        changes: Annotated[
            list[t.StrMapping],
            Field(
                description="List of changes",
            ),
        ] = Field(default_factory=lambda: list[t.StrMapping]())

        # Change metadata
        changetype: Annotated[
            str | None,
            Field(
                default=None,
                description="LDIF changetype directive",
            ),
        ]
        line_number: Annotated[
            t.NonNegativeInt,
            Field(default=0, description="Source line number"),
        ]
        source_file: Annotated[
            str | None,
            Field(default=None, description="Source LDIF file"),
        ]

        # Processing metadata
        extracted_at: Annotated[
            datetime,
            Field(
                description="Extraction timestamp",
            ),
        ] = Field(default_factory=lambda: datetime.now(UTC))
        applied: Annotated[
            bool,
            Field(default=False, description="Change application status"),
        ]
        application_errors: Annotated[
            t.StrSequence,
            Field(
                description="Application errors",
            ),
        ] = Field(default_factory=list)

        @computed_field
        def change_record_summary(self) -> t.ContainerMapping:
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

        @model_validator(mode="after")
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
