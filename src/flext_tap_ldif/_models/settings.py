"""Configuration models for LDIF tap."""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
    model_validator,
)

from flext_core import FlextConstants
from flext_tap_ldif import t


class FlextTapLdifModelsSettings:
    """MRO mixin: LdifTapConfig model."""

    class LdifTapConfig(BaseModel):
        """Configuration for LDIF tap operations."""

        model_config: ClassVar[ConfigDict] = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "LDIF tap configuration with complete settings",
                "examples": [
                    {
                        "ldif_directory": "/data/ldif",
                        "file_patterns": ["*.ldif"],
                        "batch_size": 1000,
                    },
                ],
            },
        )

        # File configuration
        ldif_directory: Annotated[
            str | None,
            Field(
                default=None,
                description="LDIF files directory",
            ),
        ]
        file_patterns: Annotated[
            t.StrSequence,
            Field(
                description="LDIF file patterns",
            ),
        ] = Field(default_factory=lambda: ["*.ldif"])
        recursive_search: Annotated[
            bool,
            Field(
                default=False,
                description="Recursive directory search",
            ),
        ]

        # Processing configuration
        batch_size: Annotated[
            int,
            Field(
                default=FlextConstants.DEFAULT_SIZE,
                description="Processing batch size",
            ),
        ]
        parallel_processing: Annotated[
            bool,
            Field(
                default=False,
                description="Enable parallel processing",
            ),
        ]
        max_workers: Annotated[
            t.WorkerCount,
            Field(default=4, description="Maximum worker threads"),
        ]

        # Error handling
        continue_on_error: Annotated[
            bool,
            Field(
                default=True,
                description="Continue processing on errors",
            ),
        ]
        max_errors: Annotated[
            int,
            Field(
                default=FlextConstants.DEFAULT_SIZE,
                description="Maximum errors before stopping",
            ),
        ]
        error_file: Annotated[
            str | None,
            Field(default=None, description="Error output file"),
        ]

        # Output configuration
        output_format: Annotated[
            str,
            Field(default="jsonl", description="Output format"),
        ]
        include_metadata: Annotated[
            bool,
            Field(
                default=True,
                description="Include processing metadata",
            ),
        ]
        compress_output: Annotated[
            bool,
            Field(
                default=False,
                description="Compress output files",
            ),
        ]

        @computed_field
        def tap_config_summary(self) -> t.ContainerMapping:
            """LDIF tap configuration summary."""
            patterns: t.ContainerList = list(self.file_patterns)
            source: t.ContainerMapping = {
                "directory": self.ldif_directory,
                "patterns": patterns,
                "recursive": self.recursive_search,
            }
            processing: t.ContainerMapping = {
                "batch_size": self.batch_size,
                "parallel": self.parallel_processing,
                "max_workers": self.max_workers,
            }
            error_handling: t.ContainerMapping = {
                "continue_on_error": self.continue_on_error,
                "max_errors": self.max_errors,
                "has_error_file": bool(self.error_file),
            }
            output: t.ContainerMapping = {
                "format": self.output_format,
                "include_metadata": self.include_metadata,
                "compressed": self.compress_output,
            }
            result: t.ContainerMapping = {
                "source": source,
                "processing": processing,
                "error_handling": error_handling,
                "output": output,
            }
            return result

        @model_validator(mode="after")
        def validate_tap_config(self) -> Self:
            """Validate LDIF tap configuration."""
            if self.batch_size <= 0:
                msg = "Batch size must be positive"
                raise ValueError(msg)
            if self.max_workers <= 0:
                msg = "Max workers must be positive"
                raise ValueError(msg)
            return self
