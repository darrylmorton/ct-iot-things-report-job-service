.DEFAULT_GOAL := build

fmt:
	poetry run ruff format .
.PHONY:fmt

lint: fmt
	poetry run ruff check . --fix
.PHONY:lint

dev-server-start: fmt
	poetry run uvicorn --log-level=debug src.things_report_job_service.service:server --reload --port 8001
.PHONY:dev-server-start

server-start: fmt
	poetry run uvicorn src.things_report_job_service.service:server --port 8001 &
.PHONY:server-start

test-unit: fmt
	poetry run pytest tests/unit
.PHONY:test-unit

test-integration: fmt
	poetry run pytest tests/integration
.PHONY:test-integration

test: fmt
	poetry run pytest tests
.PHONY:test

test-integration: fmt
	poetry run pytest tests/integration
.PHONY:test-integration

test-integration-with-server: server-start
	poetry run pytest tests/integration
.PHONY:test-integration-with-server

test: fmt
	poetry run pytest tests
.PHONY:test