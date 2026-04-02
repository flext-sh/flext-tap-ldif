# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
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

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x
    from flext_tap_ldif import (
        _models,
        api,
        constants,
        models,
        protocols,
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
        base,
        batch,
        config,
        entry,
        file,
        record,
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
    from flext_tap_ldif.tap import FlextTapLdif, logger, main
    from flext_tap_ldif.typings import FlextTapLdifTypes, FlextTapLdifTypes as t
    from flext_tap_ldif.utilities import (
        FlextTapLdifUtilities,
        FlextTapLdifUtilities as u,
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
        "c": ("flext_tap_ldif.constants", "FlextTapLdifConstants"),
        "constants": "flext_tap_ldif.constants",
        "d": "flext_ldif",
        "e": "flext_ldif",
        "h": "flext_ldif",
        "logger": "flext_tap_ldif.tap",
        "m": ("flext_tap_ldif.models", "FlextTapLdifModels"),
        "main": "flext_tap_ldif.tap",
        "models": "flext_tap_ldif.models",
        "p": ("flext_tap_ldif.protocols", "FlextTapLdifProtocols"),
        "protocols": "flext_tap_ldif.protocols",
        "r": "flext_ldif",
        "s": "flext_ldif",
        "settings": "flext_tap_ldif.settings",
        "t": ("flext_tap_ldif.typings", "FlextTapLdifTypes"),
        "tap": "flext_tap_ldif.tap",
        "typings": "flext_tap_ldif.typings",
        "u": ("flext_tap_ldif.utilities", "FlextTapLdifUtilities"),
        "utilities": "flext_tap_ldif.utilities",
        "x": "flext_ldif",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
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
