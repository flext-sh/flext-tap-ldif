"""Configuration for FLEXT Tap LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Self

from flext_core import (
    FlextConfig,
    FlextConstants,
    FlextResult,
    FlextUtilities,
)
from pydantic import Field, field_validator
from pydantic_settings import SettingsConfigDict


class FlextMeltanoTapLdifConfig(FlextConfig):
    """Configuration for the LDIF tap with optimized Python 3.13+ patterns."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TAP_LDIF_",
        case_sensitive=False,
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        use_enum_values=True,
        validate_assignment=True,
        validate_default=True,
        frozen=False,
        str_strip_whitespace=True,
    )

    # File Input Configuration - using Python 3.13+ type union syntax
    file_path: str | None = Field(
        default=None,
        description="Path to the LDIF file to extract data from",
    )

    file_pattern: str | None = Field(
        default=None,
        description="Pattern for multiple LDIF files (e.g., '*.ldif')",
    )

    directory_path: str | None = Field(
        default=None,
        description="Directory containing LDIF files",
    )

    # Filtering Configuration with optimized defaults
    base_dn_filter: str | None = Field(
        default=None,
        description="Filter entries by base DN pattern",
    )

    object_class_filter: list[str] = Field(
        default_factory=list,
        description="Filter entries by object class",
    )

    attribute_filter: list[str] = Field(
        default_factory=list,
        description="Include only specified attributes",
    )

    exclude_attributes: list[str] = Field(
        default_factory=list,
        description="Exclude specified attributes",
    )

    # Processing Configuration with proper constraints
    encoding: str = Field(default="utf-8", description="File encoding (default: utf-8)")

    batch_size: int = Field(
        default=FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE,
        ge=1,
        le=FlextConstants.Performance.MAX_BATCH_SIZE_VALIDATION,
        description="Number of entries to process in each batch",
    )

    include_operational_attributes: bool = Field(
        default=False,
        description="Include operational attributes in output",
    )

    strict_parsing: bool = Field(
        default=True,
        description="Enable strict LDIF parsing (fail on errors)",
    )

    max_file_size_mb: int = Field(
        default=FlextConstants.Logging.MAX_FILE_SIZE // (1024 * 1024),
        ge=1,
        le=FlextConstants.Logging.MAX_FILE_SIZE // (1024 * 1024),  # Convert bytes to MB
        description="Maximum file size in MB to process",
    )

    @field_validator("file_path")
    @classmethod
    def validate_file_path_field(cls, v: str | None) -> str | None:
        """Use consolidated file path validation."""
        result = FlextUtilities.Validation.validate_file_path(v)
        return result.data if result.success else None

    @field_validator("directory_path")
    @classmethod
    def validate_directory_path_field(cls, v: str | None) -> str | None:
        """Use consolidated directory path validation."""
        result = FlextUtilities.Validation.validate_directory_path(v)
        return result.data if result.success else None

    def model_post_init(self, __context: object, /) -> None:
        """Validate configuration after initialization using FlextConfig.BaseModel pattern."""
        super().model_post_init(__context)

        # Delegate to business rules validation
        validation_result: FlextResult[object] = self.validate_business_rules()
        if validation_result.is_failure:
            raise ValueError(validation_result.error)

    def validate_business_rules(self: object) -> FlextResult[None]:
        """Validate LDIF tap configuration business rules."""
        # Validate input sources using FlextResult chaining
        return (
            self._validate_input_sources()
            .flat_map(lambda _: self._validate_constraints())
            .flat_map(lambda _: self._validate_filters())
        )

    def _validate_input_sources(self: object) -> FlextResult[None]:
        """Validate input source configuration."""
        if not any([self.file_path, self.file_pattern, self.directory_path]):
            return FlextResult[None].fail(
                'At least one input source must be specified: "file_path", "file_pattern", or "directory_path"',
            )
        return FlextResult[None].ok(None)

    def _validate_constraints(self: object) -> FlextResult[None]:
        """Validate configuration constraints."""
        # Validate batch size constraints
        if self.batch_size <= 0:
            return FlextResult[None].fail("Batch size must be positive")
        max_batch = FlextConstants.Performance.MAX_BATCH_SIZE_VALIDATION
        if self.batch_size > max_batch:
            return FlextResult[None].fail(f"Batch size cannot exceed {max_batch}")

        # Validate file size constraints
        if self.max_file_size_mb <= 0:
            return FlextResult[None].fail("Max file size must be positive")
        max_file_mb = FlextConstants.Logging.MAX_FILE_SIZE // (1024 * 1024)
        if self.max_file_size_mb > max_file_mb:
            return FlextResult[None].fail(
                f"Max file size cannot exceed {max_file_mb} MB",
            )

        # Validate encoding
        if not self.encoding:
            return FlextResult[None].fail("Encoding must be specified")

        return FlextResult[None].ok(None)

    def _validate_filters(self: object) -> FlextResult[None]:
        """Validate filter configuration."""
        if self.attribute_filter and self.exclude_attributes:
            overlapping = set(self.attribute_filter) & set(self.exclude_attributes)
            if overlapping:
                return FlextResult[None].fail(
                    f"Attributes cannot be both included and excluded: {overlapping}",
                )
        return FlextResult[None].ok(None)

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-tap-ldif")

    @classmethod
    def create_for_development(cls, **overrides: object) -> Self:
        """Create development configuration instance."""
        dev_defaults = {
            "file_path": "./test.ldif",
            "batch_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 10,
            "strict_parsing": False,
            "max_file_size_mb": 10,
            "encoding": "utf-8",
        }
        dev_defaults.update(overrides)
        return cls(**dev_defaults)

    @classmethod
    def create_for_production(cls, **overrides: object) -> Self:
        """Create production configuration instance."""
        prod_defaults = {
            "batch_size": FlextConstants.Performance.BatchProcessing.MAX_ITEMS // 2,
            "strict_parsing": True,
            "max_file_size_mb": 500,
            "include_operational_attributes": False,
        }
        prod_defaults.update(overrides)
        return cls(**prod_defaults)

    @classmethod
    def create_for_testing(cls, **overrides: object) -> Self:
        """Create testing configuration instance."""
        test_defaults = {
            "file_path": "./tests/test_data/sample.ldif",
            "batch_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 20,
            "strict_parsing": True,
            "max_file_size_mb": 1,
            "encoding": "utf-8",
        }
        test_defaults.update(overrides)
        return cls(**test_defaults)

    @property
    def ldif_config(self: object) -> dict[str, object]:
        """Get LDIF-specific configuration as a dictionary."""
        return {
            "file_path": self.file_path,
            "file_pattern": self.file_pattern,
            "directory_path": self.directory_path,
            "base_dn_filter": self.base_dn_filter,
            "object_class_filter": self.object_class_filter,
            "attribute_filter": self.attribute_filter,
            "exclude_attributes": self.exclude_attributes,
            "encoding": self.encoding,
            "batch_size": self.batch_size,
            "include_operational_attributes": self.include_operational_attributes,
            "strict_parsing": self.strict_parsing,
            "max_file_size_mb": self.max_file_size_mb,
        }


# Export main configuration class
__all__ = [
    "FlextMeltanoTapLdifConfig",
]
