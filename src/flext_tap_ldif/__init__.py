# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
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

if _t.TYPE_CHECKING:
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_tap_ldif._models.batch import (
        FlextTapLdifModelsBatch as FlextTapLdifModelsBatch,
    )
    from flext_tap_ldif._models.entry import (
        FlextTapLdifModelsEntry as FlextTapLdifModelsEntry,
    )
    from flext_tap_ldif._models.file import (
        FlextTapLdifModelsFile as FlextTapLdifModelsFile,
    )
    from flext_tap_ldif._models.record import (
        FlextTapLdifModelsRecord as FlextTapLdifModelsRecord,
    )
    from flext_tap_ldif._models.settings import (
        FlextTapLdifModelsSettings as FlextTapLdifModelsSettings,
    )
    from flext_tap_ldif.api import (
        FlextTapLdifService as FlextTapLdifService,
        tap_ldif as tap_ldif,
    )
    from flext_tap_ldif.cli import FlextTapLdifCli as FlextTapLdifCli, main as main
    from flext_tap_ldif.constants import (
        FlextTapLdifConstants as FlextTapLdifConstants,
        c as c,
    )
    from flext_tap_ldif.models import FlextTapLdifModels as FlextTapLdifModels, m as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols as FlextTapLdifProtocols,
        p as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings as FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif as FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes as FlextTapLdifTypes, t as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities as FlextTapLdifUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("._models",),
    build_lazy_import_map(
        {
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
            "flext_meltano": (
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
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)

__all__: list[str] = [
    "FlextTapLdif",
    "FlextTapLdifCli",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
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
