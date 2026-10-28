# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.config import FlextTapLdifConfigModels


__all__: tuple[str, ...] = (
    "FlextTapLdifConfigModels",
    "FlextTapLdifModelsBase",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapLdifConfigModels": ".config",
        "FlextTapLdifModelsBase": ".base",
    }),
    public_exports=__all__,
)
