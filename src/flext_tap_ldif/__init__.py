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
        FlextLdifProcessorWrapper,
        LDIFProcessor,
    )
    from flext_tap_ldif.models import (
        FlextMeltanoTapLdifModels,
        FlextMeltanoTapLdifModels as m,
    )
    from flext_tap_ldif.protocols import FlextMeltanoTapLdifProtocols
    from flext_tap_ldif.settings import (
        FlextMeltanoTapLdifSettings,
        FlextMeltanoTapLdifSettings as FlextMeltanoTapLDIFSettings,
        FlextMeltanoTapLdifSettings as TapConfig,
        FlextMeltanoTapLdifSettings as TapLDIFConfig,
    )
    from flext_tap_ldif.streams import LDIFEntriesStream
    from flext_tap_ldif.tap import (
        TapLDIF,
        TapLDIF as FlextMeltanoTapLDIF,
        TapLDIF as LDIFTap,
        TapLDIF as LegacyTapLDIF,
    )
    from flext_tap_ldif.typings import t
    from flext_tap_ldif.utilities import (
        FlextMeltanoTapLdifUtilities,
        FlextTapLdifUtilities,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLdifProcessor": ("flext_tap_ldif.ldif_processor", "FlextLdifProcessor"),
    "FlextLdifProcessorWrapper": (
        "flext_tap_ldif.ldif_processor",
        "FlextLdifProcessorWrapper",
    ),
    "FlextLogger": ("flext_core", "FlextLogger"),
    "FlextMeltanoTapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "FlextMeltanoTapLDIFSettings": (
        "flext_tap_ldif.settings",
        "FlextMeltanoTapLdifSettings",
    ),
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
    "FlextTapLdifUtilities": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
    "LDIFEntriesStream": ("flext_tap_ldif.streams", "LDIFEntriesStream"),
    "LDIFProcessor": ("flext_tap_ldif.ldif_processor", "LDIFProcessor"),
    "LDIFTap": ("flext_tap_ldif.tap", "TapLDIF"),
    "LegacyTapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "TapConfig": ("flext_tap_ldif.settings", "FlextMeltanoTapLdifSettings"),
    "TapLDIF": ("flext_tap_ldif.tap", "TapLDIF"),
    "TapLDIFConfig": ("flext_tap_ldif.settings", "FlextMeltanoTapLdifSettings"),
    "__version__": ("flext_tap_ldif.__version__", "__version__"),
    "__version_info__": ("flext_tap_ldif.__version__", "__version_info__"),
    "c": ("flext_tap_ldif.constants", "FlextMeltanoTapLdifConstants"),
    "m": ("flext_tap_ldif.models", "FlextMeltanoTapLdifModels"),
    "t": ("flext_tap_ldif.typings", "t"),
    "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
}

__all__ = [
    "FlextLdifProcessor",
    "FlextLdifProcessorWrapper",
    "FlextLogger",
    "FlextMeltanoTapLDIF",
    "FlextMeltanoTapLDIFSettings",
    "FlextMeltanoTapLdifConstants",
    "FlextMeltanoTapLdifModels",
    "FlextMeltanoTapLdifProtocols",
    "FlextMeltanoTapLdifSettings",
    "FlextMeltanoTapLdifUtilities",
    "FlextModels",
    "FlextResult",
    "FlextTapLdifUtilities",
    "LDIFEntriesStream",
    "LDIFProcessor",
    "LDIFTap",
    "LegacyTapLDIF",
    "TapConfig",
    "TapLDIF",
    "TapLDIFConfig",
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
