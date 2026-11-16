# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._utilities.base import FlextTapLdifUtilitiesBase
    from flext_tap_ldif._utilities.extract_support import (
        FlextTapLdifUtilitiesExtractSupport,
    )


__all__: tuple[str, ...] = (
    "FlextTapLdifUtilitiesBase",
    "FlextTapLdifUtilitiesExtractSupport",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTapLdifUtilitiesBase": ".base",
        "FlextTapLdifUtilitiesExtractSupport": ".extract_support",
    },
    public_exports=__all__,
    deferred_members={
        "FlextTapLdifUtilitiesExtractSupport": (
            "logger",
            "tap_ldif",
            "tap_spec",
            "_resolve_single_file",
            "_resolve_dir_files",
            "resolve_files",
            "pack_entry",
        ),
    },
)
