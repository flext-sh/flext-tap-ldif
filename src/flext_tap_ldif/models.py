"""Module docstring."""

from __future__ import annotations

"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from flext_core import FlextModels


class FlextTapLdifModels(FlextModels):
    """Models for LDIF tap operations.

    Extends FlextModels to avoid duplication and ensure consistency.
    All LDIF tap models benefit from FlextModels patterns.
    """

    LdifRecord = dict["str", "object"]
    LdifRecords = list[LdifRecord]
