# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Utilities package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._utilities.data_processing import (
        FlextTapLdifUtilitiesLdifDataProcessing,
    )
    from flext_tap_ldif._utilities.entries_stream import (
        FlextTapLdifUtilitiesEntriesStream,
    )
    from flext_tap_ldif._utilities.processor import FlextTapLdifUtilitiesProcessor
    from flext_tap_ldif._utilities.state_management import (
        FlextTapLdifUtilitiesStateManagement,
    )


__all__: tuple[str, ...] = (
    "FlextTapLdifUtilitiesEntriesStream",
    "FlextTapLdifUtilitiesLdifDataProcessing",
    "FlextTapLdifUtilitiesProcessor",
    "FlextTapLdifUtilitiesStateManagement",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".data_processing": ("FlextTapLdifUtilitiesLdifDataProcessing",),
            ".entries_stream": ("FlextTapLdifUtilitiesEntriesStream",),
            ".processor": ("FlextTapLdifUtilitiesProcessor",),
            ".state_management": ("FlextTapLdifUtilitiesStateManagement",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
