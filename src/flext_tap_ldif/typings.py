"""Centralized typings facade for flext-tap-ldif.

- Extends flext-core types
- Add Tap LDIF-specific type aliases and Protocols here


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

"""
Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


from flext_core import E, F, FlextTypes as CoreFlextTypes, P, R, T, U, V


class FlextTypes(CoreFlextTypes):
    """Tap LDIF domain-specific types can extend here."""


__all__ = [
    "E",
    "F",
    "FlextTypes",
    "P",
    "R",
    "T",
    "U",
    "V",
]
