# flext-tap-ldif - LDIF Singer Tap
PROJECT_NAME := flext-tap-ldif
include ../base.mk

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: tap-run tap-discover test-unit test-integration build shell

tap-run: ## Run tap with config
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run tap-ldif --config config.json

tap-discover: ## Run discovery mode
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run tap-ldif --config config.json --discover

.DEFAULT_GOAL := help
