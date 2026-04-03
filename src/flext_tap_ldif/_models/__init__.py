# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tap_ldif import base, batch, config, entry, file, record
    from flext_tap_ldif.base import FlextTapLdifModelsBase
    from flext_tap_ldif.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif.config import FlextTapLdifModelsConfig
    from flext_tap_ldif.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif.file import FlextTapLdifModelsFile
    from flext_tap_ldif.record import FlextTapLdifModelsRecord

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTapLdifModelsBase": "flext_tap_ldif.base",
    "FlextTapLdifModelsBatch": "flext_tap_ldif.batch",
    "FlextTapLdifModelsConfig": "flext_tap_ldif.config",
    "FlextTapLdifModelsEntry": "flext_tap_ldif.entry",
    "FlextTapLdifModelsFile": "flext_tap_ldif.file",
    "FlextTapLdifModelsRecord": "flext_tap_ldif.record",
    "base": "flext_tap_ldif.base",
    "batch": "flext_tap_ldif.batch",
    "config": "flext_tap_ldif.config",
    "entry": "flext_tap_ldif.entry",
    "file": "flext_tap_ldif.file",
    "record": "flext_tap_ldif.record",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
