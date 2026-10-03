# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.file_metadata import FlextTapLdifModelsLdifFile
    from flext_tap_ldif._models.file_stream import FlextTapLdifModelsFileStream
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif._models.settings import FlextTapLdifModelsSettings


__all__: tuple[str, ...] = (
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsFileStream",
    "FlextTapLdifModelsLdifFile",
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
            ".file_stream": ("FlextTapLdifModelsFileStream",),
            ".record": ("FlextTapLdifModelsRecord",),
            ".settings": ("FlextTapLdifModelsSettings",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
