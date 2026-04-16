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
    from flext_ldif import d, e, h, r, s, x
    from flext_tap_ldif._models.base import FlextTapLdifModelsBase
    from flext_tap_ldif._models.batch import FlextTapLdifModelsBatch
    from flext_tap_ldif._models.entry import FlextTapLdifModelsEntry
    from flext_tap_ldif._models.file import FlextTapLdifModelsFile
    from flext_tap_ldif._models.record import FlextTapLdifModelsRecord
    from flext_tap_ldif._models.settings import FlextTapLdifModelsSettings
    from flext_tap_ldif.api import FlextTapLdifService, tap_ldif
    from flext_tap_ldif.cli import FlextTapLdifCli, main
    from flext_tap_ldif.constants import FlextTapLdifConstants, c
    from flext_tap_ldif.models import FlextTapLdifModels, m
    from flext_tap_ldif.protocols import FlextTapLdifProtocols, p
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes, t
    from flext_tap_ldif.utilities import FlextTapLdifUtilities, u
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
            "._models.base": ("FlextTapLdifModelsBase",),
            "._models.batch": ("FlextTapLdifModelsBatch",),
            "._models.entry": ("FlextTapLdifModelsEntry",),
            "._models.file": ("FlextTapLdifModelsFile",),
            "._models.record": ("FlextTapLdifModelsRecord",),
            "._models.settings": ("FlextTapLdifModelsSettings",),
            ".api": (
                "FlextTapLdifService",
                "tap_ldif",
            ),
            ".cli": (
                "FlextTapLdifCli",
                "main",
            ),
            ".constants": (
                "FlextTapLdifConstants",
                "c",
            ),
            ".models": (
                "FlextTapLdifModels",
                "m",
            ),
            ".protocols": (
                "FlextTapLdifProtocols",
                "p",
            ),
            ".settings": ("FlextTapLdifSettings",),
            ".tap": ("FlextTapLdif",),
            ".typings": (
                "FlextTapLdifTypes",
                "t",
            ),
            ".utilities": (
                "FlextTapLdifUtilities",
                "u",
            ),
            "flext_ldif": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
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
    "tap_ldif",
    "u",
    "x",
]
