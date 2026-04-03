# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap ldif package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_tap_ldif.__version__ import (
    __all__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_tap_ldif import (
        _models,
        api,
        base,
        batch,
        config,
        constants,
        entry,
        file,
        models,
        protocols,
        record,
        settings,
        tap,
        typings,
        utilities,
    )
    from flext_tap_ldif._models import (
        FlextTapLdifModelsBase,
        FlextTapLdifModelsBatch,
        FlextTapLdifModelsConfig,
        FlextTapLdifModelsEntry,
        FlextTapLdifModelsFile,
        FlextTapLdifModelsRecord,
    )
    from flext_tap_ldif.api import FlextTapLdifService
    from flext_tap_ldif.constants import (
        FlextTapLdifConstants,
        FlextTapLdifConstants as c,
    )
    from flext_tap_ldif.models import FlextTapLdifModels, FlextTapLdifModels as m
    from flext_tap_ldif.protocols import (
        FlextTapLdifProtocols,
        FlextTapLdifProtocols as p,
    )
    from flext_tap_ldif.settings import FlextTapLdifSettings
    from flext_tap_ldif.tap import FlextTapLdif
    from flext_tap_ldif.typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
        logger,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_tap_ldif._models",),
    {
        "FlextTapLdif": "flext_tap_ldif.tap",
        "FlextTapLdifConstants": "flext_tap_ldif.constants",
        "FlextTapLdifModels": "flext_tap_ldif.models",
        "FlextTapLdifProtocols": "flext_tap_ldif.protocols",
        "FlextTapLdifService": "flext_tap_ldif.api",
        "FlextTapLdifSettings": "flext_tap_ldif.settings",
        "FlextTapLdifTypes": "flext_tap_ldif.typings",
        "FlextTapLdifUtilities": "flext_tap_ldif.utilities",
        "_models": "flext_tap_ldif._models",
        "api": "flext_tap_ldif.api",
        "base": "flext_tap_ldif.base",
        "batch": "flext_tap_ldif.batch",
        "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
        "config": "flext_tap_ldif.config",
        "constants": "flext_tap_ldif.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "entry": "flext_tap_ldif.entry",
        "file": "flext_tap_ldif.file",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "logger": "flext_tap_ldif.utilities",
        "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
        "models": "flext_tap_ldif.models",
        "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
        "protocols": "flext_tap_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "record": "flext_tap_ldif.record",
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_tap_ldif.settings",
        "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
        "tap": "flext_tap_ldif.tap",
        "typings": "flext_tap_ldif.typings",
        "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
        "utilities": "flext_tap_ldif.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
