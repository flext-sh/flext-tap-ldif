# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_tap_ldif import d, e, h, r, s, x
    from tests.constants import TestsFlextTapLdifConstants, c
    from tests.models import TestsFlextTapLdifModels, m
    from tests.protocols import TestsFlextTapLdifProtocols, p
    from tests.typings import TestsFlextTapLdifTypes, t
    from tests.utilities import TestsFlextTapLdifUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTapLdifConstants",
                "c",
            ),
            ".models": (
                "TestsFlextTapLdifModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTapLdifProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextTapLdifTypes",
                "t",
            ),
            ".utilities": (
                "TestsFlextTapLdifUtilities",
                "u",
            ),
            "flext_tap_ldif": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
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

__all__ = [
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
]
