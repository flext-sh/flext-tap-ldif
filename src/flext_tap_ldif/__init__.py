# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

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
    ("._models",),
    {
        "FlextTapLdif": ".tap",
        "FlextTapLdifCli": ".cli",
        "FlextTapLdifConstants": ".constants",
        "FlextTapLdifModels": ".models",
        "FlextTapLdifProtocols": ".protocols",
        "FlextTapLdifService": ".api",
        "FlextTapLdifSettings": ".settings",
        "FlextTapLdifTypes": ".typings",
        "FlextTapLdifUtilities": ".utilities",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version__": ".__version__",
        "__version_info__": ".__version__",
        "c": (".constants", "FlextTapLdifConstants"),
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": (".models", "FlextTapLdifModels"),
        "p": (".protocols", "FlextTapLdifProtocols"),
        "r": ("flext_core.result", "FlextResult"),
        "s": (".api", "FlextTapLdifService"),
        "t": (".typings", "FlextTapLdifTypes"),
        "u": (".utilities", "FlextTapLdifUtilities"),
        "x": ("flext_core.mixins", "FlextMixins"),
    },
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)

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
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
