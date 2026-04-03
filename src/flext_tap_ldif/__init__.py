# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_tap_ldif.__version__ import *
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

if _t.TYPE_CHECKING:
    import flext_tap_ldif._models as _flext_tap_ldif__models

    _models = _flext_tap_ldif__models
    import flext_tap_ldif._models.base as _flext_tap_ldif__models_base

    base = _flext_tap_ldif__models_base
    import flext_tap_ldif._models.batch as _flext_tap_ldif__models_batch

    batch = _flext_tap_ldif__models_batch
    import flext_tap_ldif._models.config as _flext_tap_ldif__models_config

    config = _flext_tap_ldif__models_config
    import flext_tap_ldif._models.entry as _flext_tap_ldif__models_entry

    entry = _flext_tap_ldif__models_entry
    import flext_tap_ldif._models.file as _flext_tap_ldif__models_file

    file = _flext_tap_ldif__models_file
    import flext_tap_ldif._models.record as _flext_tap_ldif__models_record

    record = _flext_tap_ldif__models_record
    import flext_tap_ldif.api as _flext_tap_ldif_api

    api = _flext_tap_ldif_api
    import flext_tap_ldif.constants as _flext_tap_ldif_constants

    constants = _flext_tap_ldif_constants
    import flext_tap_ldif.models as _flext_tap_ldif_models

    models = _flext_tap_ldif_models
    import flext_tap_ldif.protocols as _flext_tap_ldif_protocols

    protocols = _flext_tap_ldif_protocols
    import flext_tap_ldif.settings as _flext_tap_ldif_settings

    settings = _flext_tap_ldif_settings
    import flext_tap_ldif.tap as _flext_tap_ldif_tap

    tap = _flext_tap_ldif_tap
    import flext_tap_ldif.typings as _flext_tap_ldif_typings

    typings = _flext_tap_ldif_typings
    import flext_tap_ldif.utilities as _flext_tap_ldif_utilities

    utilities = _flext_tap_ldif_utilities

    _ = (
        FlextTapLdif,
        FlextTapLdifConstants,
        FlextTapLdifModels,
        FlextTapLdifModelsBase,
        FlextTapLdifModelsBatch,
        FlextTapLdifModelsConfig,
        FlextTapLdifModelsEntry,
        FlextTapLdifModelsFile,
        FlextTapLdifModelsRecord,
        FlextTapLdifProtocols,
        FlextTapLdifService,
        FlextTapLdifSettings,
        FlextTapLdifTypes,
        FlextTapLdifUtilities,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        _models,
        api,
        base,
        batch,
        c,
        config,
        constants,
        d,
        e,
        entry,
        file,
        h,
        logger,
        m,
        main,
        models,
        p,
        protocols,
        r,
        record,
        s,
        settings,
        t,
        tap,
        typings,
        u,
        utilities,
        x,
    )
_LAZY_IMPORTS = merge_lazy_imports(
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
        "__author__": "flext_tap_ldif.__version__",
        "__author_email__": "flext_tap_ldif.__version__",
        "__description__": "flext_tap_ldif.__version__",
        "__license__": "flext_tap_ldif.__version__",
        "__title__": "flext_tap_ldif.__version__",
        "__url__": "flext_tap_ldif.__version__",
        "__version__": "flext_tap_ldif.__version__",
        "__version_info__": "flext_tap_ldif.__version__",
        "_models": "flext_tap_ldif._models",
        "api": "flext_tap_ldif.api",
        "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
        "constants": "flext_tap_ldif.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "logger": "flext_tap_ldif.tap",
        "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
        "main": "flext_tap_ldif.tap",
        "models": "flext_tap_ldif.models",
        "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
        "protocols": "flext_tap_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_tap_ldif.api", "FlextTapLdifService"),
        "settings": "flext_tap_ldif.settings",
        "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
        "tap": "flext_tap_ldif.tap",
        "typings": "flext_tap_ldif.typings",
        "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
        "utilities": "flext_tap_ldif.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

__all__ = [
    "FlextTapLdif",
    "FlextTapLdifConstants",
    "FlextTapLdifModels",
    "FlextTapLdifModelsBase",
    "FlextTapLdifModelsBatch",
    "FlextTapLdifModelsConfig",
    "FlextTapLdifModelsEntry",
    "FlextTapLdifModelsFile",
    "FlextTapLdifModelsRecord",
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
    "_models",
    "api",
    "base",
    "batch",
    "c",
    "config",
    "constants",
    "d",
    "e",
    "entry",
    "file",
    "h",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "record",
    "s",
    "settings",
    "t",
    "tap",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
