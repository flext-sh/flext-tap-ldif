# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.file_metadata import FlextTapLdifModelsLdifFile
    from flext_tap_ldif._models.file_stream import FlextTapLdifModelsLdifStream
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif._models.settings import FlextTapLdifModelsSettings
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".batch": ("FlextTapLdifModelsBatch",),
        ".entry": ("FlextTapLdifModelsEntry",),
        ".file": ("FlextTapLdifModelsFile",),
        ".file_metadata": ("FlextTapLdifModelsLdifFile",),
        ".file_stream": ("FlextTapLdifModelsLdifStream",),
        ".record": ("FlextTapLdifModelsRecord",),
        ".settings": ("FlextTapLdifModelsSettings",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
