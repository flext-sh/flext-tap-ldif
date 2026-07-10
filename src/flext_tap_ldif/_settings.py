"""Settings for FLEXT Tap LDIF — namespaced under ``settings.TapLdif``.

Universal fields via MRO; project fields in the ``TapLdif`` group with simple
scalar types (env-settable). Path derivation lives in consumers, not settings.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings


class FlextTapLdifSettings(FlextSettings):
    """Tap-LDIF runtime settings; fields under ``settings.TapLdif.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TAP_LDIF_",
        env_nested_delimiter="__",
        extra="ignore",
        validate_assignment=True,
    )

    class _TapLdif(BaseModel):
        """Namespaced tap-LDIF settings."""

        file_path: Annotated[str | None, Field(default=None, description="LDIF file path")]
        directory_path: Annotated[str | None, Field(default=None, description="LDIF directory path")]
        file_pattern: Annotated[str, Field(default="*.ldif", description="LDIF file glob pattern")]
        encoding: Annotated[str, Field(default="utf-8", description="File encoding")]
        strict_parsing: Annotated[bool, Field(default=True, description="Strict LDIF parsing")]
        max_file_size_mb: Annotated[int, Field(default=100, ge=1, description="Max file size (MB)")]

    if TYPE_CHECKING:
        TapLdif: _TapLdif
    else:
        TapLdif: _TapLdif = Field(
            default_factory=_TapLdif,
            description="Namespaced tap-LDIF settings.",
        )


settings: FlextTapLdifSettings = FlextTapLdifSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_tap_ldif import settings``."""

__all__: list[str] = ["FlextTapLdifSettings", "settings"]
