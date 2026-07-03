"""Singer state management utilities for LDIF tap files."""

from __future__ import annotations

from flext_meltano import u
from flext_tap_ldif import t


class FlextTapLdifUtilitiesStateManagement:
    """MRO mixin exposing StateManagement under u.TapLdif."""

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def resolve_file_position(
            state: t.JsonMapping,
            file_path: str,
        ) -> int:
            """Get current position in file."""
            file_state = (
                FlextTapLdifUtilitiesStateManagement.StateManagement.resolve_file_state(
                    state,
                    file_path,
                )
            )
            position = file_state.get("position", 0)
            return position if isinstance(position, int) else 0

        @classmethod
        def resolve_file_state(
            cls,
            state: t.JsonMapping,
            file_path: str,
        ) -> t.JsonMapping:
            """Get state for a specific file."""
            files_raw = state.get("files")
            if not u.mapping(files_raw):
                empty_state: t.JsonMapping = {}
                return empty_state
            file_state_raw = files_raw.get(file_path)
            return u.Cli.json_as_mapping(file_state_raw)

        @staticmethod
        def update_file_position(
            state: t.JsonMapping,
            file_path: str,
            position: int,
        ) -> t.JsonMapping:
            """Set current position in file."""
            file_state = (
                FlextTapLdifUtilitiesStateManagement.StateManagement.resolve_file_state(
                    state,
                    file_path,
                )
            )
            file_state_dict: t.MutableJsonMapping = dict(
                u.Cli.json_as_mapping(file_state)
            )
            file_state_dict["position"] = position
            file_state_dict["last_updated"] = u.generate_datetime_utc().isoformat()
            return (
                FlextTapLdifUtilitiesStateManagement.StateManagement.update_file_state(
                    state,
                    file_path,
                    file_state_dict,
                )
            )

        @classmethod
        def update_file_state(
            cls,
            state: t.JsonMapping,
            file_path: str,
            file_state: t.JsonMapping,
        ) -> t.JsonMapping:
            """Set state for a specific file."""
            files_raw = state.get("files")
            files_dict: t.MutableJsonMapping = {}
            if u.mapping(files_raw):
                for k, v in files_raw.items():
                    if u.mapping(v):
                        files_dict[k] = u.normalize_to_json_value(v)
            files_dict[file_path] = u.normalize_to_json_value(file_state)
            updated_state: t.MutableJsonMapping = {
                key: u.normalize_to_json_value(value) for key, value in state.items()
            }
            updated_state["files"] = u.normalize_to_json_value(files_dict)
            return updated_state
