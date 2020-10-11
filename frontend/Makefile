# colors
BLUE:=$(shell echo "\033[0;36m")
GREEN:=$(shell echo "\033[0;32m")
YELLOW:=$(shell echo "\033[0;33m")
RED:=$(shell echo "\033[0;31m")
END:=$(shell echo "\033[0m")


.PHONY: help
help: ## Show help (default).
	@echo "$(YELLOW)*** US COVID Stats (Frontend) ***$(END)"
	@echo
	@echo "make options:"
	@grep -E '^[ .a-zA-Z0-9_-]+:.*?## .*$$' Makefile | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-24s\033[0m %s\n", $$1, $$2}'


node_modules: ## Install node dependencies.
	@yarn install --frozen-lockfile


.PHONY: install
install: node_modules ## Setup project for local development.


.PHONY: build
build: ## Build production artifact.
	@$(eval REACT_APP_BACKEND_URL:=$(shell aws ssm get-parameter --name REACT_APP_BACKEND_URL --query Parameter.Value --output text))
	@REACT_APP_BACKEND_URL=$(REACT_APP_BACKEND_URL) npm run build


.PHONY: deploy
deploy: build ## Deploy the frontend.
	@$(eval FRONTEND_BUCKET:=$(shell aws ssm get-parameter --name FRONTEND_BUCKET --query Parameter.Value --output text))
	@aws s3 sync build s3://$(FRONTEND_BUCKET) --delete
	@$(eval FRONTEND_DISTRIBUTION:=$(shell aws ssm get-parameter --name FRONTEND_DISTRIBUTION --query Parameter.Value --output text))
	@aws cloudfront create-invalidation --distribution-id=$(FRONTEND_DISTRIBUTION) --paths=/*
