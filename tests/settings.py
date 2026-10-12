"""Runtime settings for flext-tap-ldif tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_tap_ldif import FlextTapLdifSettings


class TestsFlextTapLdifSettings(FlextTapLdifSettings, FlextTestsSettings):
    """Tap LDIF settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTapLdifSettings"]
