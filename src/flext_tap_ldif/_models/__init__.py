# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal models subpackage for flext-tap-ldif."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif._models import (
        base as base,
        batch as batch,
        config as config,
        entry as entry,
        file as file,
        record as record,
    )
    from flext_tap_ldif._models.base import (
        FlextTapLdifModelsBase as FlextTapLdifModelsBase,
    )
    from flext_tap_ldif._models.batch import (
        FlextTapLdifModelsBatch as FlextTapLdifModelsBatch,
    )
    from flext_tap_ldif._models.config import (
        FlextTapLdifModelsConfig as FlextTapLdifModelsConfig,
    )
    from flext_tap_ldif._models.entry import (
        FlextTapLdifModelsEntry as FlextTapLdifModelsEntry,
    )
    from flext_tap_ldif._models.file import (
        FlextTapLdifModelsFile as FlextTapLdifModelsFile,
    )
    from flext_tap_ldif._models.record import (
        FlextTapLdifModelsRecord as FlextTapLdifModelsRecord,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTapLdifModelsBase": ["flext_tap_ldif._models.base", "FlextTapLdifModelsBase"],
    "FlextTapLdifModelsBatch": [
        "flext_tap_ldif._models.batch",
        "FlextTapLdifModelsBatch",
    ],
    "FlextTapLdifModelsConfig": [
        "flext_tap_ldif._models.config",
        "FlextTapLdifModelsConfig",
    ],
    "FlextTapLdifModelsEntry": [
        "flext_tap_ldif._models.entry",
        "FlextTapLdifModelsEntry",
    ],
    "FlextTapLdifModelsFile": ["flext_tap_ldif._models.file", "FlextTapLdifModelsFile"],
    "FlextTapLdifModelsRecord": [
        "flext_tap_ldif._models.record",
        "FlextTapLdifModelsRecord",
    ],
    "base": ["flext_tap_ldif._models.base", ""],
    "batch": ["flext_tap_ldif._models.batch", ""],
    "config": ["flext_tap_ldif._models.config", ""],
    "entry": ["flext_tap_ldif._models.entry", ""],
    "file": ["flext_tap_ldif._models.file", ""],
    "record": ["flext_tap_ldif._models.record", ""],
}

_EXPORTS: Sequence[str] = [
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
