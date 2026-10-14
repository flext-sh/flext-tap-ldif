"""Base models for flext-tap-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import m


class FlextTapLdifModelsBase:
    """Family base for the tap's Pydantic model namespaces."""

    class ConfigNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


__all__: list[str] = ["FlextTapLdifModelsBase"]
