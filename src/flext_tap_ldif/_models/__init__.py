# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .batch import FlextTapLdifModelsBatch as FlextTapLdifModelsBatch
    from .entry import FlextTapLdifModelsEntry as FlextTapLdifModelsEntry
    from .file import FlextTapLdifModelsFile as FlextTapLdifModelsFile
    from .file_metadata import FlextTapLdifModelsLdifFile as FlextTapLdifModelsLdifFile
    from .file_stream import (
        FlextTapLdifModelsLdifStream as FlextTapLdifModelsLdifStream,
    )
    from .record import FlextTapLdifModelsRecord as FlextTapLdifModelsRecord
    from .settings import FlextTapLdifModelsSettings as FlextTapLdifModelsSettings

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".batch": ("FlextTapLdifModelsBatch",),
    ".entry": ("FlextTapLdifModelsEntry",),
    ".file": ("FlextTapLdifModelsFile",),
    ".file_metadata": ("FlextTapLdifModelsLdifFile",),
    ".file_stream": ("FlextTapLdifModelsLdifStream",),
    ".record": ("FlextTapLdifModelsRecord",),
    ".settings": ("FlextTapLdifModelsSettings",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsLdifFile",
    "FlextTapLdifModelsLdifStream",
    "FlextTapLdifModelsRecord",
    "FlextTapLdifModelsSettings",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
