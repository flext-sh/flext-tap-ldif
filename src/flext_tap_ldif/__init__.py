# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports
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

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x

    from flext_tap_ldif._config import FlextTapLdifConfig, config
    from flext_tap_ldif._settings import FlextTapLdifSettings, settings
    from flext_tap_ldif.api import FlextTapLdifService, tap_ldif
    from flext_tap_ldif.cli import FlextTapLdifCli, main
    from flext_tap_ldif.constants import FlextTapLdifConstants, c
    from flext_tap_ldif.models import FlextTapLdifModels, m
    from flext_tap_ldif.protocols import FlextTapLdifProtocols, p
    from flext_tap_ldif.tap import FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes, t
    from flext_tap_ldif.utilities import FlextTapLdifUtilities, u


__all__: tuple[str, ...] = (
    "FlextTapLdif",
    "FlextTapLdifCli",
    "FlextTapLdifConfig",
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
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapLdif": ".tap",
        "FlextTapLdifCli": ".cli",
        "FlextTapLdifConfig": "._config",
        "FlextTapLdifConstants": ".constants",
        "FlextTapLdifModels": ".models",
        "FlextTapLdifProtocols": ".protocols",
        "FlextTapLdifService": ".api",
        "FlextTapLdifSettings": "._settings",
        "FlextTapLdifTypes": ".typings",
        "FlextTapLdifUtilities": ".utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "tap_ldif": ".api",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
