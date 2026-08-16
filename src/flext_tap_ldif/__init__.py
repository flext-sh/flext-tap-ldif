# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_ldif import d, e, h, r, s, x

    from ._config import FlextTapLdifConfig, config
    from ._settings import FlextTapLdifSettings, settings
    from .api import FlextTapLdifService, tap_ldif
    from .cli import FlextTapLdifCli, main
    from .constants import FlextTapLdifConstants, FlextTapLdifConstants as c
    from .models import FlextTapLdifModels, FlextTapLdifModels as m
    from .protocols import FlextTapLdifProtocols, FlextTapLdifProtocols as p
    from .tap import FlextTapLdif
    from .typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from .utilities import FlextTapLdifUtilities, FlextTapLdifUtilities as u
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
    MappingProxyType(
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
                "flext_ldif": ("d", "e", "h", "r", "s", "x"),
            }),
            alias_groups=MappingProxyType({}),
            sort_keys=False,
        )
    ),
    public_exports=__all__,
)
