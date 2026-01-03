"""Singer LDIF tap implementation using FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants, FlextLogger, FlextTypes as t

# Use FLEXT Meltano wrappers instead of direct singer_sdk imports (domain separation)
from flext_meltano import (
    FlextMeltanoStream as Stream,
    FlextMeltanoTap as Tap,
)
from flext_meltano.typings import t as t_meltano

from flext_tap_ldif.settings import FlextMeltanoTapLdifSettings
from flext_tap_ldif.streams import LDIFEntriesStream

logger = FlextLogger(__name__)


class TapLDIF(Tap):
    """Singer tap for LDIF file format data extraction."""

    name: str = "tap-ldif"
    config_class = FlextMeltanoTapLdifSettings
    # Schema combining file-based configuration with LDIF-specific properties
    config_jsonschema: ClassVar[dict[str, t.GeneralValueType]] = (
        t_meltano.Singer.Typing.PropertiesList(
            # File-based properties
            t_meltano.Singer.Typing.Property(
                "file_path",
                t_meltano.Singer.Typing.StringType,
                description="Path to single LDIF file",
            ),
            t_meltano.Singer.Typing.Property(
                "directory_path",
                t_meltano.Singer.Typing.StringType,
                description="Directory containing LDIF files",
            ),
            t_meltano.Singer.Typing.Property(
                "file_pattern",
                t_meltano.Singer.Typing.StringType,
                default="*.ldif",
                description="File pattern for matching LDIF files in directory",
            ),
            t_meltano.Singer.Typing.Property(
                "encoding",
                t_meltano.Singer.Typing.StringType,
                default="utf-8",
                description="Text encoding for LDIF files",
            ),
            # LDIF-specific additional properties
            t_meltano.Singer.Typing.Property(
                "base_dn_filter",
                t_meltano.Singer.Typing.StringType,
                description="Filter entries by base DN pattern",
            ),
            t_meltano.Singer.Typing.Property(
                "object_class_filter",
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Filter entries by object class",
            ),
            t_meltano.Singer.Typing.Property(
                "attribute_filter",
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Include only specified attributes",
            ),
            t_meltano.Singer.Typing.Property(
                "exclude_attributes",
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Exclude specified attributes",
            ),
            t_meltano.Singer.Typing.Property(
                "include_operational_attributes",
                t_meltano.Singer.Typing.BooleanType,
                default=False,
                description="Include operational attributes in output",
            ),
            t_meltano.Singer.Typing.Property(
                "strict_parsing",
                t_meltano.Singer.Typing.BooleanType,
                default=True,
                description="Enable strict LDIF parsing (fail on errors)",
            ),
            t_meltano.Singer.Typing.Property(
                "max_file_size_mb",
                t_meltano.Singer.Typing.IntegerType,
                default=FlextConstants.Logging.MAX_FILE_SIZE // (1024 * 1024),
                description="Maximum file size in MB to process",
            ),
        ).to_dict()
    )

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
        A list of discovered streams.

        """
        return [
            LDIFEntriesStream(tap=self),
        ]

    def _get_ldif_entries_schema(self) -> dict[str, t.GeneralValueType]:
        """Get the schema for LDIF entries stream.

        Returns:
        Schema definition for LDIF entries.

        """
        return t_meltano.Singer.Typing.PropertiesList(
            t_meltano.Singer.Typing.Property(
                "dn",
                t_meltano.Singer.Typing.StringType,
                required=True,
                description="Distinguished Name",
            ),
            t_meltano.Singer.Typing.Property(
                "object_class",
                t_meltano.Singer.Typing.ArrayType(
                    t_meltano.Singer.Typing.StringType,
                ),
                description="Object classes",
            ),
            t_meltano.Singer.Typing.Property(
                "attributes",
                t_meltano.Singer.Typing.ObjectType(),
                description="LDAP attributes",
            ),
            t_meltano.Singer.Typing.Property(
                "change_type",
                t_meltano.Singer.Typing.StringType,
                description="LDIF change type",
            ),
            t_meltano.Singer.Typing.Property(
                "source_file",
                t_meltano.Singer.Typing.StringType,
                description="Source LDIF file",
            ),
            t_meltano.Singer.Typing.Property(
                "line_number",
                t_meltano.Singer.Typing.IntegerType,
                description="Line number in source file",
            ),
            t_meltano.Singer.Typing.Property(
                "entry_size",
                t_meltano.Singer.Typing.IntegerType,
                description="Size of entry in bytes",
            ),
        ).to_dict()


def main() -> None:
    """Run the tap entry point."""
    TapLDIF.cli()


if __name__ == "__main__":
    main()
