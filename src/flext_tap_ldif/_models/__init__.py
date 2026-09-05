# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Models package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .batch import FlextTapLdifModelsBatch
    from .entry import FlextTapLdifModelsEntry
    from .file import FlextTapLdifModelsFile
    from .file_metadata import FlextTapLdifModelsLdifFile
    from .file_stream import FlextTapLdifModelsLdifStream
    from .record import FlextTapLdifModelsRecord
    from .settings import FlextTapLdifModelsSettings
__all__: tuple[str, ...] = (
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsLdifFile",
    "FlextTapLdifModelsLdifStream",
    "FlextTapLdifModelsRecord",
    "FlextTapLdifModelsSettings",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".batch": ("FlextTapLdifModelsBatch",),
            ".entry": ("FlextTapLdifModelsEntry",),
            ".file": ("FlextTapLdifModelsFile",),
            ".file_metadata": ("FlextTapLdifModelsLdifFile",),
            ".file_stream": ("FlextTapLdifModelsLdifStream",),
            ".record": ("FlextTapLdifModelsRecord",),
            ".settings": ("FlextTapLdifModelsSettings",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
