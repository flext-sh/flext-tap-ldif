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
    from flext_tap_ldif.api import FlextTapLdifService, tap_ldif
    from flext_tap_ldif.cli import FlextTapLdifCli, main
    from flext_tap_ldif.constants import FlextTapLdifConstants, c
    from flext_tap_ldif.models import FlextTapLdifModels, m
    from flext_tap_ldif.protocols import FlextTapLdifProtocols, p
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes, t
    from flext_tap_ldif.utilities import FlextTapLdifUtilities, u
_LAZY_IMPORTS = build_lazy_import_map(
    {
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
        ".settings": ("FlextTapLdifSettings",),
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
    },
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
