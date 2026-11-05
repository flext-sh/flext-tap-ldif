"""Service base for flext-tap-ldif — the ``s`` alias consumed by ``services/*``.

Composes the flext-meltano Singer tap runtime via MRO and injects the flext-ldif
facade as ``self.ldif`` so tap services perform LDIF work through the
library while importing only ``c, t, p, m, u`` plus this ``s``.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_ldif import ldif
from flext_meltano import FlextMeltanoServiceBase

from flext_tap_ldif import m, p


class FlextTapLdifServiceBase(FlextMeltanoServiceBase):
    """Tap-LDIF service base: meltano service runtime plus injected LDIF facade."""

    _ldif: p.Ldif.Client = m.PrivateAttr(default_factory=lambda: ldif)

    @property
    def ldif(self) -> p.Ldif.Client:
        """The shared flext-ldif facade for tap services."""
        return self._ldif


s = FlextTapLdifServiceBase

__all__: list[str] = ["FlextTapLdifServiceBase", "s"]
