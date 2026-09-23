# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_ldif import ldif
    from flext_meltano import meltano, s

    from flext_core import core, d, e, h, lazy_attribute, r, x

    from ._config import FlextTapLdifConfig, config
    from ._settings import FlextTapLdifSettings, settings
    from .api import FlextTapLdifService, tap_ldif
    from .cli import FlextTapLdifCli, main
    from .constants import FlextTapLdifConstants, c
    from .models import FlextTapLdifModels, m
    from .protocols import FlextTapLdifProtocols, p
    from .tap import FlextTapLdif
    from .typings import FlextTapLdifTypes, t
    from .utilities import FlextTapLdifUtilities, u


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
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "lazy_attribute",
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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextTapLdifConfig", "config"),
            "._settings": ("FlextTapLdifSettings", "settings"),
            ".api": ("FlextTapLdifService", "tap_ldif"),
            ".cli": ("FlextTapLdifCli", "main"),
            ".constants": ("FlextTapLdifConstants", "c"),
            ".models": ("FlextTapLdifModels", "m"),
            ".protocols": ("FlextTapLdifProtocols", "p"),
            ".tap": ("FlextTapLdif",),
            ".typings": ("FlextTapLdifTypes", "t"),
            ".utilities": ("FlextTapLdifUtilities", "u"),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_ldif": ("ldif",),
            "flext_meltano": ("meltano", "s"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
