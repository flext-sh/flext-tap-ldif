# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
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
from flext_tap_ldif._exports import FLEXT_TAP_LDIF_LAZY_IMPORTS

if TYPE_CHECKING:
    from flext_ldif import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_tap_ldif.api import (
        FlextTapLdifService as FlextTapLdifService,
        tap_ldif as tap_ldif,
    )
    from flext_tap_ldif.cli import FlextTapLdifCli as FlextTapLdifCli, main as main
    from flext_tap_ldif.constants import (
        FlextTapLdifConstants as FlextTapLdifConstants,
        c as c,
    )
    from flext_tap_ldif.models import FlextTapLdifModels as FlextTapLdifModels, m as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols as FlextTapLdifProtocols,
        p as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings as FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif as FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes as FlextTapLdifTypes, t as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities as FlextTapLdifUtilities,
        u as u,
    )


_LAZY_IMPORTS = FLEXT_TAP_LDIF_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTapLdif",
    "FlextTapLdifCli",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifProtocols",
    "FlextTapLdifService",
    "FlextTapLdifSettings",
    "FlextTapLdifTypes",
    "FlextTapLdifUtilities",
    "tap_ldif",
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
    "t",
    "tap_ldif",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=_PUBLIC_EXPORTS,
)
