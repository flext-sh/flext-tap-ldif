"""Protocols for flext-tap-ldif tests - uses composition with TestsFlextProtocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from typing import Protocol, runtime_checkable

from flext_tests import FlextTestsProtocols

from flext_tap_ldif import FlextTapLdifProtocols
from tests import t


class TestsFlextTapLdifProtocols(FlextTestsProtocols, FlextTapLdifProtocols):
    """Protocols for flext-tap-ldif tests - combines TestsFlextProtocols with FlextTapLdifProtocols.

    Architecture: Uses composition (not inheritance) with TestsFlextProtocols and FlextTapLdifProtocols
    for flext-tap-ldif-specific protocol definitions.

    Access patterns:
    - TestsFlextTapLdifProtocols.Tests.* = flext_tests test protocols (via composition)
    - TestsFlextTapLdifProtocols.TapLdif.* = flext-tap-ldif-specific test protocols
    - TestsFlextTapLdifProtocols.* = TestsFlextProtocols protocols (via composition)

    Rules:
    - Use composition, not inheritance (TestsFlextProtocols deprecates subclassing)
    - flext-tap-ldif-specific protocols go in TapLdif namespace
    - Generic protocols accessed via Tests namespace
    """

    class Tests(FlextTestsProtocols.Tests):
        """Project-specific test protocols."""

    class TapLdif:
        """Tap LDIF test protocols — domain-specific for LDIF tap testing.

        Hosts test-only protocols (``MockLdifFile``, ``TestLdifDataProvider``,
        ``TestLdifAssertion``). The parent ``FlextTapLdifProtocols.TapLdif``
        namespace was deleted as dead code (no workspace consumers); these
        test-only entries now live directly under the test facade.
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

            def read_entries(self) -> Sequence[t.JsonMapping]:
                """Read entries from mock LDIF file."""
                ...

        @runtime_checkable
        class TestLdifDataProvider(Protocol):
            """Protocol for test LDIF data providers."""

            def test_entries(self) -> Sequence[t.JsonMapping]:
                """Get test LDIF entries."""
                ...

            def test_file_content(self) -> str:
                """Get test LDIF file content."""
                ...

            def test_config(self) -> t.JsonMapping:
                """Get test LDIF configuration."""
                ...

        @runtime_checkable
        class TestLdifAssertion(Protocol):
            """Protocol for test LDIF assertions."""

            def assert_ldif_file_parsed(
                self,
                entries: Sequence[t.JsonMapping],
            ) -> None:
                """Assert LDIF file was parsed correctly."""
                ...

            def assert_ldif_entries_valid(
                self,
                entries: Sequence[t.JsonMapping],
            ) -> None:
                """Assert LDIF entries are valid."""
                ...

            def assert_ldif_stream_config_valid(
                self,
                stream: t.JsonMapping,
            ) -> None:
                """Assert LDIF stream configuration is valid."""
                ...


p = TestsFlextTapLdifProtocols
__all__: list[str] = ["TestsFlextTapLdifProtocols", "p"]
