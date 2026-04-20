"""Configuration for FLEXT Tap LDIF using FlextSettings patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, ClassVar

from flext_core import FlextSettings

from flext_tap_ldif import c, u
from flext_tap_ldif.models import m


@FlextSettings.auto_register("tap-ldif")
class FlextTapLdifSettings(FlextSettings):
    """Validated runtime settings for tap-ldif execution."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TAP_LDIF_", extra="ignore", validate_assignment=True
    )

    file_path: Annotated[str | None, u.Field(default=None)]
    directory_path: Annotated[str | None, u.Field(default=None)]
    file_pattern: Annotated[
        str,
        u.Field(default=c.TapLdif.DEFAULT_FILE_PATTERN),
    ]
    encoding: Annotated[
        str,
        u.Field(default=c.TapLdif.DEFAULT_LDIF_ENCODING),
    ]
    strict_parsing: Annotated[
        bool,
        u.Field(default=c.TapLdif.DEFAULT_STRICT_PARSING),
    ]
    max_file_size_mb: Annotated[
        int,
        u.Field(default=c.TapLdif.MAX_FILE_SIZE_MB, ge=1),
    ]

    def normalized_file_path(self) -> Path | None:
        """Return `file_path` as `Path` when configured."""
        if self.file_path is None:
            return None
        return Path(self.file_path)


__all__: list[str] = ["FlextTapLdifSettings"]
