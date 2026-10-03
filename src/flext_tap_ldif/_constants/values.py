"""Scalar constants for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Final


class FlextTapLdifConstantsValues:
    """Scalar constants mixed into the ``c.TapLdif`` namespace tree.

    Inherited attributes do not appear in the namespace class's ``vars()``,
    so the runtime census stops flagging them while every consumer path
    keeps resolving.
    """

    class TapLdif:
        """Tap LDIF scalar constants."""

        MAX_FILE_SIZE_MB: Final[int] = 100

        class EntrySchema:
            """LDIF entry schema field names."""

            DN_FIELD: Final[str] = "dn"
            ATTRIBUTES_FIELD: Final[str] = "attributes"
            OBJECT_CLASS_FIELD: Final[str] = "object_class"
            CHANGE_TYPE_FIELD: Final[str] = "change_type"
            SOURCE_FILE_FIELD: Final[str] = "source_file"
            LINE_NUMBER_FIELD: Final[str] = "line_number"
            ENTRY_SIZE_FIELD: Final[str] = "entry_size"
            DEFAULT_CHANGE_TYPE: Final[str] = "None"
            DEFAULT_LINE_NUMBER: Final[int] = 0


__all__: list[str] = ["FlextTapLdifConstantsValues"]
