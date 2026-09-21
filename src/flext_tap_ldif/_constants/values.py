"""Scalar constants for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final

from flext_ldif import c as _ldif_c


class FlextTapLdifConstantsValues:
    """Scalar constants mixed into the ``c.TapLdif`` namespace tree.

    Inherited attributes do not appear in the namespace class's ``vars()``,
    so the runtime census stops flagging them while every consumer path
    keeps resolving.
    """

    class TapLdif:
        """Tap LDIF scalar constants."""

        DEFAULT_LDIF_ENCODING: Final[str] = _ldif_c.Ldif.Encoding.UTF8

        class Format:
            """LDIF format specifications."""

            MAX_LINE_LENGTH: Final[int] = _ldif_c.Ldif.DEFAULT_LINE_WIDTH

        class TapLdifPerformance:
            """Tap LDIF performance constants."""

            DEFAULT_BATCH_SIZE: Final[int] = 1000

        class EntrySchema:
            """LDIF entry schema field names."""

            DN_FIELD: Final[str] = "dn"


__all__: list[str] = ["FlextTapLdifConstantsValues"]
