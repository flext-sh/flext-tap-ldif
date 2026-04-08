# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_tap_ldif.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.config import FlextTapLdifModelsSettings
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif.api import FlextTapLdifService, FlextTapLdifService as s
    from flext_tap_ldif.cli import FlextTapLdifCli, main
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
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextTapLdifService",),
            ".cli": (
                "FlextTapLdifCli",
                "main",
            ),
            ".constants": ("FlextTapLdifConstants",),
            ".models": ("FlextTapLdifModels",),
            ".protocols": ("FlextTapLdifProtocols",),
            ".settings": ("FlextTapLdifSettings",),
            ".tap": ("FlextTapLdif",),
            ".typings": ("FlextTapLdifTypes",),
            ".utilities": ("FlextTapLdifUtilities",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
        },
        alias_groups={
            ".api": (("s", "FlextTapLdifService"),),
            ".constants": (("c", "FlextTapLdifConstants"),),
            ".models": (("m", "FlextTapLdifModels"),),
            ".protocols": (("p", "FlextTapLdifProtocols"),),
            ".typings": (("t", "FlextTapLdifTypes"),),
            ".utilities": (("u", "FlextTapLdifUtilities"),),
        },
    ),
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
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsRecord",
    "FlextTapLdifModelsSettings",
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
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
