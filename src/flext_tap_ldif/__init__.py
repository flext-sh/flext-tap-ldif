# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

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
    from flext_ldif import d as d
    from flext_ldif import e as e
    from flext_ldif import h as h
    from flext_ldif import r as r
    from flext_ldif import s as s
    from flext_ldif import x as x

    from ._config import FlextTapLdifConfig as FlextTapLdifConfig
    from ._config import config as config
    from ._settings import FlextTapLdifSettings as FlextTapLdifSettings
    from ._settings import settings as settings
    from .api import FlextTapLdifService as FlextTapLdifService
    from .api import tap_ldif as tap_ldif
    from .cli import FlextTapLdifCli as FlextTapLdifCli
    from .cli import main as main
    from .constants import FlextTapLdifConstants as FlextTapLdifConstants

    c: type[FlextTapLdifConstants]
    from .models import FlextTapLdifModels as FlextTapLdifModels

    m: type[FlextTapLdifModels]
    from .protocols import FlextTapLdifProtocols as FlextTapLdifProtocols

    p: type[FlextTapLdifProtocols]
    from .tap import FlextTapLdif as FlextTapLdif
    from .typings import FlextTapLdifTypes as FlextTapLdifTypes

    t: type[FlextTapLdifTypes]
    from .utilities import FlextTapLdifUtilities as FlextTapLdifUtilities

    u: type[FlextTapLdifUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
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
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
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

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
