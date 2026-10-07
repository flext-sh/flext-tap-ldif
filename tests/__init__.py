# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from tests import unit
    from tests.base import TestsFlextTapLdifServiceBase, s
    from tests.constants import TestsFlextTapLdifConstants, c
    from tests.models import TestsFlextTapLdifModels, m
    from tests.protocols import TestsFlextTapLdifProtocols, p
    from tests.settings import TestsFlextTapLdifSettings
    from tests.typings import TestsFlextTapLdifTypes, t
    from tests.utilities import TestsFlextTapLdifUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifServiceBase",
    "TestsFlextTapLdifSettings",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "api",
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
    "u",
    "unit",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextTapLdifConstants": ".constants",
        "TestsFlextTapLdifModels": ".models",
        "TestsFlextTapLdifProtocols": ".protocols",
        "TestsFlextTapLdifServiceBase": ".base",
        "TestsFlextTapLdifSettings": ".settings",
        "TestsFlextTapLdifTypes": ".typings",
        "TestsFlextTapLdifUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "unit": ".unit",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
