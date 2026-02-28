"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextLogger, FlextModels, FlextResult

    from flext_tap_ldif.__version__ import __version__, __version_info__
    from flext_tap_ldif.constants import (
        FlextMeltanoTapLdifConstants,
        FlextMeltanoTapLdifConstants as c,
    )
    from flext_tap_ldif.ldif_processor import (
        FlextLdifProcessor,
        LDIFProcessor,
    )
    from flext_tap_ldif.models import (
        FlextMeltanoTapLdifModels,
        FlextMeltanoTapLdifModels as m,
    )
    from flext_tap_ldif.protocols import FlextMeltanoTapLdifProtocols
    from flext_tap_ldif.settings import (
        FlextMeltanoTapLdifSettings,
    )
    from flext_tap_ldif.streams import LDIFEntriesStream
    from flext_tap_ldif.tap import TapLDIF
    from flext_tap_ldif.typings import t
    from flext_tap_ldif.utilities import (
        FlextMeltanoTapLdifUtilities,
        FlextMeltanoTapLdifUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLdifProcessor": ("flext_tap_ldif.ldif_processor", "FlextLdifProcessor"),
    "FlextLogger": ("flext_core", "FlextLogger"),
    "FlextMeltanoTapLdifConstants": (
        "flext_tap_ldif.constants",
        "FlextMeltanoTapLdifConstants",
    ),
    "FlextMeltanoTapLdifModels": ("flext_tap_ldif.models", "FlextMeltanoTapLdifModels"),
    "FlextMeltanoTapLdifProtocols": (
        "flext_tap_ldif.protocols",
        "FlextMeltanoTapLdifProtocols",
    ),
    "FlextMeltanoTapLdifSettings": (
        "flext_tap_ldif.settings",
        "FlextMeltanoTapLdifSettings",
    ),
    "FlextMeltanoTapLdifUtilities": (
        "flext_tap_ldif.utilities",
        "FlextMeltanoTapLdifUtilities",
    ),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
    "LDIFEntriesStream": ("flext_tap_ldif.streams", "LDIFEntriesStream"),
    "LDIFProcessor": ("flext_tap_ldif.ldif_processor", "LDIFProcessor"),
    "TapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "__version__": ("flext_tap_ldif.__version__", "__version__"),
    "__version_info__": ("flext_tap_ldif.__version__", "__version_info__"),
    "c": ("flext_tap_ldif.constants", "FlextMeltanoTapLdifConstants"),
    "m": ("flext_tap_ldif.models", "FlextMeltanoTapLdifModels"),
    "t": ("flext_tap_ldif.typings", "t"),
    "u": ("flext_tap_ldif.utilities", "u"),
}

__all__ = [
    "FlextLdifProcessor",
    "FlextLogger",
    "FlextMeltanoTapLdifConstants",
    "FlextMeltanoTapLdifModels",
    "FlextMeltanoTapLdifProtocols",
    "FlextMeltanoTapLdifSettings",
    "FlextMeltanoTapLdifUtilities",
    "FlextModels",
    "FlextResult",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "TapLDIF",
    "__version__",
    "__version_info__",
    "c",
    "m",
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
