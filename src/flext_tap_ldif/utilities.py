"""Singer tap utilities for LDIF domain operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import base64
import re
from collections.abc import Mapping, MutableMapping
from datetime import UTC, datetime
from pathlib import Path
from typing import TypeIs, override

from flext_core import r, t
from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities

from flext_tap_ldif.constants import c
from flext_tap_ldif.models import m


class FlextTapLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
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
        def create_record_message(
            stream_name: str,
            record: t.ConfigurationMapping,
            time_extracted: datetime | None = None,
        ) -> m.Meltano.SingerRecordMessage:
            """Create Singer record message.

            Args:
            stream_name: Name of the stream
            record: Record data
            time_extracted: Timestamp when record was extracted

            Returns:
            Mapping[str, t.ContainerValue]: Singer record message

            """
            extracted_time = time_extracted or datetime.now(UTC)
            return m.Meltano.SingerRecordMessage.model_validate({
                "stream": stream_name,
                "record": record,
                "time_extracted": extracted_time.isoformat(),
            })

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: t.FlatContainerMapping,
            key_properties: t.StrSequence | None = None,
        ) -> m.Meltano.SingerSchemaMessage:
            """Create Singer schema message.

            Args:
            stream_name: Name of the stream
            schema: JSON schema for the stream
            key_properties: List of key property names

            Returns:
            Mapping[str, t.ContainerValue]: Singer schema message

            """
            return m.Meltano.SingerSchemaMessage.model_validate({
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            })

        @staticmethod
        def create_state_message(
            state: t.ContainerMapping,
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
            _message: m.Meltano.SingerSchemaMessage
            | m.Meltano.SingerRecordMessage
            | m.Meltano.SingerStateMessage,
        ) -> None:
            """Write Singer message to stdout.

            Args:
            message: Singer message to write

            """

    class LdifFileProcessing:
        """LDIF file processing utilities."""

        @staticmethod
        def count_ldif_entries(file_path: Path) -> r[int]:
            """Count number of entries in LDIF file.

            Args:
            file_path: Path to LDIF file

            Returns:
            r[int]: Number of entries or error

            """
            try:
                if not file_path.exists():
                    return r[int].fail(f"LDIF file does not exist: {file_path}")
                entry_count = 0
                with file_path.open("r", encoding=c.DEFAULT_LDIF_ENCODING) as f:
                    for line_str in f:
                        line = line_str.strip()
                        if line.startswith("dn:"):
                            entry_count += 1
                return r[int].ok(entry_count)
            except UnicodeDecodeError as e:
                return r[int].fail(f"LDIF file encoding error: {e}")
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[int].fail(f"Error counting LDIF entries: {e}")

        @staticmethod
        def extract_ldif_metadata(
            file_path: Path,
        ) -> r[t.ContainerMapping]:
            """Extract metadata from LDIF file.

            Args:
            file_path: Path to LDIF file

            Returns:
            r[Mapping[str, t.ContainerValue]]: Metadata dictionary or error

            """
            try:
                version: str | None = None
                entry_count = 0
                base_dns: set[str] = set()
                object_classes: set[str] = set()
                with file_path.open("r", encoding=c.DEFAULT_LDIF_ENCODING) as f:
                    for line_str in f:
                        line = line_str.strip()
                        if line.startswith("version:"):
                            version = line.split(":", 1)[1].strip()
                        elif line.startswith("dn:"):
                            entry_count += 1
                            dn = line.split(":", 1)[1].strip()
                            min_dn_components_for_base = 2
                            dn_parts = [part.strip() for part in dn.split(",")]
                            if len(dn_parts) >= min_dn_components_for_base:
                                base_dn = ",".join(dn_parts[-2:])
                                base_dns.add(base_dn)
                        elif line.startswith("objectClass:"):
                            obj_class = line.split(":", 1)[1].strip()
                            object_classes.add(obj_class)
                metadata: t.ContainerMapping = {
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "version": version,
                    "entry_count": entry_count,
                    "base_dns": list(base_dns),
                    "object_classes": list(object_classes),
                }
                return r[t.ContainerMapping].ok(metadata)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[t.ContainerMapping].fail(
                    f"Error extracting LDIF metadata: {e}",
                )

        @staticmethod
        def validate_ldif_file(file_path: Path) -> r[bool]:
            """Validate LDIF file format and accessibility.

            Args:
            file_path: Path to LDIF file

            Returns:
            r[bool]: True if valid, error if invalid

            """
            try:
                if not file_path.exists():
                    return r[bool].fail(f"LDIF file does not exist: {file_path}")
                if not file_path.is_file():
                    return r[bool].fail(f"Path is not a file: {file_path}")
                if file_path.suffix.lower() not in {".ldif", ".ldif3", ".ldi"}:
                    return r[bool].fail(
                        f"File does not have LDIF extension: {file_path}",
                    )
                with file_path.open("r", encoding=c.DEFAULT_LDIF_ENCODING) as f:
                    first_lines = [f.readline().strip() for _ in range(10)]
                has_version = any(line.startswith("version:") for line in first_lines)
                has_dn = any(line.startswith("dn:") for line in first_lines)
                if not (has_version or has_dn):
                    return r[bool].fail(
                        f"File does not appear to be valid LDIF format: {file_path}",
                    )
                return r[bool].ok(value=True)
            except UnicodeDecodeError as e:
                return r[bool].fail(f"LDIF file encoding error: {e}")
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[bool].fail(f"Error validating LDIF file: {e}")

    class LdifDataProcessing:
        """LDIF data processing utilities."""

        @staticmethod
        def build_record_from_lines(
            entry_lines: t.StrSequence,
        ) -> MutableMapping[str, str | t.StrSequence]:
            """Build record dict from LDIF lines."""
            record: MutableMapping[str, str | t.StrSequence] = {}
            current_attr: str | None = None
            current_value: str = ""
            for line in entry_lines:
                if line.startswith(c.Format.LINE_CONTINUATION):
                    if current_attr is not None:
                        current_value += line[1:]
                    continue
                if current_attr is not None and current_value:
                    normalized_attr = FlextTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                        current_attr,
                    )
                    if normalized_attr in record:
                        existing_value = record[normalized_attr]
                        if isinstance(existing_value, list):
                            existing_value.append(current_value)
                        else:
                            record[normalized_attr] = [
                                str(existing_value),
                                current_value,
                            ]
                    else:
                        record[normalized_attr] = current_value
                parse_result = FlextTapLdifUtilities.LdifDataProcessing.parse_ldif_line(
                    line,
                )
                if parse_result.is_success:
                    a, v = parse_result.value
                    current_attr = a
                    current_value = v
                else:
                    current_attr = None
                    current_value = ""
            if current_attr is not None and current_value:
                normalized_attr = FlextTapLdifUtilities.LdifDataProcessing.normalize_ldif_attribute_name(
                    current_attr,
                )
                if normalized_attr in record:
                    existing_value = record[normalized_attr]
                    if isinstance(existing_value, list):
                        existing_value.append(current_value)
                    else:
                        record[normalized_attr] = [str(existing_value), current_value]
                else:
                    record[normalized_attr] = current_value
            return record

        @staticmethod
        def convert_ldif_entry_to_record(
            entry_lines: t.StrSequence,
        ) -> r[Mapping[str, str | t.StrSequence]]:
            """Convert LDIF entry lines to Singer record.

            Args:
            entry_lines: List of LDIF lines for single entry

            Returns:
            r[Mapping[str, str | t.StrSequence]]: Singer record or error

            """
            try:
                record = (
                    FlextTapLdifUtilities.LdifDataProcessing.build_record_from_lines(
                        entry_lines,
                    )
                )
                out: Mapping[str, str | t.StrSequence] = dict(record)
                return r[Mapping[str, str | t.StrSequence]].ok(out)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[Mapping[str, str | t.StrSequence]].fail(
                    f"Error converting LDIF entry: {e}",
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
            normalized = re.sub(r"[^a-zA-Z0-9]", "_", attr_name.lower())
            if normalized and normalized[0].isdigit():
                normalized = f"attr_{normalized}"
            return normalized

        @staticmethod
        def parse_ldif_line(line: str) -> r[tuple[str, str]]:
            """Parse LDIF attribute line.

            Args:
            line: LDIF line to parse

            Returns:
            r[tuple[str, str]]: (attribute_name, value) or error

            """
            try:
                line = line.strip()
                if not line or line.startswith("#"):
                    return r[tuple[str, str]].fail("Empty or comment line")
                if ":" not in line:
                    return r[tuple[str, str]].fail("Invalid LDIF line format")
                if "::" in line:
                    attr_name, encoded_value = line.split("::", 1)
                    try:
                        decoded_value = base64.b64decode(encoded_value.strip()).decode(
                            "utf-8",
                        )
                        return r[tuple[str, str]].ok((
                            attr_name.strip(),
                            decoded_value,
                        ))
                    except (
                        ValueError,
                        TypeError,
                        KeyError,
                        AttributeError,
                        OSError,
                        RuntimeError,
                        ImportError,
                    ) as e:
                        return r[tuple[str, str]].fail(f"Base64 decode error: {e}")
                if ":<" in line:
                    attr_name, url_value = line.split(":<", 1)
                    return r[tuple[str, str]].ok((
                        attr_name.strip(),
                        f"URL:{url_value.strip()}",
                    ))
                attr_name, value = line.split(":", 1)
                return r[tuple[str, str]].ok((
                    attr_name.strip(),
                    value.strip(),
                ))
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return r[tuple[str, str]].fail(f"Error parsing LDIF line: {e}")

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_ldif_config(
            config: t.ContainerMapping,
        ) -> r[t.ContainerMapping]:
            """Validate LDIF tap configuration.

            Args:
            config: Configuration dictionary

            Returns:
            r[Mapping[str, t.ContainerValue]]: Validated config or error

            """
            required_fields = ["files"]
            missing_fields = [field for field in required_fields if field not in config]
            if missing_fields:
                return r[t.ContainerMapping].fail(
                    f"Missing required fields: {', '.join(missing_fields)}",
                )
            files = config["files"]
            if not u.is_list(files):
                return r[t.ContainerMapping].fail("Files must be a list")
            if not files:
                return r[t.ContainerMapping].fail(
                    "At least one file must be specified",
                )
            for file_path in files:
                if not u.is_type(file_path, str):
                    return r[t.ContainerMapping].fail(
                        "File paths must be strings",
                    )
                path_obj = (
                    Path(file_path)
                    if isinstance(file_path, str)
                    else Path(str(file_path))
                )
                if not path_obj.exists():
                    return r[t.ContainerMapping].fail(
                        f"File does not exist: {file_path}",
                    )
            return r[t.ContainerMapping].ok(config)

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def _is_str_object_mapping(
            value: t.NormalizedValue,
        ) -> TypeIs[t.ContainerMapping]:
            return isinstance(value, Mapping)

        @classmethod
        def _is_nested_state_mapping(
            cls,
            value: t.NormalizedValue,
        ) -> TypeIs[Mapping[str, t.ContainerMapping]]:
            if not cls._is_str_object_mapping(value):
                return False
            return all(cls._is_str_object_mapping(item) for item in value.values())

        @staticmethod
        def get_file_position(
            state: t.ContainerMapping,
            file_path: str,
        ) -> int:
            """Get current position in file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file

            Returns:
            int: Current position or 0

            """
            file_state = FlextTapLdifUtilities.StateManagement.get_file_state(
                state,
                file_path,
            )
            position = file_state.get("position", 0)
            return position if isinstance(position, int) else 0

        @classmethod
        def get_file_state(
            cls,
            state: t.ContainerMapping,
            file_path: str,
        ) -> t.ContainerMapping:
            """Get state for a specific file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file

            Returns:
            Mapping[str, t.ContainerValue]: File state

            """
            files_raw = state.get("files")
            if not cls._is_str_object_mapping(files_raw):
                empty: t.ContainerMapping = {}
                return empty
            file_state_raw = files_raw.get(file_path)
            if not cls._is_str_object_mapping(file_state_raw):
                empty_state: t.ContainerMapping = {}
                return empty_state
            return dict(file_state_raw)

        @staticmethod
        def set_file_position(
            state: t.ContainerMapping,
            file_path: str,
            position: int,
        ) -> t.ContainerMapping:
            """Set current position in file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file
            position: Current position

            Returns:
            Mapping[str, t.ContainerValue]: Updated state

            """
            file_state = FlextTapLdifUtilities.StateManagement.get_file_state(
                state,
                file_path,
            )
            file_state_dict: MutableMapping[str, t.NormalizedValue] = dict(file_state)
            file_state_dict["position"] = position
            file_state_dict["last_updated"] = datetime.now(UTC).isoformat()
            return FlextTapLdifUtilities.StateManagement.set_file_state(
                state,
                file_path,
                file_state_dict,
            )

        @classmethod
        def set_file_state(
            cls,
            state: t.ContainerMapping,
            file_path: str,
            file_state: t.ContainerMapping,
        ) -> t.ContainerMapping:
            """Set state for a specific file.

            Args:
            state: Complete state dictionary
            file_path: Path to the file
            file_state: State data for the file

            Returns:
            Mapping[str, t.ContainerValue]: Updated state

            """
            files_raw = state.get("files")
            files_dict: MutableMapping[str, t.NormalizedValue] = {}
            if isinstance(files_raw, Mapping):
                for k, v in files_raw.items():
                    if isinstance(v, Mapping):
                        files_dict[k] = dict(v)
            files_dict[file_path] = dict(file_state)
            updated_state: MutableMapping[str, t.NormalizedValue] = dict(state)
            updated_state["files"] = files_dict
            return updated_state

    @classmethod
    def convert_ldif_entry_to_record(
        cls,
        entry_lines: t.StrSequence,
    ) -> r[Mapping[str, str | t.StrSequence]]:
        """Proxy method for LdifDataProcessing.convert_ldif_entry_to_record()."""
        return cls.LdifDataProcessing.convert_ldif_entry_to_record(entry_lines)

    @classmethod
    def count_ldif_entries(cls, file_path: Path) -> r[int]:
        """Proxy method for LdifFileProcessing.count_ldif_entries()."""
        return cls.LdifFileProcessing.count_ldif_entries(file_path)

    @classmethod
    def create_record_message(
        cls,
        stream_name: str,
        record: t.ConfigurationMapping,
        time_extracted: datetime | None = None,
    ) -> m.Meltano.SingerRecordMessage:
        """Proxy method for SingerUtilities.create_record_message()."""
        return cls.TapLdif.create_record_message(stream_name, record, time_extracted)

    @classmethod
    def create_schema_message(
        cls,
        stream_name: str,
        schema: t.FlatContainerMapping,
        key_properties: t.StrSequence | None = None,
    ) -> m.Meltano.SingerSchemaMessage:
        """Proxy method for SingerUtilities.create_schema_message()."""
        return cls.TapLdif.create_schema_message(stream_name, schema, key_properties)

    @classmethod
    def get_file_state(
        cls,
        state: t.ContainerMapping,
        file_path: str,
    ) -> t.ContainerMapping:
        """Proxy method for StateManagement.get_file_state()."""
        return cls.StateManagement.get_file_state(state, file_path)

    @classmethod
    def parse_ldif_line(cls, line: str) -> r[tuple[str, str]]:
        """Proxy method for LdifDataProcessing.parse_ldif_line()."""
        return cls.LdifDataProcessing.parse_ldif_line(line)

    @classmethod
    def set_file_position(
        cls,
        state: t.ContainerMapping,
        file_path: str,
        position: int,
    ) -> t.ContainerMapping:
        """Proxy method for StateManagement.set_file_position()."""
        return cls.StateManagement.set_file_position(state, file_path, position)

    @classmethod
    def validate_ldif_config(
        cls,
        config: t.ContainerMapping,
    ) -> r[t.ContainerMapping]:
        """Proxy method for ConfigValidation.validate_ldif_config()."""
        return cls.ConfigValidation.validate_ldif_config(config)

    @classmethod
    def validate_ldif_file(cls, file_path: Path) -> r[bool]:
        """Proxy method for LdifFileProcessing.validate_ldif_file()."""
        return cls.LdifFileProcessing.validate_ldif_file(file_path)


u = FlextTapLdifUtilities
__all__ = ["FlextTapLdifUtilities", "u"]
