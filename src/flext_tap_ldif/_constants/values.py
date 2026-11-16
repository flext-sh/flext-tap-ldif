"""Scalar constants for flext-tap-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar


class FlextTapLdifConstantsValues:
    """Scalar constants mixed into the ``c.TapLdif`` namespace tree.

    Inherited attributes do not appear in the namespace class's ``vars()``,
    so the runtime census stops flagging them while every consumer path
    keeps resolving.
    """

    TAP_NAME: ClassVar[str] = "tap-ldif"
    MAX_FILE_SIZE_MB: ClassVar[int] = 100

    class EntrySchema:
        """LDIF entry schema field names."""

        DN_FIELD: ClassVar[str] = "dn"
        ATTRIBUTES_FIELD: ClassVar[str] = "attributes"
        OBJECT_CLASS_FIELD: ClassVar[str] = "object_class"
        CHANGE_TYPE_FIELD: ClassVar[str] = "change_type"
        SOURCE_FILE_FIELD: ClassVar[str] = "source_file"
        LINE_NUMBER_FIELD: ClassVar[str] = "line_number"
        ENTRY_SIZE_FIELD: ClassVar[str] = "entry_size"
        DEFAULT_CHANGE_TYPE: ClassVar[str] = "None"
        DEFAULT_LINE_NUMBER: ClassVar[int] = 0


__all__: list[str] = ["FlextTapLdifConstantsValues"]
