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

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x

    from flext_tap_ldif.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
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
        FlextLdifProcessor,
        FlextTapLdifEntriesStream,
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextLdifProcessor": ["flext_tap_ldif.utilities", "FlextLdifProcessor"],
    "FlextTapLdif": ["flext_tap_ldif.tap", "FlextTapLdif"],
    "FlextTapLdifConstants": ["flext_tap_ldif.constants", "FlextTapLdifConstants"],
    "FlextTapLdifEntriesStream": [
        "flext_tap_ldif.utilities",
        "FlextTapLdifEntriesStream",
    ],
    "FlextTapLdifModels": ["flext_tap_ldif.models", "FlextTapLdifModels"],
    "FlextTapLdifProtocols": ["flext_tap_ldif.protocols", "FlextTapLdifProtocols"],
    "FlextTapLdifSettings": ["flext_tap_ldif.settings", "FlextTapLdifSettings"],
    "FlextTapLdifTypes": ["flext_tap_ldif.typings", "FlextTapLdifTypes"],
    "FlextTapLdifUtilities": ["flext_tap_ldif.utilities", "FlextTapLdifUtilities"],
    "__all__": ["flext_tap_ldif.__version__", "__all__"],
    "__author__": ["flext_tap_ldif.__version__", "__author__"],
    "__author_email__": ["flext_tap_ldif.__version__", "__author_email__"],
    "__description__": ["flext_tap_ldif.__version__", "__description__"],
    "__license__": ["flext_tap_ldif.__version__", "__license__"],
    "__title__": ["flext_tap_ldif.__version__", "__title__"],
    "__url__": ["flext_tap_ldif.__version__", "__url__"],
    "__version__": ["flext_tap_ldif.__version__", "__version__"],
    "__version_info__": ["flext_tap_ldif.__version__", "__version_info__"],
    "c": ["flext_tap_ldif.constants", "FlextTapLdifConstants"],
    "d": ["flext_ldif", "d"],
    "e": ["flext_ldif", "e"],
    "h": ["flext_ldif", "h"],
    "logger": ["flext_tap_ldif.tap", "logger"],
    "m": ["flext_tap_ldif.models", "FlextTapLdifModels"],
    "main": ["flext_tap_ldif.tap", "main"],
    "p": ["flext_tap_ldif.protocols", "FlextTapLdifProtocols"],
    "r": ["flext_ldif", "r"],
    "s": ["flext_ldif", "s"],
    "t": ["flext_tap_ldif.typings", "FlextTapLdifTypes"],
    "u": ["flext_tap_ldif.utilities", "FlextTapLdifUtilities"],
    "x": ["flext_ldif", "x"],
}

__all__ = [
    "FlextLdifProcessor",
    "FlextTapLdif",
    "FlextTapLdifConstants",
    "FlextTapLdifEntriesStream",
    "FlextTapLdifModels",
    "FlextTapLdifProtocols",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "logger",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
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
