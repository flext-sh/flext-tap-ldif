"""FLEXT Tap LDIF - Singer protocol implementation for LDIF file data extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from singer_sdk import Stream, Tap
from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

from flext_core import FlextLogger
from flext_tap_ldif.config import TapLDIFConfig
from flext_tap_ldif.streams import LDIFEntriesStream

logger = FlextLogger(__name__)


class TapLDIF(Tap):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = TapLDIFConfig
    # Schema combining file-based configuration with LDIF-specific properties
    config_jsonschema: ClassVar[dict[str, object]] = PropertiesList(
        # File-based properties
        Property(
            "file_path",
            StringType,
            description="Path to single LDIF file",
        ),
        Property(
            "directory_path",
            StringType,
            description="Directory containing LDIF files",
        ),
        Property(
            "file_pattern",
            StringType,
            default="*.ldif",
            description="File pattern for matching LDIF files in directory",
        ),
        Property(
            "encoding",
            StringType,
            default="utf-8",
            description="Text encoding for LDIF files",
        ),
        # LDIF-specific additional properties
        Property(
            "base_dn_filter",
            StringType,
            description="Filter entries by base DN pattern",
        ),
        Property(
            "object_class_filter",
            ArrayType(StringType),
            description="Filter entries by object class",
        ),
        Property(
            "attribute_filter",
            ArrayType(StringType),
            description="Include only specified attributes",
        ),
        Property(
            "exclude_attributes",
            ArrayType(StringType),
            description="Exclude specified attributes",
        ),
        Property(
            "include_operational_attributes",
            BooleanType,
            default=False,
            description="Include operational attributes in output",
        ),
        Property(
            "strict_parsing",
            BooleanType,
            default=True,
            description="Enable strict LDIF parsing (fail on errors)",
        ),
        Property(
            "max_file_size_mb",
            IntegerType,
            default=100,
            description="Maximum file size in MB to process",
        ),
    ).to_dict()

    def discover_streams(self: object) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.

        """
        return [
            LDIFEntriesStream(tap=self),
        ]

    def _get_ldif_entries_schema(self: object) -> dict[str, object]:
        """Get the schema for LDIF entries stream.

        Returns:
            Schema definition for LDIF entries.

        """
        return PropertiesList(
            Property(
                "dn",
                StringType,
                required=True,
                description="Distinguished Name",
            ),
            Property(
                "object_class",
                ArrayType(StringType),
                description="Object classes",
            ),
            Property("attributes", ObjectType(), description="LDAP attributes"),
            Property("change_type", StringType, description="LDIF change type"),
            Property("source_file", StringType, description="Source LDIF file"),
            Property(
                "line_number",
                IntegerType,
                description="Line number in source file",
            ),
            Property(
                "entry_size",
                IntegerType,
                description="Size of entry in bytes",
            ),
        ).to_dict()


def main() -> None:
    """Run the tap entry point."""
    TapLDIF.cli()


if __name__ == "__main__":
    main()
