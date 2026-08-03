"""Settings for FLEXT Tap LDIF — namespaced under ``settings.TapLdif``.

Universal fields via MRO; project fields in the ``TapLdif`` group with simple
scalar types (env-settable). Path derivation lives in consumers, not settings.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings, m


class FlextTapLdifSettings(FlextSettings):
    """Tap-LDIF runtime settings; fields under ``settings.TapLdif.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TAP_LDIF_",
        env_nested_delimiter="__",
        extra="ignore",
        validate_assignment=True,
    )

    class _TapLdif(m.BaseModel):
        """Namespaced tap-LDIF settings."""

        file_path: Annotated[
            str | None, m.Field(default=None, description="LDIF file path")
        ]
        directory_path: Annotated[
            str | None, m.Field(default=None, description="LDIF directory path")
        ]
        file_pattern: Annotated[
            str, m.Field(default="*.ldif", description="LDIF file glob pattern")
        ]
        encoding: Annotated[str, m.Field(default="utf-8", description="File encoding")]
        strict_parsing: Annotated[
            bool, m.Field(default=True, description="Strict LDIF parsing")
        ]
        max_file_size_mb: Annotated[
            int, m.Field(default=100, ge=1, description="Max file size (MB)")
        ]

    if TYPE_CHECKING:
        TapLdif: _TapLdif
    else:
        TapLdif: _TapLdif = m.Field(
            default_factory=_TapLdif, description="Namespaced tap-LDIF settings."
        )


settings: FlextTapLdifSettings = FlextTapLdifSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_tap_ldif import settings``."""

__all__: list[str] = ["FlextTapLdifSettings", "settings"]
