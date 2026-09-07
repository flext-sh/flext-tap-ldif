# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Utilities package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .data_processing import FlextTapLdifUtilitiesLdifDataProcessing
    from .entries_stream import FlextTapLdifUtilitiesEntriesStream
    from .processor import FlextTapLdifUtilitiesProcessor
    from .state_management import FlextTapLdifUtilitiesStateManagement
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
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
