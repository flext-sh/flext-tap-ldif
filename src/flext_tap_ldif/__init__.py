# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""FLEXT Tap LDIF - Enterprise Singer Tap for LDIF Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
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

if TYPE_CHECKING:
    from flext_ldif import *

    from flext_tap_ldif import (
        constants,
        models,
        protocols,
        settings,
        tap,
        typings,
        utilities,
    )
    from flext_tap_ldif._models import *
    from flext_tap_ldif.constants import *
    from flext_tap_ldif.models import *
    from flext_tap_ldif.protocols import *
    from flext_tap_ldif.settings import *
    from flext_tap_ldif.tap import *
    from flext_tap_ldif.typings import *
    from flext_tap_ldif.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextTapLdif": "flext_tap_ldif.tap",
    "FlextTapLdifConstants": "flext_tap_ldif.constants",
    "FlextTapLdifModels": "flext_tap_ldif.models",
    "FlextTapLdifModelsBase": "flext_tap_ldif._models.base",
    "FlextTapLdifModelsBatch": "flext_tap_ldif._models.batch",
    "FlextTapLdifModelsConfig": "flext_tap_ldif._models.config",
    "FlextTapLdifModelsEntry": "flext_tap_ldif._models.entry",
    "FlextTapLdifModelsFile": "flext_tap_ldif._models.file",
    "FlextTapLdifModelsRecord": "flext_tap_ldif._models.record",
    "FlextTapLdifProtocols": "flext_tap_ldif.protocols",
    "FlextTapLdifSettings": "flext_tap_ldif.settings",
    "FlextTapLdifTypes": "flext_tap_ldif.typings",
    "FlextTapLdifUtilities": "flext_tap_ldif.utilities",
    "_models": "flext_tap_ldif._models",
    "base": "flext_tap_ldif._models.base",
    "batch": "flext_tap_ldif._models.batch",
    "c": ["flext_tap_ldif.constants", "FlextTapLdifConstants"],
    "config": "flext_tap_ldif._models.config",
    "constants": "flext_tap_ldif.constants",
    "d": "flext_ldif",
    "e": "flext_ldif",
    "entry": "flext_tap_ldif._models.entry",
    "file": "flext_tap_ldif._models.file",
    "h": "flext_ldif",
    "logger": "flext_tap_ldif.tap",
    "m": ["flext_tap_ldif.models", "FlextTapLdifModels"],
    "main": "flext_tap_ldif.tap",
    "models": "flext_tap_ldif.models",
    "p": ["flext_tap_ldif.protocols", "FlextTapLdifProtocols"],
    "protocols": "flext_tap_ldif.protocols",
    "r": "flext_ldif",
    "record": "flext_tap_ldif._models.record",
    "s": "flext_ldif",
    "settings": "flext_tap_ldif.settings",
    "t": ["flext_tap_ldif.typings", "FlextTapLdifTypes"],
    "tap": "flext_tap_ldif.tap",
    "typings": "flext_tap_ldif.typings",
    "u": ["flext_tap_ldif.utilities", "FlextTapLdifUtilities"],
    "utilities": "flext_tap_ldif.utilities",
    "x": "flext_ldif",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
