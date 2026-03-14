"""Test module for flext-tap-ldif.

This module provides test infrastructure for flext-tap-ldif with subnamespaces .Tests
following FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from algar_oud_mig import p, u
from algar_oud_mig.protocols import p
from algar_oud_mig.utilities import u
from docker.images.support.quality.simple.flext_core import p, u
from fix import p
from flext_api import p, u
from flext_api.protocols import p
from flext_api.utilities import u
from flext_auth import p, u
from flext_auth.protocols import p
from flext_auth.utilities import u
from flext_cli import p, u
from flext_cli.protocols import p
from flext_cli.utilities import u
from flext_core import p, u
from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr
from flext_core.protocols import p
from flext_core.utilities import u
from flext_db_oracle import p, u
from flext_db_oracle.protocols import p
from flext_db_oracle.utilities import u
from flext_dbt_ldap import p, u
from flext_dbt_ldap.protocols import p
from flext_dbt_ldap.utilities import u
from flext_dbt_ldif import p, u
from flext_dbt_ldif.protocols import p
from flext_dbt_oracle import p, u
from flext_dbt_oracle.protocols import p
from flext_dbt_oracle.utilities import u
from flext_dbt_oracle_wms.protocols import p
from flext_dbt_oracle_wms.utilities import u
from flext_grpc import p, u
from flext_grpc.protocols import p
from flext_grpc.utilities import u
from flext_infra import p, u
from flext_infra.protocols import p
from flext_infra.refactor import u
from flext_infra.refactor.transformers.policy import u
from flext_infra.utilities import u
from flext_ldap import p, u
from flext_ldap.protocols import p
from flext_ldap.utilities import u
from flext_ldif import p, u
from flext_ldif._models.domain import p, u
from flext_ldif._utilities.oid import u
from flext_ldif.protocols import p
from flext_ldif.utilities import u
from flext_meltano import p, u
from flext_meltano.file_managers import u
from flext_meltano.protocols import p
from flext_meltano.utilities import u
from flext_observability import p, u
from flext_observability.protocols import p
from flext_observability.utilities import u
from flext_oracle_oic import p, u
from flext_oracle_oic.protocols import p
from flext_oracle_oic.utilities import u
from flext_oracle_wms import p, u
from flext_oracle_wms.protocols import p
from flext_oracle_wms.utilities import u
from flext_plugin import p, u
from flext_plugin.protocols import p
from flext_plugin.utilities import u
from flext_quality import p, u
from flext_quality.protocols import p
from flext_quality.utilities import u
from flext_tap_ldap import p, u
from flext_tap_ldap.protocols import p
from flext_tap_ldap.utilities import u
from flext_tap_oracle import p, u
from flext_tap_oracle.protocols import p
from flext_tap_oracle.utilities import u
from flext_tap_oracle_oic import p, u
from flext_tap_oracle_oic.protocols import p
from flext_tap_oracle_oic.utilities import u
from flext_tap_oracle_wms import p
from flext_tap_oracle_wms.protocols import p
from flext_target_ldap import p, u
from flext_target_ldap.protocols import p
from flext_target_ldap.utilities import u
from flext_target_ldif import p, u
from flext_target_ldif.protocols import p
from flext_target_ldif.utilities import u
from flext_target_oracle import p, u
from flext_target_oracle.protocols import p
from flext_target_oracle.utilities import u
from flext_target_oracle_oic.protocols import p
from flext_target_oracle_oic.utilities import u
from flext_target_oracle_wms import p, u
from flext_target_oracle_wms.protocols import p
from flext_target_oracle_wms.utilities import u
from flext_tests import p, tm, tt, u
from flext_tests.factories import tt
from flext_tests.matchers import tm
from flext_tests.protocols import p
from flext_tests.typings import tt
from flext_tests.utilities import u
from flext_web import p, u
from flext_web.protocols import p
from flext_web.utilities import u
from gruponos_meltano_native import p, u
from gruponos_meltano_native.protocols import p
from gruponos_meltano_native.utilities import u
from multipart import p
from paramiko.util import u
from rich.panel import p
from scripts.acl_converter import u
from scripts.acl_converter.utilities import u
from scripts.stress_test import u
from scripts.stress_test.utilities import u
from src.algar_oud_mig.protocols import p
from src.algar_oud_mig.utilities import u
from src.flext_api.protocols import p
from src.flext_api.utilities import u
from src.flext_auth.protocols import p
from src.flext_auth.utilities import u
from src.flext_cli.protocols import p
from src.flext_cli.utilities import u
from src.flext_core.protocols import p
from src.flext_core.utilities import u
from src.flext_db_oracle.protocols import p
from src.flext_db_oracle.utilities import u
from src.flext_dbt_ldap.protocols import p
from src.flext_dbt_ldap.utilities import u
from src.flext_dbt_ldif import p, u
from src.flext_dbt_ldif.protocols import p
from src.flext_dbt_oracle.protocols import p
from src.flext_dbt_oracle.utilities import u
from src.flext_dbt_oracle_wms.protocols import p
from src.flext_dbt_oracle_wms.utilities import u
from src.flext_grpc.protocols import p
from src.flext_grpc.utilities import u
from src.flext_infra.protocols import p
from src.flext_infra.utilities import u
from src.flext_ldap.protocols import p
from src.flext_ldap.utilities import u
from src.flext_ldif._models.domain import p, u
from src.flext_ldif._utilities.oid import u
from src.flext_ldif.protocols import p
from src.flext_ldif.utilities import u
from src.flext_meltano.file_managers import u
from src.flext_meltano.protocols import p
from src.flext_meltano.utilities import u
from src.flext_observability.protocols import p
from src.flext_observability.utilities import u
from src.flext_oracle_oic.protocols import p
from src.flext_oracle_oic.utilities import u
from src.flext_oracle_wms.protocols import p
from src.flext_oracle_wms.utilities import u
from src.flext_plugin.protocols import p
from src.flext_plugin.utilities import u
from src.flext_quality.protocols import p
from src.flext_quality.utilities import u
from src.flext_tap_ldap.protocols import p
from src.flext_tap_ldap.utilities import u
from src.flext_tap_ldif.protocols import p
from src.flext_tap_ldif.utilities import u
from src.flext_tap_oracle.protocols import p
from src.flext_tap_oracle.utilities import u
from src.flext_tap_oracle_oic.protocols import p
from src.flext_tap_oracle_oic.utilities import u
from src.flext_tap_oracle_wms.protocols import p
from src.flext_target_ldap.protocols import p
from src.flext_target_ldap.utilities import u
from src.flext_target_ldif.protocols import p
from src.flext_target_ldif.utilities import u
from src.flext_target_oracle.protocols import p
from src.flext_target_oracle.utilities import u
from src.flext_target_oracle_oic.protocols import p
from src.flext_target_oracle_oic.utilities import u
from src.flext_target_oracle_wms.protocols import p
from src.flext_target_oracle_wms.utilities import u
from src.flext_tests.factories import tt
from src.flext_tests.matchers import tm
from src.flext_tests.protocols import p
from src.flext_tests.utilities import u
from src.flext_web.protocols import p
from src.flext_web.utilities import u
from src.gruponos_meltano_native.protocols import p
from src.gruponos_meltano_native.utilities import u

from flext_tap_ldif import p, u
from flext_tap_ldif.protocols import p
from flext_tap_ldif.utilities import u
from tests import p, tm, tt, u
from tests.fixtures.namespace_validator import u
from tests.fixtures.namespace_validator.rule1_magic_number import u
from tests.helpers import p, u
from tests.helpers.protocols import p
from tests.helpers.utilities import u
from tests.infra import p, u
from tests.infra.protocols import p
from tests.infra.utilities import u
from tests.integration import p, u
from tests.integration.test_refactor_policy_mro import p, u
from tests.models import tm
from tests.protocols import p
from tests.test_helpers import tm
from tests.test_helpers_core import u
from tests.tp import p
from tests.tu import u
from tests.typings import tt
from tests.unit import p, u
from tests.unit.test_automated_utilities import u
from tests.unit.test_protocols import p
from tests.unit.test_utilities import u
from tests.utilities import u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "p": ("protocols", "p"),
    "tm": ("models", "m"),
    "tt": ("typings", "t"),
    "u": ("utilities", "u"),
}
p
tm
tt
u
__all__ = ["p", "tm", "tt", "u"]


def __getattr__(name: str):
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
