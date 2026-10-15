"""Protocols for flext-tap-ldif tests - uses composition with TestsFlextProtocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_tap_ldif import FlextTapLdifProtocols


class TestsFlextTapLdifProtocols(FlextTestsProtocols, FlextTapLdifProtocols):
    """Protocols for flext-tap-ldif tests: TestsFlextProtocols + FlextTapLdifProtocols.

    Uses composition with ``TestsFlextProtocols`` for the generic test protocols
    and ``FlextTapLdifProtocols`` for the project protocols.

    Access patterns:
    - TestsFlextTapLdifProtocols.Tests.* = flext_tests test protocols
    - TestsFlextTapLdifProtocols.* = TestsFlextProtocols protocols

    Rules:
    - Use composition, not inheritance (TestsFlextProtocols deprecates subclassing)
    - Generic protocols accessed via the Tests namespace
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols."""


p = TestsFlextTapLdifProtocols
__all__: list[str] = ["TestsFlextTapLdifProtocols", "p"]
