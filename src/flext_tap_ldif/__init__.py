# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

from flext_tap_ldif.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x

    from flext_tap_ldif import (
        _models,
        constants,
        models,
        protocols,
        settings,
        tap,
        typings,
        utilities,
    )
    from flext_tap_ldif._models import base, batch, config, entry, file, record
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.config import FlextTapLdifModelsConfig
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif.constants import (
        FlextTapLdifConstants,
        FlextTapLdifConstants as c,
    )
    from flext_tap_ldif.models import FlextTapLdifModels, FlextTapLdifModels as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols,
        FlextTapLdifProtocols as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif, logger, main
    from flext_tap_ldif.typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextTapLdif": ["flext_tap_ldif.tap", "FlextTapLdif"],
    "FlextTapLdifConstants": ["flext_tap_ldif.constants", "FlextTapLdifConstants"],
    "FlextTapLdifModels": ["flext_tap_ldif.models", "FlextTapLdifModels"],
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
    "FlextTapLdifProtocols": ["flext_tap_ldif.protocols", "FlextTapLdifProtocols"],
    "FlextTapLdifSettings": ["flext_tap_ldif.settings", "FlextTapLdifSettings"],
    "FlextTapLdifTypes": ["flext_tap_ldif.typings", "FlextTapLdifTypes"],
    "FlextTapLdifUtilities": ["flext_tap_ldif.utilities", "FlextTapLdifUtilities"],
    "_models": ["flext_tap_ldif._models", ""],
    "base": ["flext_tap_ldif._models.base", ""],
    "batch": ["flext_tap_ldif._models.batch", ""],
    "c": ["flext_tap_ldif.constants", "FlextTapLdifConstants"],
    "config": ["flext_tap_ldif._models.config", ""],
    "constants": ["flext_tap_ldif.constants", ""],
    "d": ["flext_ldif", "d"],
    "e": ["flext_ldif", "e"],
    "entry": ["flext_tap_ldif._models.entry", ""],
    "file": ["flext_tap_ldif._models.file", ""],
    "h": ["flext_ldif", "h"],
    "logger": ["flext_tap_ldif.tap", "logger"],
    "m": ["flext_tap_ldif.models", "FlextTapLdifModels"],
    "main": ["flext_tap_ldif.tap", "main"],
    "models": ["flext_tap_ldif.models", ""],
    "p": ["flext_tap_ldif.protocols", "FlextTapLdifProtocols"],
    "protocols": ["flext_tap_ldif.protocols", ""],
    "r": ["flext_ldif", "r"],
    "record": ["flext_tap_ldif._models.record", ""],
    "s": ["flext_ldif", "s"],
    "settings": ["flext_tap_ldif.settings", ""],
    "t": ["flext_tap_ldif.typings", "FlextTapLdifTypes"],
    "tap": ["flext_tap_ldif.tap", ""],
    "typings": ["flext_tap_ldif.typings", ""],
    "u": ["flext_tap_ldif.utilities", "FlextTapLdifUtilities"],
    "utilities": ["flext_tap_ldif.utilities", ""],
    "x": ["flext_ldif", "x"],
}

__all__ = [
    "FlextTapLdif",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifModelsBase",
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsConfig",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsRecord",
    "FlextTapLdifProtocols",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_models",
    "base",
    "batch",
    "c",
    "config",
    "constants",
    "d",
    "e",
    "entry",
    "file",
    "h",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "record",
    "s",
    "settings",
    "t",
    "tap",
    "typings",
    "u",
    "utilities",
    "x",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
