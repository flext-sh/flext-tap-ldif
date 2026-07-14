# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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
    from flext_ldif import d, e, h, r, s, x

    from ._settings import FlextTapLdifSettings, settings
    from .api import FlextTapLdifService, tap_ldif
    from .cli import FlextTapLdifCli, main
    from .constants import FlextTapLdifConstants, FlextTapLdifConstants as c
    from .models import FlextTapLdifModels, FlextTapLdifModels as m
    from .protocols import FlextTapLdifProtocols, FlextTapLdifProtocols as p
    from .tap import FlextTapLdif
    from .typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from .utilities import FlextTapLdifUtilities, FlextTapLdifUtilities as u

    _ = (
        c,
        FlextTapLdifConstants,
        t,
        FlextTapLdifTypes,
        p,
        FlextTapLdifProtocols,
        m,
        FlextTapLdifModels,
        u,
        FlextTapLdifUtilities,
        d,
        e,
        h,
        r,
        s,
        x,
        main,
        FlextTapLdifCli,
        FlextTapLdifSettings,
        settings,
        FlextTapLdifService,
        tap_ldif,
        FlextTapLdif,
    )


_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._settings": (
        "FlextTapLdifSettings",
        "settings",
    ),
    ".api": (
        "FlextTapLdifService",
        "tap_ldif",
    ),
    ".cli": (
        "FlextTapLdifCli",
        "main",
    ),
    ".constants": (
        "FlextTapLdifConstants",
        "c",
    ),
    ".models": (
        "FlextTapLdifModels",
        "m",
    ),
    ".protocols": (
        "FlextTapLdifProtocols",
        "p",
    ),
    ".tap": ("FlextTapLdif",),
    ".typings": (
        "FlextTapLdifTypes",
        "t",
    ),
    ".utilities": (
        "FlextTapLdifUtilities",
        "u",
    ),
    "flext_ldif": (
        "d",
        "e",
        "h",
        "r",
        "s",
        "x",
    ),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES,
    alias_groups=_LAZY_ALIAS_GROUPS,
    sort_keys=False,
)

_DIRECT_IMPORTS: tuple[str, ...] = (
    "FlextTapLdif",
    "FlextTapLdifCli",
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
    "build_lazy_import_map",
    "c",
    "d",
    "e",
    "h",
    "install_lazy_exports",
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

__all__: tuple[str, ...] = (
    "FlextTapLdif",
    "FlextTapLdifCli",
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
    _LAZY_IMPORTS,
    public_exports=__all__,
)
