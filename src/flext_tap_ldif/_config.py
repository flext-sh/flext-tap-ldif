"""FlextTapLdifConfig — frozen, validated config singleton for flext-tap-ldif.

Every ``config/*.yaml`` file is auto-discovered and deep-merged at first
``fetch_global`` call (model-less, ``extra="allow"`` at the FlextMeltanoConfig base).
The flat YAML is then validated into the pure-Pydantic ``_models.config``
shapes and exposed as typed domain objects under ``config.TapLdif`` — never a
model-less dict subscript.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import ClassVar

from flext_meltano import FlextMeltanoConfig
from flext_tap_ldif._models.config import FlextTapLdifConfigModels


class FlextTapLdifConfig(FlextMeltanoConfig):
    """TapLdif config auto-loaded from ``config/*.yaml`` and validated via models."""

    CONFIG_DIR: ClassVar[str] = str(
        Path(__file__).resolve().parents[2] / "config",
    )

    @cached_property
    def TapLdif(self) -> FlextTapLdifConfigModels.TapLdif:
        """Validated ``TapLdif`` business-rule config namespace."""
        root = FlextTapLdifConfigModels.Root.model_validate(
            dict(self.model_extra or {}),
        )
        return root.TapLdif


config: FlextTapLdifConfig = FlextTapLdifConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_ldif import config``."""

__all__: list[str] = ["FlextTapLdifConfig", "config"]
