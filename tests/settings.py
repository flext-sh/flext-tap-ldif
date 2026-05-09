"""Runtime settings for flext-tap-ldif tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_tap_ldif import FlextTapLdifSettings


class TestsFlextTapLdifSettings(FlextTapLdifSettings, FlextTestsSettings):
    """Tap LDIF settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTapLdifSettings"]
