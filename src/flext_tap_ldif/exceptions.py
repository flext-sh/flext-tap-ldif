"""LDIF tap exception hierarchy using flext-core DRY patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Domain-specific exceptions using direct inheritance from flext-core.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextExceptions, FlextTypes

# Use flext-core exception classes directly for proper type safety
FlextTapLdifError = FlextExceptions.Error
FlextTapLdifValidationError = FlextExceptions.ValidationError
FlextTapLdifConfigurationError = FlextExceptions.ConfigurationError
FlextTapLdifConnectionError = FlextExceptions.ConnectionError
FlextTapLdifProcessingError = FlextExceptions.ProcessingError
FlextTapLdifAuthenticationError = FlextExceptions.AuthenticationError
FlextTapLdifTimeoutError = FlextExceptions.TimeoutError


class FlextTapLdifParseError(FlextExceptions.BaseError):
    """LDIF tap parsing errors with LDIF-specific context."""

    @override
    def __init__(
        self,
        message: str = "LDIF tap parsing failed",
        *,
        file_path: str | None = None,
        line_number: int | None = None,
        entry_dn: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF tap parse error with LDIF-specific context."""
        # Store LDIF-specific attributes before extracting common kwargs
        self.file_path = file_path
        self.line_number = line_number
        self.entry_dn = entry_dn

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with LDIF parse-specific fields
        context = self._build_context(
            base_context,
            file_path=file_path,
            line_number=line_number,
            entry_dn=entry_dn,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF tap parse: {message}",
            code=error_code or "TAP_LDIF_PARSE_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTapLdifFileError(FlextExceptions.BaseError):
    """LDIF tap file operation errors with file-specific context."""

    @override
    def __init__(
        self,
        message: str = "LDIF tap file error",
        *,
        file_path: str | None = None,
        operation: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF tap file error with file-specific context."""
        # Store file-specific attributes before extracting common kwargs
        self.file_path = file_path
        self.operation = operation

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with file operation-specific fields
        context = self._build_context(
            base_context,
            file_path=file_path,
            operation=operation,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF tap file: {message}",
            code=error_code or "TAP_LDIF_FILE_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


class FlextTapLdifStreamError(FlextExceptions.BaseError):
    """LDIF tap stream processing errors with stream-specific context."""

    @override
    def __init__(
        self,
        message: str = "LDIF tap stream error",
        *,
        stream_name: str | None = None,
        file_path: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF tap stream error with stream-specific context."""
        # Store stream-specific attributes before extracting common kwargs
        self.stream_name = stream_name
        self.file_path = file_path

        # Extract common parameters using helper
        base_context, correlation_id, error_code = self._extract_common_kwargs(kwargs)

        # Build context with stream-specific fields
        context = self._build_context(
            base_context,
            stream_name=stream_name,
            file_path=file_path,
        )

        # Call parent with complete error information
        super().__init__(
            f"LDIF tap stream: {message}",
            code=error_code or "TAP_LDIF_STREAM_ERROR",
            context=context,
            correlation_id=correlation_id,
        )


__all__: FlextTypes.StringList = [
    "FlextTapLdifConfigurationError",
    "FlextTapLdifError",
    "FlextTapLdifFileError",
    "FlextTapLdifParseError",
    "FlextTapLdifProcessingError",
    "FlextTapLdifStreamError",
    "FlextTapLdifValidationError",
]
