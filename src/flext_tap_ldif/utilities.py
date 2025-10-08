"""Singer tap utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar, override

from flext_core import FlextResult, FlextTypes, FlextUtilities


class FlextMeltanoTapLdifUtilities(FlextUtilities):
    """Single unified utilities class for Singer tap LDIF operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with LDIF data sources.
    Extends FlextUtilities with LDIF tap-specific operations.
    """

    # Configuration constants
    DEFAULT_BATCH_SIZE: ClassVar[int] = 1000
    DEFAULT_ENCODING: ClassVar[str] = "utf-8"
    MAX_LINE_LENGTH: ClassVar[int] = 1024
    LDIF_LINE_CONTINUATION: ClassVar[str] = " "

    @override
    def __init__(self) -> None:
        """Initialize LDIF tap utilities."""
        super().__init__()

    class SingerUtilities:
        """Singer protocol utilities for tap operations."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: FlextTypes.Dict,
            key_properties: FlextTypes.StringList | None = None,
        ) -> FlextTypes.Dict:
            """Create Singer schema message.

            Args:
                stream_name: Name of the stream
                schema: JSON schema for the stream
                key_properties: List of key property names

            Returns:
                FlextTypes.Dict: Singer schema message

            """
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            }

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: FlextTypes.Dict,
            time_extracted: datetime | None = None,
        ) -> FlextTypes.Dict:
            """Create Singer record message.

            Args:
                stream_name: Name of the stream
                record: Record data
                time_extracted: Timestamp when record was extracted

            Returns:
                FlextTypes.Dict: Singer record message

            """
            extracted_time = time_extracted or datetime.now(UTC)
            return {
                "type": "RECORD",
                "stream": stream_name,
                "record": record,
                "time_extracted": extracted_time.isoformat(),
            }

        @staticmethod
        def create_state_message(state: FlextTypes.Dict) -> FlextTypes.Dict:
            """Create Singer state message.

            Args:
                state: State data

            Returns:
                FlextTypes.Dict: Singer state message

            """
            return {
                "type": "STATE",
                "value": state,
            }

        @staticmethod
        def write_message(message: FlextTypes.Dict) -> None:
            """Write Singer message to stdout.

            Args:
                message: Singer message to write

            """

    class LdifFileProcessing:
        """LDIF file processing utilities."""

        @staticmethod
        def validate_ldif_file(file_path: Path) -> FlextResult[bool]:
            """Validate LDIF file format and accessibility.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[bool]: True if valid, error if invalid

            """
            try:
                if not file_path.exists():
                    return FlextResult[bool].fail(
                        f"LDIF file does not exist: {file_path}"
                    )

                if not file_path.is_file():
                    return FlextResult[bool].fail(f"Path is not a file: {file_path}")

                # Check file extension
                if file_path.suffix.lower() not in {".ldif", ".ldif3", ".ldi"}:
                    return FlextResult[bool].fail(
                        f"File does not have LDIF extension: {file_path}"
                    )

                # Basic content validation
                with file_path.open(
                    "r", encoding=FlextMeltanoTapLdifUtilities.DEFAULT_ENCODING
                ) as f:
                    first_lines = [f.readline().strip() for _ in range(10)]

                # Check for LDIF indicators
                has_version = any(line.startswith("version:") for line in first_lines)
                has_dn = any(line.startswith("dn:") for line in first_lines)

                if not (has_version or has_dn):
                    return FlextResult[bool].fail(
                        f"File does not appear to be valid LDIF format: {file_path}"
                    )

                return FlextResult[bool].ok(True)

            except UnicodeDecodeError as e:
                return FlextResult[bool].fail(f"LDIF file encoding error: {e}")
            except Exception as e:
                return FlextResult[bool].fail(f"Error validating LDIF file: {e}")

        @staticmethod
        def count_ldif_entries(file_path: Path) -> FlextResult[int]:
            """Count number of entries in LDIF file.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[int]: Number of entries or error

            """
            try:
                if not file_path.exists():
                    return FlextResult[int].fail(
                        f"LDIF file does not exist: {file_path}"
                    )

                entry_count = 0
                with file_path.open(
                    "r", encoding=FlextMeltanoTapLdifUtilities.DEFAULT_ENCODING
                ) as f:
                    for line_str in f:
                        line = line_str.strip()
                        if line.startswith("dn:"):
                            entry_count += 1

                return FlextResult[int].ok(entry_count)

            except UnicodeDecodeError as e:
                return FlextResult[int].fail(f"LDIF file encoding error: {e}")
            except Exception as e:
                return FlextResult[int].fail(f"Error counting LDIF entries: {e}")

        @staticmethod
        def extract_ldif_metadata(file_path: Path) -> FlextResult[FlextTypes.Dict]:
            """Extract metadata from LDIF file.

            Args:
                file_path: Path to LDIF file

            Returns:
                FlextResult[FlextTypes.Dict]: Metadata dictionary or error

            """
            try:
                metadata: FlextTypes.Dict = {
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "version": None,
                    "entry_count": 0,
                    "base_dns": set(),
                    "object_classes": set(),
                }

                with file_path.open(
                    "r", encoding=FlextMeltanoTapLdifUtilities.DEFAULT_ENCODING
                ) as f:
                    for line_str in f:
                        line = line_str.strip()

                        if line.startswith("version:"):
                            metadata["version"] = line.split(":", 1)[1].strip()
                        elif line.startswith("dn:"):
                            metadata["entry_count"] += 1
                            dn = line.split(":", 1)[1].strip()
                            # Extract base DN (last two components)
                            min_dn_components_for_base = 2
                            dn_parts = [part.strip() for part in dn.split(",")]
                            if len(dn_parts) >= min_dn_components_for_base:
                                base_dn = ",".join(dn_parts[-2:])
                                metadata["base_dns"].add(base_dn)
                        elif line.startswith("objectClass:"):
                            obj_class = line.split(":", 1)[1].strip()
                            metadata["object_classes"].add(obj_class)

                # Convert sets to lists for JSON serialization
                metadata["base_dns"] = list(metadata["base_dns"])
                metadata["object_classes"] = list(metadata["object_classes"])

                return FlextResult[FlextTypes.Dict].ok(metadata)

            except Exception as e:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Error extracting LDIF metadata: {e}"
                )

    class LdifDataProcessing:
        """LDIF data processing utilities."""

        @staticmethod
        def parse_ldif_line(line: str) -> FlextResult[tuple[str, str]]:
            """Parse LDIF attribute line.

            Args:
                line: LDIF line to parse

            Returns:
                FlextResult[tuple[str, str]]: (attribute_name, value) or error

            """
            try:
                line = line.strip()
                if not line or line.startswith("#"):
                    return FlextResult[tuple[str, str]].fail("Empty or comment line")

                if ":" not in line:
                    return FlextResult[tuple[str, str]].fail("Invalid LDIF line format")

                # Handle base64 encoded values (::)
                if "::" in line:
                    attr_name, encoded_value = line.split("::", 1)

                    try:
                        decoded_value = base64.b64decode(encoded_value.strip()).decode(
                            "utf-8"
                        )
                        return FlextResult[tuple[str, str]].ok((
                            attr_name.strip(),
                            decoded_value,
                        ))
                    except Exception as e:
                        return FlextResult[tuple[str, str]].fail(
                            f"Base64 decode error: {e}"
                        )

                # Handle URL values (:<)
                if ":<" in line:
                    attr_name, url_value = line.split(":<", 1)
                    return FlextResult[tuple[str, str]].ok((
                        attr_name.strip(),
                        f"URL:{url_value.strip()}",
                    ))

                # Handle regular values (:)
                attr_name, value = line.split(":", 1)
                return FlextResult[tuple[str, str]].ok((
                    attr_name.strip(),
                    value.strip(),
                ))

            except Exception as e:
                return FlextResult[tuple[str, str]].fail(
                    f"Error parsing LDIF line: {e}"
                )

        @staticmethod
        def normalize_ldif_attribute_name(attr_name: str) -> str:
            """Normalize LDIF attribute name for JSON schema.

            Args:
                attr_name: LDIF attribute name

            Returns:
                str: Normalized attribute name

            """
            if not attr_name:
                return ""

            # Convert to lowercase and replace non-alphanumeric with underscores
            normalized = re.sub(r"[^a-zA-Z0-9]", "_", attr_name.lower())

            # Ensure it doesn't start with a number
            if normalized and normalized[0].isdigit():
                normalized = f"attr_{normalized}"

            return normalized

        @staticmethod
        def convert_ldif_entry_to_record(
            entry_lines: FlextTypes.StringList,
        ) -> FlextResult[FlextTypes.Dict]:
            """Convert LDIF entry lines to Singer record.

            Args:
                entry_lines: List of LDIF lines for single entry

            Returns:
                FlextResult[FlextTypes.Dict]: Singer record or error

            """
            try:
                record: FlextTypes.Dict = {}
                current_attr = None
                current_value = ""

                for line in entry_lines:
                    # Handle line continuation
                    if line.startswith(
                        FlextMeltanoTapLdifUtilities.LDIF_LINE_CONTINUATION
                    ):
                        if current_attr:
                            current_value += line[1:]  # Remove continuation character
                        continue

                    # Process previous attribute if exists
                    if current_attr and current_value:
                        normalized_attr = FlextMeltanoTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                            current_attr
                        )
                        if normalized_attr in record:
                            # Convert to list if multiple values
                            if not isinstance(record[normalized_attr], list):
                                record[normalized_attr] = [record[normalized_attr]]
                            record[normalized_attr].append(current_value)
                        else:
                            record[normalized_attr] = current_value

                    # Parse new attribute line
                    parse_result = (
                        FlextMeltanoTapLdifUtilities.LdifDataProcessing.parse_ldif_line(
                            line
                        )
                    )
                    if parse_result.is_success:
                        current_attr, current_value = parse_result.value
                    else:
                        current_attr = None
                        current_value = ""

                # Process final attribute
                if current_attr and current_value:
                    normalized_attr = FlextMeltanoTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                        current_attr
                    )
                    if normalized_attr in record:
                        if not isinstance(record[normalized_attr], list):
                            record[normalized_attr] = [record[normalized_attr]]
                        record[normalized_attr].append(current_value)
                    else:
                        record[normalized_attr] = current_value

                return FlextResult[FlextTypes.Dict].ok(record)

            except Exception as e:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Error converting LDIF entry: {e}"
                )

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_ldif_config(
            config: FlextTypes.Dict,
        ) -> FlextResult[FlextTypes.Dict]:
            """Validate LDIF tap configuration.

            Args:
                config: Configuration dictionary

            Returns:
                FlextResult[FlextTypes.Dict]: Validated config or error

            """
            required_fields = ["files"]
            missing_fields = [field for field in required_fields if field not in config]

            if missing_fields:
                return FlextResult[FlextTypes.Dict].fail(
                    f"Missing required fields: {', '.join(missing_fields)}"
                )

            # Validate files configuration
            files = config["files"]
            if not isinstance(files, list):
                return FlextResult[FlextTypes.Dict].fail("Files must be a list")

            if not files:
                return FlextResult[FlextTypes.Dict].fail(
                    "At least one file must be specified"
                )

            # Validate each file path
            for file_path in files:
                if not isinstance(file_path, str):
                    return FlextResult[FlextTypes.Dict].fail(
                        "File paths must be strings"
                    )

                path_obj = Path(file_path)
                if not path_obj.exists():
                    return FlextResult[FlextTypes.Dict].fail(
                        f"File does not exist: {file_path}"
                    )

            return FlextResult[FlextTypes.Dict].ok(config)

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def get_file_state(state: FlextTypes.Dict, file_path: str) -> FlextTypes.Dict:
            """Get state for a specific file.

            Args:
                state: Complete state dictionary
                file_path: Path to the file

            Returns:
                FlextTypes.Dict: File state

            """
            return state.get("files", {}).get(file_path, {})

        @staticmethod
        def set_file_state(
            state: FlextTypes.Dict,
            file_path: str,
            file_state: FlextTypes.Dict,
        ) -> FlextTypes.Dict:
            """Set state for a specific file.

            Args:
                state: Complete state dictionary
                file_path: Path to the file
                file_state: State data for the file

            Returns:
                FlextTypes.Dict: Updated state

            """
            if "files" not in state:
                state["files"] = {}

            state["files"][file_path] = file_state
            return state

        @staticmethod
        def get_file_position(state: FlextTypes.Dict, file_path: str) -> int:
            """Get current position in file.

            Args:
                state: Complete state dictionary
                file_path: Path to the file

            Returns:
                int: Current position or 0

            """
            file_state = FlextMeltanoTapLdifUtilities.StateManagement.get_file_state(
                state, file_path
            )
            return file_state.get("position", 0)

        @staticmethod
        def set_file_position(
            state: FlextTypes.Dict,
            file_path: str,
            position: int,
        ) -> FlextTypes.Dict:
            """Set current position in file.

            Args:
                state: Complete state dictionary
                file_path: Path to the file
                position: Current position

            Returns:
                FlextTypes.Dict: Updated state

            """
            if "files" not in state:
                state["files"] = {}
            if file_path not in state["files"]:
                state["files"][file_path] = {}

            state["files"][file_path]["position"] = position
            state["files"][file_path]["last_updated"] = datetime.now(UTC).isoformat()
            return state

    # Proxy methods for backward compatibility
    @classmethod
    def create_schema_message(
        cls,
        stream_name: str,
        schema: FlextTypes.Dict,
        key_properties: FlextTypes.StringList | None = None,
    ) -> FlextTypes.Dict:
        """Proxy method for SingerUtilities.create_schema_message()."""
        return cls.SingerUtilities.create_schema_message(
            stream_name, schema, key_properties
        )

    @classmethod
    def create_record_message(
        cls,
        stream_name: str,
        record: FlextTypes.Dict,
        time_extracted: datetime | None = None,
    ) -> FlextTypes.Dict:
        """Proxy method for SingerUtilities.create_record_message()."""
        return cls.SingerUtilities.create_record_message(
            stream_name, record, time_extracted
        )

    @classmethod
    def validate_ldif_file(cls, file_path: Path) -> FlextResult[bool]:
        """Proxy method for LdifFileProcessing.validate_ldif_file()."""
        return cls.LdifFileProcessing.validate_ldif_file(file_path)

    @classmethod
    def count_ldif_entries(cls, file_path: Path) -> FlextResult[int]:
        """Proxy method for LdifFileProcessing.count_ldif_entries()."""
        return cls.LdifFileProcessing.count_ldif_entries(file_path)

    @classmethod
    def parse_ldif_line(cls, line: str) -> FlextResult[tuple[str, str]]:
        """Proxy method for LdifDataProcessing.parse_ldif_line()."""
        return cls.LdifDataProcessing.parse_ldif_line(line)

    @classmethod
    def convert_ldif_entry_to_record(
        cls, entry_lines: FlextTypes.StringList
    ) -> FlextResult[FlextTypes.Dict]:
        """Proxy method for LdifDataProcessing.convert_ldif_entry_to_record()."""
        return cls.LdifDataProcessing.convert_ldif_entry_to_record(entry_lines)

    @classmethod
    def validate_ldif_config(
        cls, config: FlextTypes.Dict
    ) -> FlextResult[FlextTypes.Dict]:
        """Proxy method for ConfigValidation.validate_ldif_config()."""
        return cls.ConfigValidation.validate_ldif_config(config)

    @classmethod
    def get_file_state(cls, state: FlextTypes.Dict, file_path: str) -> FlextTypes.Dict:
        """Proxy method for StateManagement.get_file_state()."""
        return cls.StateManagement.get_file_state(state, file_path)

    @classmethod
    def set_file_position(
        cls,
        state: FlextTypes.Dict,
        file_path: str,
        position: int,
    ) -> FlextTypes.Dict:
        """Proxy method for StateManagement.set_file_position()."""
        return cls.StateManagement.set_file_position(state, file_path, position)


__all__ = [
    "FlextMeltanoTapLdifUtilities",
]
