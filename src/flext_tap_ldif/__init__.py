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

if _TYPE_CHECKING:
    from flext_ldif import d, e, h, r, s, x

    from flext_tap_ldif.__version__ import *
    from flext_tap_ldif._models import *
    from flext_tap_ldif.constants import *
    from flext_tap_ldif.models import *
    from flext_tap_ldif.protocols import *
    from flext_tap_ldif.settings import *
    from flext_tap_ldif.tap import *
    from flext_tap_ldif.typings import *
    from flext_tap_ldif.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    ("flext_tap_ldif._models",),
    {
        "FlextTapLdif": "flext_tap_ldif.tap",
        "FlextTapLdifConstants": "flext_tap_ldif.constants",
        "FlextTapLdifModels": "flext_tap_ldif.models",
        "FlextTapLdifProtocols": "flext_tap_ldif.protocols",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
