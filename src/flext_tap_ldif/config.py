"""Configuration for FLEXT Tap LDIF using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import ConfigDict, Field, field_validator

from flext_core import FlextModels, FlextResult
from flext_meltano import validate_directory_path, validate_file_path

# Constants for validation limits
MAX_BATCH_SIZE = 10000
MAX_FILE_SIZE_MB = 1000


class TapLDIFConfig(FlextModels.Config):
    """Configuration for the LDIF tap with optimized Python 3.13+ patterns."""

    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        validate_default=True,
        extra="forbid",
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
        default=1000,
        ge=1,
        le=MAX_BATCH_SIZE,
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
        default=100,
        ge=1,
        le=MAX_FILE_SIZE_MB,
        description="Maximum file size in MB to process",
    )

    @field_validator("file_path")
    @classmethod
    def validate_file_path_field(cls, v: str | None) -> str | None:
        """Use consolidated file path validation."""
        return validate_file_path(v)

    @field_validator("directory_path")
    @classmethod
    def validate_directory_path_field(cls, v: str | None) -> str | None:
        """Use consolidated directory path validation."""
        return validate_directory_path(v)

    def model_post_init(self, __context: object, /) -> None:
        """Validate configuration after initialization using FlextConfig.BaseModel pattern."""
        super().model_post_init(__context)

        # Delegate to business rules validation
        validation_result = self.validate_business_rules()
        if validation_result.is_failure:
            raise ValueError(validation_result.error)

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate LDIF tap configuration business rules."""
        # Validate input sources using FlextResult chaining
        return (
            self._validate_input_sources()
            .flat_map(lambda _: self._validate_constraints())
            .flat_map(lambda _: self._validate_filters())
        )

    def _validate_input_sources(self) -> FlextResult[None]:
        """Validate input source configuration."""
        if not any([self.file_path, self.file_pattern, self.directory_path]):
            return FlextResult[None].fail(
                "At least one input source must be specified: file_path, file_pattern, or directory_path",
            )
        return FlextResult[None].ok(None)

    def _validate_constraints(self) -> FlextResult[None]:
        """Validate configuration constraints."""
        # Validate batch size constraints
        if self.batch_size <= 0:
            return FlextResult[None].fail("Batch size must be positive")
        if self.batch_size > MAX_BATCH_SIZE:
            return FlextResult[None].fail(f"Batch size cannot exceed {MAX_BATCH_SIZE}")

        # Validate file size constraints
        if self.max_file_size_mb <= 0:
            return FlextResult[None].fail("Max file size must be positive")
        if self.max_file_size_mb > MAX_FILE_SIZE_MB:
            return FlextResult[None].fail(
                f"Max file size cannot exceed {MAX_FILE_SIZE_MB} MB",
            )

        # Validate encoding
        if not self.encoding:
            return FlextResult[None].fail("Encoding must be specified")

        return FlextResult[None].ok(None)

    def _validate_filters(self) -> FlextResult[None]:
        """Validate filter configuration."""
        if self.attribute_filter and self.exclude_attributes:
            overlapping = set(self.attribute_filter) & set(self.exclude_attributes)
            if overlapping:
                return FlextResult[None].fail(
                    f"Attributes cannot be both included and excluded: {overlapping}",
                )
        return FlextResult[None].ok(None)

    @property
    def ldif_config(self) -> dict[str, object]:
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
