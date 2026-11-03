# AUTO-GENERATED FILE — Regenerate with: make gen
"""Static instance-to-protocol evidence required by candidate admission.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_ldif/_protocols/model_conformance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flext_tap_ldif import FlextTapLdifModels, FlextTapLdifProtocols

    def model_protocol_1(
        value: (FlextTapLdifModels.Root),
    ) -> FlextTapLdifProtocols.Root:
        return value

    def model_protocol_2(
        value: (FlextTapLdifModels.TapLdif),
    ) -> FlextTapLdifProtocols.TapLdif:
        return value

    def model_protocol_3(
        value: (FlextTapLdifModels.TapLdif.StreamRule),
    ) -> FlextTapLdifProtocols.TapLdifStreamRule:
        return value
