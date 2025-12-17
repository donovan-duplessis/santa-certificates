# Makefile for Santa Certificates

.PHONY: help setup generate clean clean-build clean-pyc \
        format format-check lint lint-fix type quality quality-fix

## Show available commands
help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: clean ## Setup environment and install dependencies with uv
	uv sync --all-extras

generate: ## Generate certificates (HTML and PDF)
	./generate_pdfs.sh

clean: clean-build clean-pyc ## Remove all build and python artifacts

clean-build: ## Remove built files
	@echo "Cleaning build files..."
	@rm -rf build/

clean-pyc: ## Remove compiled python files
	@echo "Cleaning python files..."
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name '*~' -exec rm -f {} +

format: ## Format codebase with black, isort, and docformatter
	uv run isort .
	uv run black .
	uv run docformatter --in-place --recursive .

format-check: ## Check formatting without changing files
	uv run isort --check-only .
	uv run black --check .

lint: ## Lint with ruff (PEP8)
	uv run ruff check .

lint-fix: ## Lint with ruff and auto-fix issues
	uv run ruff check --fix .

type: ## Type check with mypy
	uv run mypy santa_certificates.py

quality: ## Run all quality checks (lint, type, format-check)
	@echo "Running quality checks..."
	uv run ruff check .
	uv run mypy santa_certificates.py
	uv run isort --check-only .
	uv run black --check .

quality-fix: ## Run all quality checks with auto-fix
	@echo "Running quality checks with auto-fix..."
	uv run isort .
	uv run black .
	uv run ruff check --fix .
	uv run mypy santa_certificates.py

.DEFAULT_GOAL := help
