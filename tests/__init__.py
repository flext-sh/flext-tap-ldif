"""Test module for flext-tap-ldif.

This module provides test infrastructure for flext-tap-ldif with subnamespaces .Tests
following FLEXT ecosystem patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from .models import m as tm
from .protocols import p as p
from .typings import t as tt
from .utilities import u as u

__all__ = [
    "tm",
    "p",
    "tt",
    "u",
]
