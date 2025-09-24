"""Models for LDIF tap operations.

This module provides data models for LDIF tap operations.
"""

from flext_core import FlextModels


class FlextTapLdifModels:
    """Models for LDIF tap operations."""

    Core = FlextModels

    LdifRecord = dict[str, object]
    LdifRecords = list[LdifRecord]
