"""Test configuration and fixtures for flext-tap-ldif tests."""

from __future__ import annotations

import os
from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def docker_control() -> FlextTestsDocker:
    """Provide Docker control instance for tests."""
    return FlextTestsDocker()


@pytest.fixture(scope="session")
def shared_ldap_container(docker_control: FlextTestsDocker) -> Generator[str]:
    """Managed LDAP container using FlextTestsDocker with auto-start."""
    result = docker_control.start_existing_container("flext-openldap-test")
    if result.is_failure:
        pytest.skip(f"Failed to start LDAP container: {result.error}")
    yield "flext-openldap-test"
    try:
        docker_control.get_client().containers.get("flext-openldap-test").stop()
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ):
        pass


@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "DEBUG"
    os.environ["SINGER_SDK_LOG_LEVEL"] = "debug"
    yield
    _ = os.environ.pop("FLEXT_ENV", None)
    _ = os.environ.pop("FLEXT_LOG_LEVEL", None)
    _ = os.environ.pop("SINGER_SDK_LOG_LEVEL", None)


@pytest.fixture
def sample_ldif_content() -> str:
    """Sample LDIF content for testing."""
    return "version: 1\n\ndn: cn=John Doe,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: John Doe\nsn: Doe\ngivenName: John\nmail: john.doe@example.com\ntelephoneNumber: +1-555-123-4567\nuserPassword:: e1NTSEF9VGVzdFBhc3N3b3JkMTIz\n\ndn: cn=Jane Smith,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: Jane Smith\nsn: Smith\ngivenName: Jane\nmail: jane.smith@example.com\ntelephoneNumber: +1-555-987-6543\n\ndn: cn=Administrators,ou=groups,dc=example,dc=com\nobjectClass: groupOfNames\ncn: Administrators\ndescription: System REDACTED_LDAP_BIND_PASSWORDistrators group\nmember: cn=John Doe,ou=users,dc=example,dc=com\nmember: cn=Jane Smith,ou=users,dc=example,dc=com\n\ndn: cn=IT Department,ou=groups,dc=example,dc=com\nobjectClass: groupOfNames\ncn: IT Department\ndescription: Information Technology department\nmember: cn=John Doe,ou=users,dc=example,dc=com\n"


@pytest.fixture
def sample_ldif_changes() -> str:
    """Sample LDIF changes content for testing."""
    return "version: 1\n\ndn: cn=John Doe,ou=users,dc=example,dc=com\nchangetype: modify\nreplace: telephoneNumber\ntelephoneNumber: +1-555-111-2222\n-\nadd: description\ndescription: Senior System Administrator\n-\n\ndn: cn=New User,ou=users,dc=example,dc=com\nchangetype: add\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: New User\nsn: User\ngivenName: New\nmail: new.user@example.com\n\ndn: cn=Old User,ou=users,dc=example,dc=com\nchangetype: delete\n"


@pytest.fixture
def sample_ldif_file(tmp_path: Path, sample_ldif_content: str) -> Path:
    """Create sample LDIF file for testing."""
    ldif_file = tmp_path / "test.ldif"
    n = ldif_file.write_text(sample_ldif_content, encoding="utf-8")
    assert n >= 0
    return ldif_file


@pytest.fixture
def sample_ldif_changes_file(tmp_path: Path, sample_ldif_changes: str) -> Path:
    """Create sample LDIF changes file for testing."""
    ldif_file = tmp_path / "changes.ldif"
    n = ldif_file.write_text(sample_ldif_changes, encoding="utf-8")
    assert n >= 0
    return ldif_file


@pytest.fixture
def ldif_directory(
    tmp_path: Path, sample_ldif_content: str, sample_ldif_changes: str
) -> Path:
    """Create directory with multiple LDIF files."""
    ldif_dir = tmp_path / "ldif_files"
    ldif_dir.mkdir()
    written = (ldif_dir / "users.ldif").write_text(
        sample_ldif_content, encoding="utf-8"
    ) + (ldif_dir / "changes.ldif").write_text(sample_ldif_changes, encoding="utf-8")
    assert written >= 0
    additional_content = "version: 1\n\ndn: cn=Test User,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: Test User\nsn: User\ngivenName: Test\nmail: test.user@example.com\n"
    _ = (ldif_dir / "additional.ldif").write_text(additional_content, encoding="utf-8")
    return ldif_dir


