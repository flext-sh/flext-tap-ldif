# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_ldif import ldif
    from flext_meltano import cli, d, e, h, meltano, r, x

    from flext_tap_ldif.__version__ import (
        FlextTapLdifVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_tap_ldif._config import FlextTapLdifConfig, config
    from flext_tap_ldif._settings import FlextTapLdifSettings, settings
    from flext_tap_ldif.api import FlextTapLdifService, tap_ldif
    from flext_tap_ldif.base import FlextTapLdifServiceBase, s
    from flext_tap_ldif.cli import FlextTapLdifCli, main
    from flext_tap_ldif.constants import FlextTapLdifConstants, c
    from flext_tap_ldif.models import FlextTapLdifModels, m
    from flext_tap_ldif.protocols import FlextTapLdifProtocols, p
    from flext_tap_ldif.typings import FlextTapLdifTypes, t
    from flext_tap_ldif.utilities import FlextTapLdifUtilities, u


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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "cli",
    "config",
    "d",
    "e",
    "h",
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
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapLdifCli": ".cli",
        "FlextTapLdifConfig": "._config",
        "FlextTapLdifConstants": ".constants",
        "FlextTapLdifModels": ".models",
        "FlextTapLdifProtocols": ".protocols",
        "FlextTapLdifService": ".api",
        "FlextTapLdifServiceBase": ".base",
        "FlextTapLdifSettings": "._settings",
        "FlextTapLdifTypes": ".typings",
        "FlextTapLdifUtilities": ".utilities",
        "FlextTapLdifVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "c": ".constants",
        "cli": "flext_meltano",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "ldif": "flext_ldif",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": ".base",
        "settings": "._settings",
        "t": ".typings",
        "tap_ldif": ".api",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_tap_ldif.__version__ import __version__
