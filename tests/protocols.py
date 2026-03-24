"""Protocols for flext-tap-ldif tests - uses composition with FlextTestsProtocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_tap_ldif import FlextTapLdifProtocols
from tests import t


class FlextTapLdifTestProtocols(FlextTestsProtocols, FlextTapLdifProtocols):
    """Protocols for flext-tap-ldif tests - combines FlextTestsProtocols with FlextTapLdifProtocols.

    Architecture: Uses composition (not inheritance) with FlextTestsProtocols and FlextTapLdifProtocols
    for flext-tap-ldif-specific protocol definitions.

    Access patterns:
    - FlextTapLdifTestProtocols.Tests.* = flext_tests test protocols (via composition)
    - FlextTapLdifTestProtocols.TapLdif.* = flext-tap-ldif-specific test protocols
    - FlextTapLdifTestProtocols.* = FlextTestsProtocols protocols (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsProtocols deprecates subclassing)
    - flext-tap-ldif-specific protocols go in TapLdif namespace
    - Generic protocols accessed via Tests namespace
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols."""

    class TapLdif(FlextTapLdifProtocols.TapLdif):
        """Tap LDIF test protocols - domain-specific for LDIF tap testing.

        Contains test protocols specific to LDIF tap functionality including:
        - Mock LDIF file protocols for testing
        - Test data provider protocols
        - Test assertion protocols
        """

        @runtime_checkable
        class MockLdifFile(Protocol):
            """Protocol for mock LDIF file operations in tests."""

            def open_file(self, file_path: str) -> bool:
                """Open mock LDIF file."""
                ...

            def close_file(self) -> bool:
                """Close mock LDIF file."""
                ...

            def read_entries(self) -> Sequence[t.ContainerMapping]:
                """Read entries from mock LDIF file."""
                ...

        @runtime_checkable
        class TestLdifDataProvider(Protocol):
            """Protocol for test LDIF data providers."""

            def get_test_entries(self) -> Sequence[t.ContainerMapping]:
                """Get test LDIF entries."""
                ...

            def get_test_file_content(self) -> str:
                """Get test LDIF file content."""
                ...

            def get_test_config(self) -> t.ContainerMapping:
                """Get test LDIF configuration."""
                ...

        @runtime_checkable
        class TestLdifAssertion(Protocol):
            """Protocol for test LDIF assertions."""

            def assert_ldif_file_parsed(
                self, entries: Sequence[t.ContainerMapping]
            ) -> None:
                """Assert LDIF file was parsed correctly."""
                ...

            def assert_ldif_entries_valid(
                self, entries: Sequence[t.ContainerMapping]
            ) -> None:
                """Assert LDIF entries are valid."""
                ...

            def assert_ldif_stream_config_valid(
                self, stream: t.ContainerMapping
            ) -> None:
                """Assert LDIF stream configuration is valid."""
                ...


p = FlextTapLdifTestProtocols
__all__ = ["FlextTapLdifTestProtocols", "p"]
