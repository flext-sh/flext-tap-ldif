"""FLEXT Tap LDIF Protocols — domain-specific LDIF tap protocol facade.

The 5 inner ``TapLdif.*`` Protocol classes that previously lived here had
**zero workspace consumers**. Per AGENTS.md §3.5 + STRICT YAGNI they were
deleted; the canonical ``FlextTapLdifProtocols`` facade remains intact
(re-exported via ``p``) and inherits behaviour from the parent
``FlextMeltanoProtocols`` (``p``) + ``FlextLdifProtocols`` MRO chain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifProtocols
from flext_meltano import p as meltano_p


class FlextTapLdifProtocols(meltano_p, FlextLdifProtocols):
    """Singer Tap LDIF protocols facade — composes Meltano + LDIF."""


p = FlextTapLdifProtocols
__all__: list[str] = ["FlextTapLdifProtocols", "p"]
