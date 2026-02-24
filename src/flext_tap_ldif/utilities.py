"""Singer tap utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import re
from collections.abc import Mapping
from datetime import UTC, datetime
from pathlib import Path
from typing import override

from flext_core import FlextResult, FlextUtilities, t
from flext_meltano import FlextMeltanoModels as m

from flext_tap_ldif.constants import c


class FlextMeltanoTapLdifUtilities(FlextUtilities):
    """Single unified utilities class for Singer tap LDIF operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with LDIF data sources.
    Extends up-specific operations.

    Constants are accessed via constants module:
        c.Format.LINE_CONTINUATION
        c.TapLdifPerformance.DEFAULT_BATCH_SIZE
        c.DEFAULT_LDIF_ENCODING
        c.Format.MAX_LINE_LENGTH
    """

    @override
    def __init__(self) -> None:
        """Initialize LDIF tap utilities."""
        super().__init__()

    class TapLdif:
        """Singer protocol utilities for tap operations."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: Mapping[str, t.JsonValue],
            key_properties: list[str] | None = None,
        ) -> m.Meltano.SingerSchemaMessage:
            """Create Singer schema message.

            Args:
            stream_name: Name of the stream
            schema: JSON schema for the stream
            key_properties: List of key property names

            Returns:
            dict[str, t.GeneralValueType]: Singer schema message

            """
            return m.Meltano.SingerSchemaMessage.model_validate({
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            })

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: Mapping[str, t.JsonValue],
            time_extracted: datetime | None = None,
        ) -> m.Meltano.SingerRecordMessage:
            """Create Singer record message.

            Args:
            stream_name: Name of the stream
            record: Record data
            time_extracted: Timestamp when record was extracted

            Returns:
            dict[str, t.GeneralValueType]: Singer record message

            """
            extracted_time = time_extracted or datetime.now(UTC)
            return m.Meltano.SingerRecordMessage.model_validate({
                "stream": stream_name,
                "record": record,
                "time_extracted": extracted_time.isoformat(),
            })

        @staticmethod
        def create_state_message(
            state: Mapping[str, t.GeneralValueType],
        ) -> m.Meltano.SingerStateMessage:
            """Create Singer state message from state data.

            Args:
            state: State bookmark payload

            Returns:
            SingerStateMessage model

            """
            return m.Meltano.SingerStateMessage.model_validate({"value": state})

        @staticmethod
        def write_message(
            message: (
                m.Meltano.SingerSchemaMessage
                | m.Meltano.SingerRecordMessage
                | m.Meltano.SingerStateMessage
            ),
        ) -> None:
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
                        f"LDIF file does not exist: {file_path}",
                    )

                if not file_path.is_file():
                    return FlextResult[bool].fail(f"Path is not a file: {file_path}")

                # Check file extension
                if file_path.suffix.lower() not in {".ldif", ".ldif3", ".ldi"}:
                    return FlextResult[bool].fail(
                        f"File does not have LDIF extension: {file_path}",
                    )

                # Basic content validation
                with file_path.open(
                    "r",
                    encoding=c.DEFAULT_LDIF_ENCODING,
                ) as f:
                    first_lines = [f.readline().strip() for _ in range(10)]

                # Check for LDIF indicators
                has_version = any(line.startswith("version:") for line in first_lines)
                has_dn = any(line.startswith("dn:") for line in first_lines)

                if not (has_version or has_dn):
                    return FlextResult[bool].fail(
                        f"File does not appear to be valid LDIF format: {file_path}",
                    )

                return FlextResult[bool].ok(value=True)

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
                        f"LDIF file does not exist: {file_path}",
                    )

                entry_count = 0
                with file_path.open(
                    "r",
                    encoding=c.DEFAULT_LDIF_ENCODING,
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
        def extract_ldif_metadata(
            file_path: Path,
        ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
            """Extract metadata from LDIF file.

            Args:
            file_path: Path to LDIF file

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Metadata dictionary or error

            """
            try:
                version: str | None = None
                entry_count = 0
                base_dns: set[str] = set()
                object_classes: set[str] = set()

                with file_path.open(
                    "r",
                    encoding=c.DEFAULT_LDIF_ENCODING,
                ) as f:
                    for line_str in f:
                        line = line_str.strip()

                        if line.startswith("version:"):
                            version = line.split(":", 1)[1].strip()
                        elif line.startswith("dn:"):
                            entry_count += 1
                            dn = line.split(":", 1)[1].strip()
                            # Extract base DN (last two components)
                            min_dn_components_for_base = 2
                            dn_parts = [part.strip() for part in dn.split(",")]
                            if len(dn_parts) >= min_dn_components_for_base:
                                base_dn = ",".join(dn_parts[-2:])
                                base_dns.add(base_dn)
                        elif line.startswith("objectClass:"):
                            obj_class = line.split(":", 1)[1].strip()
                            object_classes.add(obj_class)

                metadata: dict[str, t.GeneralValueType] = {
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "version": version,
                    "entry_count": entry_count,
                    "base_dns": list(base_dns),
                    "object_classes": list(object_classes),
                }

                return FlextResult[Mapping[str, t.GeneralValueType]].ok(metadata)

            except Exception as e:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    f"Error extracting LDIF metadata: {e}",
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
                            "utf-8",
                        )
                        return FlextResult[tuple[str, str]].ok((
                            attr_name.strip(),
                            decoded_value,
                        ))
                    except Exception as e:
                        return FlextResult[tuple[str, str]].fail(
                            f"Base64 decode error: {e}",
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
                    f"Error parsing LDIF line: {e}",
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
        def build_record_from_lines(
            entry_lines: list[str],
        ) -> Mapping[str, str | list[str]]:
            """Build record dict from LDIF lines. Returns concrete type for type checker."""
            record: dict[str, str | list[str]] = {}
            current_attr: str | None = None
            current_value: str = ""

            for line in entry_lines:
                if line.startswith(c.Format.LINE_CONTINUATION):
                    if current_attr is not None:
                        current_value += line[1:]
                    continue

                if current_attr is not None and current_value:
                    normalized_attr = FlextMeltanoTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                        current_attr,
                    )
                    if normalized_attr in record:
                        existing_value = record[normalized_attr]
                        if u.Guards.is_list(existing_value):
                            existing_value.append(current_value)
                        else:
                            record[normalized_attr] = [
                                str(existing_value),
                                current_value,
                            ]
                    else:
                        record[normalized_attr] = current_value

                parse_result = (
                    FlextMeltanoTapLdifUtilities.LdifDataProcessing.parse_ldif_line(
                        line,
                    )
                )
                if parse_result.is_success:
                    a, v = parse_result.value
                    current_attr = a
                    current_value = v
                else:
                    current_attr = None
                    current_value = ""

            if current_attr is not None and current_value:
                normalized_attr = FlextMeltanoTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                    current_attr,
                )
                if normalized_attr in record:
                    existing_value = record[normalized_attr]
                    if u.Guards.is_list(existing_value):
                        existing_value.append(current_value)
                    else:
                        record[normalized_attr] = [
                            str(existing_value),
                            current_value,
                        ]
                else:
                    record[normalized_attr] = current_value

            return record

        @staticmethod
        def convert_ldif_entry_to_record(
            entry_lines: list[str],
        ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
            """Convert LDIF entry lines to Singer record.

            Args:
            entry_lines: List of LDIF lines for single entry

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Singer record or error

            """
            try:
                record = FlextMeltanoTapLdifUtilities.LdifDataProcessing.build_record_from_lines(
                    entry_lines,
                )
                out: dict[str, t.GeneralValueType] = dict(record)
                return FlextResult[Mapping[str, t.GeneralValueType]].ok(out)
            except Exception as e:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    f"Error converting LDIF entry: {e}",
                )

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_ldif_config(
            config: Mapping[str, t.GeneralValueType],
        ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
            """Validate LDIF tap configuration.

            Args:
            config: Configuration dictionary

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Validated config or error

            """
            required_fields = ["files"]
            missing_fields = [field for field in required_fields if field not in config]

            if missing_fields:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    f"Missing required fields: {', '.join(missing_fields)}",
                )

            # Validate files configuration
            files = config["files"]
            if not u.Guards.is_list(files):
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    "Files must be a list"
                )

            if not files:
                return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                    "At least one file must be specified",
                )

            # Validate each file path
            for file_path in files:
                if not u.Guards.is_type(file_path, str):
                    return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                        "File paths must be strings",
                    )

                path_obj = Path(file_path)
                if not path_obj.exists():
                    return FlextResult[Mapping[str, t.GeneralValueType]].fail(
                        f"File does not exist: {file_path}",
                    )

            return FlextResult[Mapping[str, t.GeneralValueType]].ok(config)

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def get_file_state(
            state: Mapping[str, t.GeneralValueType],
            file_path: str,
        ) -> Mapping[str, t.GeneralValueType]:
            """Get state for a specific file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file

            Returns:
            dict[str, t.GeneralValueType]: File state

            """
            files_raw = state.get("files")
            if not u.is_dict_like(files_raw):
                return {}
            file_state_raw = files_raw.get(file_path)
            if not u.is_dict_like(file_state_raw):
                return {}
            return {
                str(key): value
                for key, value in file_state_raw.items()
                if u.Guards.is_type(key, str)
            }

        @staticmethod
        def set_file_state(
            state: Mapping[str, t.GeneralValueType],
            file_path: str,
            file_state: Mapping[str, t.GeneralValueType],
        ) -> Mapping[str, t.GeneralValueType]:
            """Set state for a specific file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file
            file_state: State data for the file

            Returns:
            dict[str, t.GeneralValueType]: Updated state

            """
            files_raw = state.get("files")
            files_dict: dict[str, dict[str, t.GeneralValueType]] = {}
            if u.is_dict_like(files_raw):
                for key, value in files_raw.items():
                    if u.Guards.is_type(key, str) and u.is_dict_like(value):
                        files_dict[key] = {
                            str(inner_key): inner_value
                            for inner_key, inner_value in value.items()
                            if u.Guards.is_type(inner_key, str)
                        }
            files_dict[file_path] = dict(file_state)
            updated_state: dict[str, t.GeneralValueType] = dict(state)
            updated_state["files"] = files_dict
            return updated_state

        @staticmethod
        def get_file_position(
            state: Mapping[str, t.GeneralValueType], file_path: str
        ) -> int:
            """Get current position in file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file

            Returns:
            int: Current position or 0

            """
            file_state = FlextMeltanoTapLdifUtilities.StateManagement.get_file_state(
                state,
                file_path,
            )
            position = file_state.get("position", 0)
            return position if u.Guards.is_type(position, int) else 0

        @staticmethod
        def set_file_position(
            state: Mapping[str, t.GeneralValueType],
            file_path: str,
            position: int,
        ) -> Mapping[str, t.GeneralValueType]:
            """Set current position in file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file
            position: Current position

            Returns:
            dict[str, t.GeneralValueType]: Updated state

            """
            file_state = FlextMeltanoTapLdifUtilities.StateManagement.get_file_state(
                state,
                file_path,
            )
            file_state_dict: dict[str, t.GeneralValueType] = dict(file_state)
            file_state_dict["position"] = position
            file_state_dict["last_updated"] = datetime.now(UTC).isoformat()
            return FlextMeltanoTapLdifUtilities.StateManagement.set_file_state(
                state,
                file_path,
                file_state_dict,
            )

    # Proxy methods for backward compatibility
    @classmethod
    def create_schema_message(
        cls,
        stream_name: str,
        schema: Mapping[str, t.JsonValue],
        key_properties: list[str] | None = None,
    ) -> m.Meltano.SingerSchemaMessage:
        """Proxy method for SingerUtilities.create_schema_message()."""
        return cls.TapLdif.create_schema_message(
            stream_name,
            schema,
            key_properties,
        )

    @classmethod
    def create_record_message(
        cls,
        stream_name: str,
        record: Mapping[str, t.JsonValue],
        time_extracted: datetime | None = None,
    ) -> m.Meltano.SingerRecordMessage:
        """Proxy method for SingerUtilities.create_record_message()."""
        return cls.TapLdif.create_record_message(
            stream_name,
            record,
            time_extracted,
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
        cls,
        entry_lines: list[str],
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Proxy method for LdifDataProcessing.convert_ldif_entry_to_record()."""
        return cls.LdifDataProcessing.convert_ldif_entry_to_record(entry_lines)

    @classmethod
    def validate_ldif_config(
        cls,
        config: Mapping[str, t.GeneralValueType],
    ) -> FlextResult[Mapping[str, t.GeneralValueType]]:
        """Proxy method for ConfigValidation.validate_ldif_config()."""
        return cls.ConfigValidation.validate_ldif_config(config)

    @classmethod
    def get_file_state(
        cls,
        state: Mapping[str, t.GeneralValueType],
        file_path: str,
    ) -> Mapping[str, t.GeneralValueType]:
        """Proxy method for StateManagement.get_file_state()."""
        return cls.StateManagement.get_file_state(state, file_path)

    @classmethod
    def set_file_position(
        cls,
        state: Mapping[str, t.GeneralValueType],
        file_path: str,
        position: int,
    ) -> Mapping[str, t.GeneralValueType]:
        """Proxy method for StateManagement.set_file_position()."""
        return cls.StateManagement.set_file_position(state, file_path, position)


# Runtime alias for simplified usage
u = FlextMeltanoTapLdifUtilities

__all__ = [
    "FlextMeltanoTapLdifUtilities",
    "u",
]
