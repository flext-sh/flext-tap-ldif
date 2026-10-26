# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        config,
        d,
        e,
        h,
        install_local_packages,
        r,
        settings,
        td,
        tf,
        tk,
        tm,
        x,
    )

    from flext_tap_ldif import cli, ldif, main, meltano, tap_ldif
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
    "cli",
    "config",
    "d",
    "e",
    "h",
    "install_local_packages",
    "ldif",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "tap_ldif",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
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
        "cli": "flext_tap_ldif",
        "config": "flext_tests",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_local_packages": "flext_tests",
        "ldif": "flext_tap_ldif",
        "m": ".models",
        "main": "flext_tap_ldif",
        "meltano": "flext_tap_ldif",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tests",
        "t": ".typings",
        "tap_ldif": "flext_tap_ldif",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
