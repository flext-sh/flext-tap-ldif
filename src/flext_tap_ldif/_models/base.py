"""Base utilities and computed fields for LDIF tap models."""

from __future__ import annotations

import base64
from datetime import UTC, datetime
from typing import Self

from flext_meltano import m, u

from flext_tap_ldif import c, t


class FlextTapLdifModelsBase:
    """Base MRO mixin: computed fields, serializers, validators, utility methods."""

    @property
    def active_ldif_tap_models_count(self) -> int:
        """Count of active LDIF tap models with file processing capabilities."""
        model_attrs = [
            "LdifEntry",
            "LdifChangeRecord",
            "LdifFile",
            "LdifStream",
            "LdifBatch",
            "LdifProcessingState",
            "LdifTapConfig",
            "LdifRecord",
            "LdifValidationResult",
        ]
        return sum(1 for attr in model_attrs if getattr(self, attr, None) is not None)

    @property
    def ldif_tap_system_summary(self) -> t.JsonMapping:
        """Complete Singer LDIF tap system summary with file processing capabilities."""
        total_models = sum(
            1
            for attr in [
                "LdifEntry",
                "LdifChangeRecord",
                "LdifFile",
                "LdifStream",
                "LdifBatch",
                "LdifProcessingState",
                "LdifTapConfig",
                "LdifRecord",
                "LdifValidationResult",
            ]
            if getattr(self, attr, None) is not None
        )
        return {
            "total_models": total_models,
            "tap_type": "singer_ldif_file_extractor",
            "extraction_features": [
                "ldif_file_parsing",
                "change_record_processing",
                "entry_validation",
                "batch_file_processing",
                "format_compliance_checking",
                "performance_monitoring",
            ],
            "singer_compliance": {
                "protocol_version": "singer_v1",
                "stream_discovery": True,
                "catalog_generation": True,
                "state_management": True,
                "file_bookmarking": True,
            },
            "ldif_capabilities": {
                "format_validation": True,
                "change_record_support": True,
                "batch_processing": True,
                "error_recovery": True,
                "schema_inference": True,
            },
        }

    @u.field_serializer("*", when_used="json")
    def serialize_with_ldif_metadata(
        self,
        value: t.JsonValue,
        _info: u.FieldSerializationInfo,
    ) -> t.JsonValue:
        """Add Singer LDIF tap metadata to all serialized fields."""
        if u.dict_like(value):
            value_dict: t.JsonMapping = {}
            if isinstance(value, m.ConfigMap):
                value_dict = {str(k): str(v) for k, v in value.root.items()}
            else:
                value_dict = {str(k): str(v) for k, v in value.items()}
            metadata_dict: t.MutableJsonMapping = dict(value_dict)
            metadata_dict["_ldif_tap_metadata"] = u.Cli.normalize_json_value({
                "extraction_timestamp": datetime.now(UTC).isoformat(),
                "tap_type": "ldif_file_extractor",
                "singer_protocol": "v1.0",
                "data_source": "ldif_files",
            })
            return u.Cli.normalize_json_value(metadata_dict)
        if (
            isinstance(value, (str, int, float, bool))
            and getattr(
                self,
                "_include_ldif_metadata",
                None,
            )
            is not None
        ):
            return u.Cli.normalize_json_value({
                "value": value,
                "_ldif_context": {
                    "extracted_at": datetime.now(UTC).isoformat(),
                    "tap_name": "flext-tap-ldif",
                },
            })
        return str(value)

    @u.model_validator(mode="after")
    def validate_ldif_tap_system_consistency(self) -> Self:
        """Validate Singer LDIF tap system consistency and configuration."""
        if (
            getattr(self, "_ldif_files", None)
            and getattr(self, "LdifFile", None) is None
        ):
            msg = "LdifFile model required when LDIF files configured"
            raise ValueError(msg)

        if (
            getattr(self, "_batch_processing", None)
            and getattr(self, "LdifBatch", None) is None
        ):
            msg = "LdifBatch model required for batch processing"
            raise ValueError(msg)

        if getattr(self, "_singer_mode", None):
            required_models = ["LdifStream", "LdifRecord", "LdifProcessingState"]
            for model in required_models:
                if getattr(self, model, None) is None:
                    msg = f"{model} required for Singer protocol compliance"
                    raise ValueError(msg)

        return self

    @staticmethod
    def decode_base64_value(value: str) -> str:
        """Decode base64 encoded LDIF value."""
        try:
            return base64.b64decode(value).decode("utf-8")
        except c.Meltano.SINGER_SAFE_EXCEPTIONS:
            return value

    @staticmethod
    def normalize_attribute_name(name: str) -> str:
        """Normalize LDIF attribute name."""
        return name.lower().strip()

    @staticmethod
    def parse_dn(dn: str) -> t.StrMapping:
        """Parse Distinguished Name into components."""
        components: t.MutableStrMapping = {}
        parts = dn.split(",")
        for part in parts:
            if "=" in part:
                key, value = part.strip().split("=", 1)
                components[key.strip()] = value.strip()
        return components

    @staticmethod
    def validate_ldif_line(line: str) -> bool:
        """Validate LDIF line format."""
        return not line or line.startswith("#")
