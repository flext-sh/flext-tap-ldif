# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .data_processing import (
        FlextTapLdifUtilitiesLdifDataProcessing as FlextTapLdifUtilitiesLdifDataProcessing,
    )
    from .entries_stream import (
        FlextTapLdifUtilitiesEntriesStream as FlextTapLdifUtilitiesEntriesStream,
    )
    from .processor import (
        FlextTapLdifUtilitiesProcessor as FlextTapLdifUtilitiesProcessor,
    )
    from .state_management import (
        FlextTapLdifUtilitiesStateManagement as FlextTapLdifUtilitiesStateManagement,
    )

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".data_processing": ("FlextTapLdifUtilitiesLdifDataProcessing",),
    ".entries_stream": ("FlextTapLdifUtilitiesEntriesStream",),
    ".processor": ("FlextTapLdifUtilitiesProcessor",),
    ".state_management": ("FlextTapLdifUtilitiesStateManagement",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTapLdifUtilitiesEntriesStream",
    "FlextTapLdifUtilitiesLdifDataProcessing",
    "FlextTapLdifUtilitiesProcessor",
    "FlextTapLdifUtilitiesStateManagement",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
