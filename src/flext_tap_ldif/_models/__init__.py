# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.config import FlextTapLdifModelsConfig


__all__: tuple[str, ...] = ("FlextTapLdifModelsBase", "FlextTapLdifModelsConfig")

install_lazy_exports(
    __name__,
    globals(),
    {"FlextTapLdifModelsBase": ".base", "FlextTapLdifModelsConfig": ".config"},
    public_exports=__all__,
)
