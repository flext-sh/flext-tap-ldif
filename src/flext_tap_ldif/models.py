"""Models for LDIF tap operations.

Entry and Singer shapes come from the parent libraries (``m.Ldif.*`` from
flext-ldif, ``m.Meltano.*`` from flext-meltano); the tap declares no copies.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels


class FlextTapLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Models facade for the LDIF tap composed from flext-meltano and flext-ldif."""

    class TapLdif:
        """TapLdif domain namespace."""


# Short aliases
m = FlextTapLdifModels

__all__: list[str] = ["FlextTapLdifModels", "m"]
