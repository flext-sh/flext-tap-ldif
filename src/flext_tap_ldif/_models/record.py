"""Record, validation, and performance models for LDIF tap."""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from flext_tap_ldif import t, u
from flext_tap_ldif.models import m


class FlextTapLdifModelsRecord:
    """MRO mixin: LdifRecord, LdifValidationResult, LdifPerformanceMetrics."""

    class LdifValidationResult(m.EnforcedModel):
        """LDIF validation result with detailed error reporting."""

        model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
        )

        file_path: Annotated[str, u.Field(..., description="Validated LDIF file path")]
        valid: Annotated[bool, u.Field(..., description="Overall validation result")]

        # Validation results
        validation_errors: Annotated[
            t.SequenceOf[t.StrMapping],
            u.Field(
                description="Validation errors with details",
            ),
        ] = u.Field(default_factory=tuple)
        warnings: Annotated[
            t.SequenceOf[t.StrMapping],
            u.Field(
                description="Validation warnings",
            ),
        ] = u.Field(default_factory=tuple)

        # Statistics
        total_entries: Annotated[
            t.NonNegativeInt,
            u.Field(description="Total entries validated"),
        ] = 0
        valid_entries: Annotated[
            t.NonNegativeInt,
            u.Field(description="Valid entries count"),
        ] = 0
        invalid_entries: Annotated[
            t.NonNegativeInt,
            u.Field(description="Invalid entries count"),
        ] = 0

        # Validation metadata
        validation_time: Annotated[
            t.NonNegativeFloat,
            u.Field(
                description="Validation time in seconds",
            ),
        ] = 0.0
        validator_version: Annotated[str, u.Field(description="Validator version")] = (
            "1.0"
        )

        @u.computed_field()
        @property
        def validation_summary(self) -> t.JsonMapping:
            """LDIF validation complete summary."""
            success_rate = 0.0
            if self.total_entries > 0:
                success_rate = self.valid_entries / self.total_entries

            return {
                "file_path": self.file_path,
                "validation_result": "valid" if self.valid else "invalid",
                "statistics": {
                    "total_entries": self.total_entries,
                    "valid_entries": self.valid_entries,
                    "invalid_entries": self.invalid_entries,
                    "success_rate": success_rate,
                },
                "issues": {
                    "error_count": len(self.validation_errors),
                    "warning_count": len(self.warnings),
                    "has_critical_errors": any(
                        error.get("severity") == "critical"
                        for error in self.validation_errors
                    ),
                },
                "performance": {
                    "validation_time_seconds": self.validation_time,
                    "entries_per_second": self.total_entries / self.validation_time
                    if self.validation_time > 0
                    else 0,
                },
            }

        @u.model_validator(mode="after")
        def validate_result_consistency(self) -> Self:
            """Validate result consistency."""
            if self.valid_entries + self.invalid_entries != self.total_entries:
                msg = "Valid + invalid entries must equal total entries"
                raise ValueError(msg)
            if self.valid and self.validation_errors:
                msg = "Cannot be valid with validation errors"
                raise ValueError(msg)
            return self
