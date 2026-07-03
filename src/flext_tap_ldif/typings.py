"""FLEXT Tap LDIF Types — MRO composition of parent type namespaces.

Singer protocol types come from the inherited ``t.Meltano.*`` namespace.
LDIF domain types come from the inherited ``t.Ldif.*`` namespace.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.Ldif.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifTypes
from flext_meltano import t


class FlextTapLdifTypes(t, FlextLdifTypes):
    """MRO facade composing Meltano + LDIF type namespaces.

    Access: ``t.Meltano.*`` (Singer protocol), ``t.Ldif.*`` (LDIF domain),
    and all core ``t.*`` types via MRO inheritance.
    """


t = FlextTapLdifTypes
__all__: list[str] = ["FlextTapLdifTypes", "t"]
