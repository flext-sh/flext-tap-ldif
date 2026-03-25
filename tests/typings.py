"""Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from flext_tests import FlextTestsTypes

from flext_tap_ldif import FlextTapLdifConstants as _c, FlextTapLdifTypes


class FlextTapLdifTestTypes(FlextTestsTypes, FlextTapLdifTypes):
    """Types for flext-tap-ldif tests - uses composition with FlextTestsTypes.

    Architecture: Uses composition (not inheritance) with FlextTestsTypes and FlextTapLdifTypes
    for flext-tap-ldif-specific type definitions.

    Access patterns:
    - FlextTapLdifTestTypes.Tests.* = flext_tests test types (via composition)
    - FlextTapLdifTestTypes.TapLdifTest.* = flext-tap-ldif-specific test types
    - FlextTapLdifTestTypes.* = FlextTestsTypes types (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsTypes deprecates subclassing)
    - flext-tap-ldif-specific types go in TapLdifTest namespace
    - Generic types accessed via Tests namespace
    """

    class TapLdifTest:
        """Tap LDIF test types - domain-specific for LDIF tap testing.

        Contains test types specific to LDIF tap functionality including:
        - Test configuration types
        - Mock LDIF data types
        - Test scenario types
        """

        type TestLdifFilePath = _c.TapLdif.TestLdifFilePath
        type TestLdifEncoding = _c.TapLdif.TestLdifEncoding
        type TestObjectClass = _c.TapLdif.TestObjectClass
        type MockLdifEntry = Mapping[str, str | Mapping[str, t.StrSequence]]
        type MockLdifFile = Sequence[Mapping[str, str | Mapping[str, t.StrSequence]]]
        type TestLdifScenario = t.ContainerMapping
        type TestLdifValidationResult = Mapping[str, bool | str | t.StrSequence]
        type TestLdifParsingResult = t.ContainerMapping


t = FlextTapLdifTestTypes
__all__ = ["FlextTapLdifTestTypes", "t"]
