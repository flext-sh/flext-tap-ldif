# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models for LDIF tap operations.

Entry and Singer shapes come from the parent libraries (``m.Ldif.*`` from
flext-ldif, ``m.Meltano.*`` from flext-meltano); the tap declares no copies.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import m
from flext_meltano import m as flext_meltano_m

from flext_tap_ldif._models import FlextTapLdifModelsBase


class FlextTapLdifModels(flext_meltano_m, m):
    """Models facade for the LDIF tap composed from flext-meltano and flext-ldif."""

    class TapLdif(FlextTapLdifModelsBase):
        """TapLdif domain namespace."""


# Short aliases
m = FlextTapLdifModels
__all__: list[str] = ["FlextTapLdifModels", "m"]
