# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import d, e, h, r, s, x
    from flext_core.typings import FlextTypes

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
    from flext_tap_ldif.ldif_processor import FlextLdifProcessor
    from flext_tap_ldif.models import FlextTapLdifModels, FlextTapLdifModels as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols,
        FlextTapLdifProtocols as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.streams import LDIFEntriesStream
    from flext_tap_ldif.tap import TapLDIF, logger, main
    from flext_tap_ldif.typings import (
        FlextTapLdifTypes,
        FlextTapLdifTypes as t,
        StreamRecordValue,
    )
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLdifProcessor": ("flext_tap_ldif.ldif_processor", "FlextLdifProcessor"),
    "FlextTapLdifConstants": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
    "FlextTapLdifModels": ("flext_tap_ldif.models", "FlextTapLdifModels"),
    "FlextTapLdifProtocols": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
    "FlextTapLdifSettings": ("flext_tap_ldif.settings", "FlextTapLdifSettings"),
    "FlextTapLdifTypes": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
    "FlextTapLdifUtilities": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
    "LDIFEntriesStream": ("flext_tap_ldif.streams", "LDIFEntriesStream"),
    "StreamRecordValue": ("flext_tap_ldif.typings", "StreamRecordValue"),
    "TapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "__all__": ("flext_tap_ldif.__version__", "__all__"),
    "__author__": ("flext_tap_ldif.__version__", "__author__"),
    "__author_email__": ("flext_tap_ldif.__version__", "__author_email__"),
    "__description__": ("flext_tap_ldif.__version__", "__description__"),
    "__license__": ("flext_tap_ldif.__version__", "__license__"),
    "__title__": ("flext_tap_ldif.__version__", "__title__"),
    "__url__": ("flext_tap_ldif.__version__", "__url__"),
    "__version__": ("flext_tap_ldif.__version__", "__version__"),
    "__version_info__": ("flext_tap_ldif.__version__", "__version_info__"),
    "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
    "d": ("flext_core", "d"),
    "e": ("flext_core", "e"),
    "h": ("flext_core", "h"),
    "logger": ("flext_tap_ldif.tap", "logger"),
    "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
    "main": ("flext_tap_ldif.tap", "main"),
    "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
    "r": ("flext_core", "r"),
    "s": ("flext_core", "s"),
    "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
    "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
    "x": ("flext_core", "x"),
}

__all__ = [
    "FlextLdifProcessor",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifProtocols",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "LDIFEntriesStream",
    "StreamRecordValue",
    "TapLDIF",
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


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
