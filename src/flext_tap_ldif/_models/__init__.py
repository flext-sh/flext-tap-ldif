# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_tap_ldif._models.base as _flext_tap_ldif__models_base

    base = _flext_tap_ldif__models_base
    import flext_tap_ldif._models.batch as _flext_tap_ldif__models_batch
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase

    batch = _flext_tap_ldif__models_batch
    import flext_tap_ldif._models.config as _flext_tap_ldif__models_config
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch

    config = _flext_tap_ldif__models_config
    import flext_tap_ldif._models.entry as _flext_tap_ldif__models_entry
    from flext_tap_ldif._models.config import FlextTapLdifModelsConfig

    entry = _flext_tap_ldif__models_entry
    import flext_tap_ldif._models.file as _flext_tap_ldif__models_file
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry

    file = _flext_tap_ldif__models_file
    import flext_tap_ldif._models.record as _flext_tap_ldif__models_record
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile

    record = _flext_tap_ldif__models_record
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
_LAZY_IMPORTS = {
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

__all__ = [
    "FlextTapLdifModelsBase",
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsConfig",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsRecord",
    "base",
    "batch",
    "config",
    "entry",
    "file",
    "record",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
