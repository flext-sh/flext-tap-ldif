# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._utilities.entries_stream import (
        FlextTapLdifUtilitiesEntriesStream,
    )
    from flext_tap_ldif._utilities.processor import FlextTapLdifUtilitiesProcessor


__all__: tuple[str, ...] = (
    "FlextTapLdifUtilitiesEntriesStream",
    "FlextTapLdifUtilitiesProcessor",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapLdifUtilitiesEntriesStream": ".entries_stream",
        "FlextTapLdifUtilitiesProcessor": ".processor",
    }),
    public_exports=__all__,
)
