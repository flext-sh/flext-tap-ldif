"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core._utilities.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextLogger, FlextModels, FlextResult

    from flext_tap_ldif.__version__ import __version__, __version_info__
    from flext_tap_ldif.constants import (
        FlextTapLdifConstants,
        FlextTapLdifConstants as c,
    )
    from flext_tap_ldif.ldif_processor import FlextLdifProcessor, LDIFProcessor
    from flext_tap_ldif.models import FlextTapLdifModels, FlextTapLdifModels as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols,
        FlextTapLdifProtocols as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.streams import LDIFEntriesStream
    from flext_tap_ldif.tap import TapLDIF
    from flext_tap_ldif.typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLdifProcessor": ("flext_tap_ldif.ldif_processor", "FlextLdifProcessor"),
    "FlextLogger": ("flext_core", "FlextLogger"),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
    "FlextTapLdifConstants": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
    "FlextTapLdifModels": ("flext_tap_ldif.models", "FlextTapLdifModels"),
    "FlextTapLdifProtocols": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
    "FlextTapLdifSettings": ("flext_tap_ldif.settings", "FlextTapLdifSettings"),
    "FlextTapLdifTypes": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
    "FlextTapLdifUtilities": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
    "LDIFEntriesStream": ("flext_tap_ldif.streams", "LDIFEntriesStream"),
    "LDIFProcessor": ("flext_tap_ldif.ldif_processor", "LDIFProcessor"),
    "TapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "__version__": ("flext_tap_ldif.__version__", "__version__"),
    "__version_info__": ("flext_tap_ldif.__version__", "__version_info__"),
    "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
    "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
    "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
    "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
    "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
}

__all__ = [
    "FlextLdifProcessor",
    "FlextLogger",
    "FlextModels",
    "FlextResult",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifProtocols",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "TapLDIF",
    "__version__",
    "__version_info__",
    "c",
    "m",
    "p",
    "t",
    "u",
]


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
