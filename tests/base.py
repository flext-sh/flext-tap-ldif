"""Service base for flext-tap-ldif tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_tap_ldif import m
from tests.settings import TestsFlextTapLdifSettings


class TestsFlextTapLdifServiceBase(tests_s):
    """Tap LDIF test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextTapLdifSettings:
        """Return the typed Tap LDIF+Tests settings singleton."""
        return TestsFlextTapLdifSettings.fetch_global()

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTapLdifSettings)


s = TestsFlextTapLdifServiceBase

__all__: list[str] = ["TestsFlextTapLdifServiceBase", "s"]
