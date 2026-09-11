"""File and stream models for LDIF tap."""

from __future__ import annotations

from .file_metadata import FlextTapLdifModelsLdifFile
from .file_stream import FlextTapLdifModelsLdifStream


class FlextTapLdifModelsFile(FlextTapLdifModelsLdifFile, FlextTapLdifModelsLdifStream):
    """MRO mixin: LdifFile and LdifStream models."""
