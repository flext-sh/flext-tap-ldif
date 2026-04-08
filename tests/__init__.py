# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.constants import (
        TestsFlextTapLdifConstants,
        TestsFlextTapLdifConstants as c,
    )
    from tests.models import TestsFlextTapLdifModels, TestsFlextTapLdifModels as m
    from tests.protocols import (
        TestsFlextTapLdifProtocols,
        TestsFlextTapLdifProtocols as p,
    )
    from tests.typings import TestsFlextTapLdifTypes, TestsFlextTapLdifTypes as t
    from tests.utilities import (
        TestsFlextTapLdifUtilities,
        TestsFlextTapLdifUtilities as u,
    )
_LAZY_IMPORTS = {
    "TestsFlextTapLdifConstants": ("tests.constants", "TestsFlextTapLdifConstants"),
    "TestsFlextTapLdifModels": ("tests.models", "TestsFlextTapLdifModels"),
    "TestsFlextTapLdifProtocols": ("tests.protocols", "TestsFlextTapLdifProtocols"),
    "TestsFlextTapLdifTypes": ("tests.typings", "TestsFlextTapLdifTypes"),
    "TestsFlextTapLdifUtilities": ("tests.utilities", "TestsFlextTapLdifUtilities"),
    "c": ("tests.constants", "TestsFlextTapLdifConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "TestsFlextTapLdifModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "TestsFlextTapLdifProtocols"),
    "protocols": "tests.protocols",
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "TestsFlextTapLdifTypes"),
    "test_tap": "tests.test_tap",
    "typings": "tests.typings",
    "u": ("tests.utilities", "TestsFlextTapLdifUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestsFlextTapLdifConstants",
    "TestsFlextTapLdifModels",
    "TestsFlextTapLdifProtocols",
    "TestsFlextTapLdifTypes",
    "TestsFlextTapLdifUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_tap",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
