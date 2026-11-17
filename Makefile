
.PHONY: build test test-all prepare

ENV ?= dev
BROWSER ?= chromium
MODULE ?= tests/
PYTEST_ARGS ?=

export LOCAL_UID ?= $(shell id -u)
export LOCAL_GID ?= $(shell id -g)
export TEST_ENV_FILE ?= .env.$(ENV)

COMPOSE = docker compose

prepare:
	mkdir -p reports test-results

build:
	$(COMPOSE) build

test: prepare
	$(COMPOSE) run --rm playwright \
		python -m pytest $(MODULE) \
		--env=$(ENV) \
		--browser $(BROWSER) \
		$(PYTEST_ARGS)

test-all: prepare
	$(COMPOSE) run --rm playwright \
		python -m pytest $(MODULE) \
		--env=$(ENV) \
		--browser chromium \
		--browser firefox \
		--browser webkit \
		$(PYTEST_ARGS)
