# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._protocols.config import FlextTapLdifProtocolsConfig


__all__: tuple[str, ...] = ("FlextTapLdifProtocolsConfig",)

install_lazy_exports(
    __name__,
    globals(),
    {"FlextTapLdifProtocolsConfig": ".config"},
    public_exports=__all__,
)