@pytest.fixture
def basic_tap_config(sample_ldif_file: Path) -> dict[str, object]:
    """Basic LDIF tap configuration."""
    return {
        "ldif_file_path": str(sample_ldif_file),
        "file_pattern": "*.ldif",
        "encoding": "utf-8",
        "processing_mode": "entries",
        "max_entries_per_batch": 100,
        "auto_discover_schema": True,
        "validate_entries": True,
        "enable_streaming": True,
    }


@pytest.fixture
def changes_tap_config(sample_ldif_changes_file: Path) -> dict[str, object]:
    """LDIF tap configuration for changes processing."""
    return {
        "ldif_file_path": str(sample_ldif_changes_file),
        "file_pattern": "*.ldif",
        "encoding": "utf-8",
        "processing_mode": "changes",
        "max_entries_per_batch": 50,
        "auto_discover_schema": True,
        "validate_entries": True,
        "enable_streaming": True,
    }


@pytest.fixture
def directory_tap_config(ldif_directory: Path) -> dict[str, object]:
    """LDIF tap configuration for directory processing."""
    return {
        "ldif_file_path": str(ldif_directory),
        "file_pattern": "*.ldif",
        "encoding": "utf-8",
        "processing_mode": "entries",
        "max_entries_per_batch": 100,
        "auto_discover_schema": True,
        "validate_entries": True,
        "enable_streaming": True,
        "enable_parallel_processing": True,
    }


@pytest.fixture
def filtered_tap_config(sample_ldif_file: Path) -> dict[str, object]:
    """LDIF tap configuration with filters."""
    return {
        "ldif_file_path": str(sample_ldif_file),
        "file_pattern": "*.ldif",
        "encoding": "utf-8",
        "processing_mode": "entries",
        "max_entries_per_batch": 100,
        "auto_discover_schema": True,
        "validate_entries": True,
        "include_object_classes": ["inetOrgPerson"],
        "exclude_dns": ["ou=groups"],
    }


@pytest.fixture
def large_ldif_file(tmp_path: Path) -> Path:
    """Create large LDIF file for performance testing."""
    ldif_file = tmp_path / "large.ldif"
    with ldif_file.open("w", encoding="utf-8") as f:
        _ = f.write("version: 1\n\n")
        for i in range(1000):
            _ = f.write(f"dn: cn=user{i:04d},ou=users,dc=example,dc=com\n")
            _ = f.write("objectClass: inetOrgPerson\n")
            _ = f.write("objectClass: person\n")
            _ = f.write(f"cn: user{i:04d}\n")
            _ = f.write(f"sn: User{i:04d}\n")
            _ = f.write("givenName: User\n")
            _ = f.write(f"mail: user{i:04d}@example.com\n")
            _ = f.write(f"employeeNumber: {i:04d}\n")
            _ = f.write("\n")
    return ldif_file


@pytest.fixture
def performance_tap_config(large_ldif_file: Path) -> dict[str, object]:
    """LDIF tap configuration for performance testing."""
    return {
        "ldif_file_path": str(large_ldif_file),
        "file_pattern": "*.ldif",
        "encoding": "utf-8",
        "processing_mode": "entries",
        "max_entries_per_batch": 250,
        "auto_discover_schema": True,
        "validate_entries": True,
        "enable_streaming": True,
        "buffer_size": 16384,
        "max_memory_usage": 50 * 1024 * 1024,
    }


@pytest.fixture
def binary_ldif_content() -> str:
    """LDIF content with binary attributes."""
    return "version: 1\n\ndn: cn=Binary User,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: Binary User\nsn: User\ngivenName: Binary\nmail: binary.user@example.com\nuserCertificate;binary:: MIICXjCCAcegAwIBAgIJAODNcKgAQMRAMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNVBAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBXaWRnaXRzIFB0eSBMdGQwHhcNMTgwNjA1MTI0ODM3WhcNMTkwNjA1MTI0ODM3WjBFMQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDZFQZ1ZZ1Z\njpegPhoto:: /9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIfIiEmKzcvJik0KSEiMEExNDk7Pj4+JS5ESUM8SDc9Pjv/2wBDAQoLCw4NDhwQEBw7KCIoOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozv/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k=\n"


@pytest.fixture
def binary_ldif_file(tmp_path: Path, binary_ldif_content: str) -> Path:
    """Create LDIF file with binary attributes."""
    ldif_file = tmp_path / "binary.ldif"
    _ = ldif_file.write_text(binary_ldif_content, encoding="utf-8")
    return ldif_file


