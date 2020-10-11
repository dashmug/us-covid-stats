# colors
BLUE:=$(shell echo "\033[0;36m")
GREEN:=$(shell echo "\033[0;32m")
YELLOW:=$(shell echo "\033[0;33m")
RED:=$(shell echo "\033[0;31m")
END:=$(shell echo "\033[0m")


.PHONY: help
help: ## Show help (default).
	@echo "$(YELLOW)*** US COVID Stats (Backend) ***$(END)"
	@echo
	@echo "make options:"
	@grep -E '^[ .a-zA-Z0-9_-]+:.*?## .*$$' Makefile | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-24s\033[0m %s\n", $$1, $$2}'


.PHONY: venv
venv: ## Install python dependencies.
	@poetry install


node_modules: ## Install node dependencies.
	@yarn install --frozen-lockfile


.PHONY: install
install: venv node_modules ## Setup project for local development.


.PHONY: shell
shell: ## Run interactive python shell (ipython).
	@poetry run ipython


.PHONY: autopep8
autopep8: ## Auto-format using autopep8.
	@poetry run autopep8 --in-place us_covid_stats/*.py


.PHONY: black
black: ## Auto-format using black.
	@poetry run black .


.PHONY: format
format: autopep8 black ## Auto-format the project source code.


.PHONY: flake8
flake8: ## Lint using flake8.
	@poetry run flake8 .


.PHONY: black_check
black_check: ## Lint using black.
	@poetry run black . --check


.PHONY: lint
lint: flake8 black_check ## Lint the project source code.


.PHONY: typecheck
typecheck: ## Check type annotations.
	@poetry run mypy


.PHONY: clean
clean: ## Delete the deployment package.
	@rm -rf .serverless


.PHONY: build
build: clean ## Build the deployment package.
	@yarn build


.PHONY: deploy
deploy: build ## Deploy the backend services.
	@yarn deploy
