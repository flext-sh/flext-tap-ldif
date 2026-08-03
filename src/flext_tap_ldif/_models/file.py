"""File and stream models for LDIF tap."""

from __future__ import annotations

from flext_tap_ldif._models.file_metadata import FlextTapLdifModelsLdifFile
from flext_tap_ldif._models.file_stream import FlextTapLdifModelsLdifStream


class FlextTapLdifModelsFile(FlextTapLdifModelsLdifFile, FlextTapLdifModelsLdifStream):
    """MRO mixin: LdifFile and LdifStream models."""
