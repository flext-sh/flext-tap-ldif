"""Configuration for FLEXT Tap LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, ClassVar

from pydantic import BaseModel, ConfigDict, Field


class FlextTapLdifSettings(BaseModel):
    """Validated runtime settings for tap-ldif execution."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        extra="ignore",
        validate_assignment=True,
    )

    file_path: Annotated[str | None, Field(default=None)]
    directory_path: Annotated[str | None, Field(default=None)]
    file_pattern: Annotated[str, Field(default="*.ldif")]
    encoding: Annotated[str, Field(default="utf-8")]
    strict_parsing: Annotated[bool, Field(default=True)]
    max_file_size_mb: Annotated[int, Field(default=100, ge=1)]

    def normalized_file_path(self) -> Path | None:
        """Return `file_path` as `Path` when configured."""
        if self.file_path is None:
            return None
        return Path(self.file_path)


__all__ = ["FlextTapLdifSettings"]
