# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

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
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".data_processing": ("FlextTapLdifUtilitiesLdifDataProcessing",),
        ".entries_stream": ("FlextTapLdifUtilitiesEntriesStream",),
        ".processor": ("FlextTapLdifUtilitiesProcessor",),
        ".state_management": ("FlextTapLdifUtilitiesStateManagement",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
