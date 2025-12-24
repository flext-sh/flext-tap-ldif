"""Test protocol definitions for flext-tap-ldif.

Provides TestsFlextTapLdifProtocols, combining FlextTestsProtocols with
the tap's protocol definitions for test-specific protocol definitions.

Note: flext-tap-ldif defines individual protocols (TapProtocol, TapConfigProtocol)
without a wrapper class. Tests can access FlextTestsProtocols functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.protocols import FlextTestsProtocols


class TestsFlextTapLdifProtocols(FlextTestsProtocols):
    """Test protocols for flext-tap-ldif.

    Extends FlextTestsProtocols with tap-specific test protocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.Tests.TapLdif.* (tap-specific test protocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TapLdif-specific protocols.
        """

        class TapLdif:
            """TapLdif-specific test protocols."""


# Runtime aliases
p = TestsFlextTapLdifProtocols
tp = TestsFlextTapLdifProtocols

__all__ = ["TestsFlextTapLdifProtocols", "p", "tp"]
