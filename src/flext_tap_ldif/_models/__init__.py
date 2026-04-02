# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal models subpackage for flext-tap-ldif."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tap_ldif._models import base, batch, config, entry, file, record
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.config import FlextTapLdifModelsConfig
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTapLdifModelsBase": "flext_tap_ldif._models.base",
    "FlextTapLdifModelsBatch": "flext_tap_ldif._models.batch",
    "FlextTapLdifModelsConfig": "flext_tap_ldif._models.config",
    "FlextTapLdifModelsEntry": "flext_tap_ldif._models.entry",
    "FlextTapLdifModelsFile": "flext_tap_ldif._models.file",
    "FlextTapLdifModelsRecord": "flext_tap_ldif._models.record",
    "base": "flext_tap_ldif._models.base",
    "batch": "flext_tap_ldif._models.batch",
    "config": "flext_tap_ldif._models.config",
    "entry": "flext_tap_ldif._models.entry",
    "file": "flext_tap_ldif._models.file",
    "record": "flext_tap_ldif._models.record",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
