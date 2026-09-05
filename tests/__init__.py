# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_ldif import FlextTapLdifConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit as unit
    from .base import TestsFlextTapLdifServiceBase, TestsFlextTapLdifServiceBase as s
    from .constants import TestsFlextTapLdifConstants, TestsFlextTapLdifConstants as c
    from .models import TestsFlextTapLdifModels, TestsFlextTapLdifModels as m
    from .protocols import TestsFlextTapLdifProtocols, TestsFlextTapLdifProtocols as p
    from .settings import TestsFlextTapLdifSettings
    from .typings import TestsFlextTapLdifTypes, TestsFlextTapLdifTypes as t
    from .utilities import TestsFlextTapLdifUtilities, TestsFlextTapLdifUtilities as u
__all__: tuple[str, ...] = (
    "FlextTapLdifConstants",
    "FlextTestsConstants",
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifServiceBase",
    "TestsFlextTapLdifSettings",
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
            "flext_tap_ldif": ("FlextTapLdifConstants",),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