@pytest.fixture
def utf16_ldif_file(tmp_path: Path) -> Path:
    """Create UTF-16 encoded LDIF file."""
    content = "version: 1\n\ndn: cn=Unicode User,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: Unicode User\nsn: Üser\ngivenName: Ünicöde\nmail: unicode.user@example.com\ndescription: User with unicode characters: àáâãäåæç\n"
    ldif_file = tmp_path / "utf16.ldif"
    _ = ldif_file.write_text(content, encoding="utf-16")
    return ldif_file


@pytest.fixture
def singer_catalog_config() -> dict[str, object]:
    """Singer catalog configuration."""
    return {
        "streams": [
            {
                "tap_stream_id": "ldif_entries",
                "schema": {
                    "type": "object",
                    "properties": {
                        "dn": {"type": "string"},
                        "source_file": {"type": "string"},
                        "source_file_mtime": {"type": "number"},
                        "objectClass": {"type": "array", "items": {"type": "string"}},
                        "cn": {"type": "array", "items": {"type": "string"}},
                        "mail": {"type": "array", "items": {"type": "string"}},
                    },
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "replication-method": "INCREMENTAL",
                            "replication-key": "source_file_mtime",
                            "selected": True,
                        },
                    }
                ],
            }
        ]
    }


@pytest.fixture
def singer_state() -> dict[str, object]:
    """Singer state for incremental sync."""
    return {
        "currently_syncing": None,
        "bookmarks": {
            "ldif_entries": {
                "replication_key_value": 1640995200.0,
                "version": 1,
                "processed_files": [],
            }
        },
    }


@pytest.fixture
def invalid_ldif_content() -> str:
    """Invalid LDIF content for error testing."""
    return "version: 1\n\ndn: cn=Invalid User,ou=users,dc=example,dc=com\nobjectClass: inetOrgPerson\nobjectClass: person\ncn: Invalid User\nsn: User\ninvalid_line_without_colon\nmail: invalid.user@example.com\n"


@pytest.fixture
def invalid_ldif_file(tmp_path: Path, invalid_ldif_content: str) -> Path:
    """Create invalid LDIF file for error testing."""
    ldif_file = tmp_path / "invalid.ldif"
    _ = ldif_file.write_text(invalid_ldif_content, encoding="utf-8")
    return ldif_file


@pytest.fixture
def benchmark_config() -> dict[str, object]:
    """Configuration for performance benchmarking."""
    return {
        "max_entries_to_process": 1000,
        "expected_processing_time": 30.0,
        "memory_limit": 100 * 1024 * 1024,
        "batch_sizes": [50, 100, 250, 500, 1000],
    }


def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "ldif: LDIF-specific tests")
    config.addinivalue_line("markers", "singer: Singer protocol tests")
    config.addinivalue_line("markers", "performance: Performance tests")
    config.addinivalue_line("markers", "binary: Binary data tests")
    config.addinivalue_line("markers", "encoding: Encoding tests")
    config.addinivalue_line("markers", "slow: Slow tests")


class MockLDIFTap:
    """Mock implementation of the LDIF Tap."""

    def __init__(self, config: dict[str, object]) -> None:
        """Initialize the instance."""
        super().__init__()
        self.config = config
        self.discovered_streams: list[dict[str, object]] = []

    def discover_streams(self) -> list[dict[str, object]]:
        return self.discovered_streams

    def sync_records(self) -> list[dict[str, object]]:
        return [
            {
                "dn": "cn=test,ou=users,dc=example,dc=com",
                "objectClass": ["inetOrgPerson", "person"],
                "cn": ["test"],
                "mail": ["test@example.com"],
                "source_file": "test.ldif",
                "source_file_mtime": 1640995200.0,
            }
        ]


@pytest.fixture
def mock_ldif_tap() -> type[MockLDIFTap]:
    """Mock LDIF tap for testing."""
    return MockLDIFTap


class MockLDIFParser:
    """Mock implementation of the LDIF Parser."""

    def __init__(self, config: dict[str, object]) -> None:
        """Initialize the instance."""
        super().__init__()
        self.config = config
        self.parsed_entries: list[dict[str, object]] = []

    def parse_file(self, _file_path: str) -> dict[str, object]:
        return {"success": True, "entries": self.parsed_entries, "errors": []}

    def add_mock_entry(self, entry: dict[str, object]) -> None:
        self.parsed_entries.append(entry)


@pytest.fixture
def mock_ldif_parser() -> type[MockLDIFParser]:
    """Mock LDIF parser for testing."""
    return MockLDIFParser
