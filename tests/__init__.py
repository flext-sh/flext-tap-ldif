# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_tap_ldif import (
        FlextTapLdifCli,
        FlextTapLdifConfig,
        FlextTapLdifConstants,
        FlextTapLdifModels,
        FlextTapLdifProtocols,
        FlextTapLdifService,
        FlextTapLdifServiceBase,
        FlextTapLdifSettings,
        FlextTapLdifTypes,
        FlextTapLdifUtilities,
        FlextTapLdifVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        main,
        settings,
        tap_ldif,
    )
    from tests.base import TestsFlextTapLdifServiceBase, s
    from tests.constants import TestsFlextTapLdifConstants, c
    from tests.models import TestsFlextTapLdifModels, m
    from tests.protocols import TestsFlextTapLdifProtocols, p
    from tests.settings import TestsFlextTapLdifSettings
    from tests.typings import TestsFlextTapLdifTypes, t
    from tests.unit import (
        TestsFlextTapLdifExtractService,
        TestsFlextTapLdifExtractSupport,
    )
    from tests.utilities import TestsFlextTapLdifUtilities, u


__all__: tuple[str, ...] = (
    "FlextTapLdifCli",
    "FlextTapLdifConfig",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifProtocols",
    "FlextTapLdifService",
    "FlextTapLdifServiceBase",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "FlextTapLdifVersion",
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifExtractService",
    "TestsFlextTapLdifExtractSupport",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifServiceBase",
    "TestsFlextTapLdifSettings",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
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
    {
        "FlextTapLdifCli": "flext_tap_ldif",
        "FlextTapLdifConfig": "flext_tap_ldif",
        "FlextTapLdifConstants": "flext_tap_ldif",
        "FlextTapLdifModels": "flext_tap_ldif",
        "FlextTapLdifProtocols": "flext_tap_ldif",
        "FlextTapLdifService": "flext_tap_ldif",
        "FlextTapLdifServiceBase": "flext_tap_ldif",
        "FlextTapLdifSettings": "flext_tap_ldif",
        "FlextTapLdifTypes": "flext_tap_ldif",
        "FlextTapLdifUtilities": "flext_tap_ldif",
        "FlextTapLdifVersion": "flext_tap_ldif",
        "TestsFlextTapLdifConstants": ".constants",
        "TestsFlextTapLdifExtractService": ".unit",
        "TestsFlextTapLdifExtractSupport": ".unit",
        "TestsFlextTapLdifModels": ".models",
        "TestsFlextTapLdifProtocols": ".protocols",
        "TestsFlextTapLdifServiceBase": ".base",
        "TestsFlextTapLdifSettings": ".settings",
        "TestsFlextTapLdifTypes": ".typings",
        "TestsFlextTapLdifUtilities": ".utilities",
        "__author__": "flext_tap_ldif",
        "__author_email__": "flext_tap_ldif",
        "__description__": "flext_tap_ldif",
        "__license__": "flext_tap_ldif",
        "__title__": "flext_tap_ldif",
        "__url__": "flext_tap_ldif",
        "__version__": "flext_tap_ldif",
        "__version_info__": "flext_tap_ldif",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_tap_ldif",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_tap_ldif",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tap_ldif",
        "t": ".typings",
        "tap_ldif": "flext_tap_ldif",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
