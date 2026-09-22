# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_ldif import ldif
    from flext_meltano import meltano
    from flext_tests import (
        active_rules,
        api,
        config,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        settings,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )

    from flext_core import core, d, e, h, lazy_attribute, r, x
    from flext_tap_ldif import main, tap_ldif

    from . import unit
    from .base import TestsFlextTapLdifServiceBase, TestsFlextTapLdifServiceBase as s
    from .constants import TestsFlextTapLdifConstants, TestsFlextTapLdifConstants as c
    from .models import TestsFlextTapLdifModels, TestsFlextTapLdifModels as m
    from .protocols import TestsFlextTapLdifProtocols, TestsFlextTapLdifProtocols as p
    from .settings import TestsFlextTapLdifSettings
    from .typings import TestsFlextTapLdifTypes, TestsFlextTapLdifTypes as t
    from .utilities import TestsFlextTapLdifUtilities, TestsFlextTapLdifUtilities as u


__all__: tuple[str, ...] = (
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifServiceBase",
    "TestsFlextTapLdifSettings",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "active_rules",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "discover_repository_root",
    "e",
    "h",
    "install_local_packages",
    "lazy_attribute",
    "ldif",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "tap_ldif",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTapLdifServiceBase", "s"),
            ".constants": ("TestsFlextTapLdifConstants", "c"),
            ".models": ("TestsFlextTapLdifModels", "m"),
            ".protocols": ("TestsFlextTapLdifProtocols", "p"),
            ".settings": ("TestsFlextTapLdifSettings",),
            ".typings": ("TestsFlextTapLdifTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTapLdifUtilities", "u"),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_ldif": ("ldif",),
            "flext_meltano": ("meltano",),
            "flext_tap_ldif": ("main", "tap_ldif"),
            "flext_tests": (
                "active_rules",
                "api",
                "config",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "settings",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
