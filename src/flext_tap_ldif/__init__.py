# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_tap_ldif.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_tap_ldif import (
        _models,
        api,
        cli,
        constants,
        models,
        protocols,
        settings,
        tap,
        typings,
        utilities,
    )
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.config import FlextTapLdifModelsConfig
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif.api import FlextTapLdifService, FlextTapLdifService as s
    from flext_tap_ldif.cli import FlextTapLdifCli
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
    from flext_tap_ldif.tap import FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_tap_ldif._models",),
    {
        "FlextTapLdif": ("flext_tap_ldif.tap", "FlextTapLdif"),
        "FlextTapLdifCli": ("flext_tap_ldif.cli", "FlextTapLdifCli"),
        "FlextTapLdifConstants": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
        "FlextTapLdifModels": ("flext_tap_ldif.models", "FlextTapLdifModels"),
        "FlextTapLdifProtocols": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
        "FlextTapLdifService": ("flext_tap_ldif.api", "FlextTapLdifService"),
        "FlextTapLdifSettings": ("flext_tap_ldif.settings", "FlextTapLdifSettings"),
        "FlextTapLdifTypes": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
        "FlextTapLdifUtilities": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
        "__author__": ("flext_tap_ldif.__version__", "__author__"),
        "__author_email__": ("flext_tap_ldif.__version__", "__author_email__"),
        "__description__": ("flext_tap_ldif.__version__", "__description__"),
        "__license__": ("flext_tap_ldif.__version__", "__license__"),
        "__title__": ("flext_tap_ldif.__version__", "__title__"),
        "__url__": ("flext_tap_ldif.__version__", "__url__"),
        "__version__": ("flext_tap_ldif.__version__", "__version__"),
        "__version_info__": ("flext_tap_ldif.__version__", "__version_info__"),
        "_models": "flext_tap_ldif._models",
        "api": "flext_tap_ldif.api",
        "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
        "cli": "flext_tap_ldif.cli",
        "constants": "flext_tap_ldif.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
        "models": "flext_tap_ldif.models",
        "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
        "protocols": "flext_tap_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_tap_ldif.api", "FlextTapLdifService"),
        "settings": "flext_tap_ldif.settings",
        "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
        "tap": "flext_tap_ldif.tap",
        "typings": "flext_tap_ldif.typings",
        "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
        "utilities": "flext_tap_ldif.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "FlextTapLdif",
    "FlextTapLdifCli",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifModelsBase",
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsConfig",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsRecord",
    "FlextTapLdifProtocols",
    "FlextTapLdifService",
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
    "api",
    "c",
    "cli",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "t",
    "tap",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
