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
    from flext_tests import td as td, tf as tf, tk as tk, tv as tv

    from flext_tap_ldif import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextTapLdifServiceBase as TestsFlextTapLdifServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextTapLdifConstants as TestsFlextTapLdifConstants,
        c as c,
    )
    from tests.models import TestsFlextTapLdifModels as TestsFlextTapLdifModels, m as m
    from tests.protocols import (
        TestsFlextTapLdifProtocols as TestsFlextTapLdifProtocols,
        p as p,
    )
    from tests.settings import TestsFlextTapLdifSettings as TestsFlextTapLdifSettings
    from tests.typings import TestsFlextTapLdifTypes as TestsFlextTapLdifTypes, t as t
    from tests.unit.test_tap import TestsFlextTapLdifTap as TestsFlextTapLdifTap
    from tests.utilities import (
        TestsFlextTapLdifUtilities as TestsFlextTapLdifUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextTapLdifServiceBase",
                "s",
            ),
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
            ".settings": ("TestsFlextTapLdifSettings",),
            ".typings": (
                "TestsFlextTapLdifTypes",
                "t",
            ),
            ".unit.test_tap": ("TestsFlextTapLdifTap",),
            ".utilities": (
                "TestsFlextTapLdifUtilities",
                "u",
            ),
            "flext_tap_ldif": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifServiceBase",
    "TestsFlextTapLdifSettings",
    "TestsFlextTapLdifTap",
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
    "tv",
    "u",
    "x",
]
