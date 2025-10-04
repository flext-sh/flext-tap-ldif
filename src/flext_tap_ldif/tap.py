"""Singer LDIF tap implementation using FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants, FlextLogger, FlextTypes

# Use FLEXT Meltano wrappers instead of direct singer_sdk imports (domain separation)
from flext_meltano import FlextMeltanoTypes, FlextStream as Stream, FlextTap as Tap

from flext_tap_ldif.config import FlextTapLdifConfig
from flext_tap_ldif.streams import LDIFEntriesStream

logger = FlextLogger(__name__)


class TapLDIF(Tap):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = FlextTapLdifConfig
    # Schema combining file-based configuration with LDIF-specific properties
    config_jsonschema: ClassVar[FlextTypes.Dict] = (
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            # File-based properties
            FlextMeltanoTypes.Singer.Typing.Property(
                "file_path",
                FlextMeltanoTypes.Singer.Typing.StringType,
                description="Path to single LDIF file",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "directory_path",
                FlextMeltanoTypes.Singer.Typing.StringType,
                description="Directory containing LDIF files",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "file_pattern",
                FlextMeltanoTypes.Singer.Typing.StringType,
                default="*.ldif",
                description="File pattern for matching LDIF files in directory",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "encoding",
                FlextMeltanoTypes.Singer.Typing.StringType,
                default="utf-8",
                description="Text encoding for LDIF files",
            ),
            # LDIF-specific additional properties
            FlextMeltanoTypes.Singer.Typing.Property(
                "base_dn_filter",
                FlextMeltanoTypes.Singer.Typing.StringType,
                description="Filter entries by base DN pattern",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "object_class_filter",
                FlextMeltanoTypes.Singer.Typing.ArrayType(FlextMeltanoTypes.Singer.Typing.StringType),
                description="Filter entries by object class",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "attribute_filter",
                FlextMeltanoTypes.Singer.Typing.ArrayType(FlextMeltanoTypes.Singer.Typing.StringType),
                description="Include only specified attributes",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "exclude_attributes",
                FlextMeltanoTypes.Singer.Typing.ArrayType(FlextMeltanoTypes.Singer.Typing.StringType),
                description="Exclude specified attributes",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "include_operational_attributes",
                FlextMeltanoTypes.Singer.Typing.BooleanType,
                default=False,
                description="Include operational attributes in output",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "strict_parsing",
                FlextMeltanoTypes.Singer.Typing.BooleanType,
                default=True,
                description="Enable strict LDIF parsing (fail on errors)",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "max_file_size_mb",
                FlextMeltanoTypes.Singer.Typing.IntegerType,
                default=FlextConstants.Logging.MAX_FILE_SIZE // (1024 * 1024),
                description="Maximum file size in MB to process",
            ),
        ).to_dict()
    )

    def discover_streams(self: object) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.

        """
        return [
            LDIFEntriesStream(tap=self),
        ]

    def _get_ldif_entries_schema(self: object) -> FlextTypes.Dict:
        """Get the schema for LDIF entries stream.

        Returns:
            Schema definition for LDIF entries.

        """
        return FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "dn",
                FlextMeltanoTypes.Singer.Typing.StringType,
                required=True,
                description="Distinguished Name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "object_class",
                FlextMeltanoTypes.Singer.Typing.ArrayType(FlextMeltanoTypes.Singer.Typing.StringType),
                description="Object classes",
            ),
            FlextMeltanoTypes.Singer.Typing.Property("attributes", FlextMeltanoTypes.Singer.Typing.ObjectType(), description="LDAP attributes"),
            FlextMeltanoTypes.Singer.Typing.Property("change_type", FlextMeltanoTypes.Singer.Typing.StringType, description="LDIF change type"),
            FlextMeltanoTypes.Singer.Typing.Property("source_file", FlextMeltanoTypes.Singer.Typing.StringType, description="Source LDIF file"),
            FlextMeltanoTypes.Singer.Typing.Property(
                "line_number",
                FlextMeltanoTypes.Singer.Typing.IntegerType,
                description="Line number in source file",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "entry_size",
                FlextMeltanoTypes.Singer.Typing.IntegerType,
                description="Size of entry in bytes",
            ),
        ).to_dict()


def main() -> None:
    """Run the tap entry point."""
    TapLDIF.cli()


if __name__ == "__main__":
    main()
