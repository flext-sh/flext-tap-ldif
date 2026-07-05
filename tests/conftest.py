"""Test configuration and fixtures for flext-tap-ldif tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from tests.utilities import u

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    with u.Tests.env_vars_context({
        "FLEXT_ENV": "test",
        "FLEXT_LOG_LEVEL": "DEBUG",
        "SINGER_SDK_LOG_LEVEL": "debug",
    }):
        yield
