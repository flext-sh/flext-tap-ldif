"""flext-tap-ldif config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/tap_ldif.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.TapLdif``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextTapLdifConfigModels:
    """Namespace of typed flext-tap-ldif config models."""

    class Io(BaseModel):
        """LDIF input/output defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        file_pattern: str = Field(description="LDIF file glob pattern.")
        encoding: str = Field(description="File encoding.")
        strict_parsing: bool = Field(description="Strict LDIF parsing.")
        max_file_size_mb: int = Field(
            ge=1, description="Maximum file size in megabytes."
        )

    class Processing(BaseModel):
        """LDIF processing defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        batch_size: int = Field(
            ge=1, description="Default batch size for LDIF processing."
        )
        default_change_type: str = Field(
            description="Default changetype token for entries without one."
        )
        default_line_number: int = Field(
            ge=0, description="Default line number for entries without source location."
        )

    class EntrySchema(BaseModel):
        """LDIF entry schema field names."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        dn_field: str = Field(description="Distinguished name field name.")
        attributes_field: str = Field(description="Attributes field name.")
        object_class_field: str = Field(description="Object class field name.")
        change_type_field: str = Field(description="Change type field name.")
        source_file_field: str = Field(description="Source file field name.")
        line_number_field: str = Field(description="Line number field name.")
        entry_size_field: str = Field(description="Entry size field name.")

    class TapLdif(BaseModel):
        """Root tap-LDIF business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        io: FlextTapLdifConfigModels.Io = Field(
            description="LDIF input/output defaults."
        )
        processing: FlextTapLdifConfigModels.Processing = Field(
            description="LDIF processing defaults."
        )
        entry_schema: FlextTapLdifConfigModels.EntrySchema = Field(
            description="LDIF entry schema field names."
        )

    class Root(BaseModel):
        """Root flext-tap-ldif config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        TapLdif: FlextTapLdifConfigModels.TapLdif = Field(
            description="Tap LDIF business-rule config namespace."
        )


__all__: list[str] = ["FlextTapLdifConfigModels"]
