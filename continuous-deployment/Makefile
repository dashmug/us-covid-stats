# colors
BLUE:=$(shell echo "\033[0;36m")
GREEN:=$(shell echo "\033[0;32m")
YELLOW:=$(shell echo "\033[0;33m")
RED:=$(shell echo "\033[0;31m")
END:=$(shell echo "\033[0m")

PHONY: deploy
deploy:
	@echo "$(BLUE)Updating stack...$(END)"
	@aws cloudformation deploy \
	--template-file cloudformation.yml \
	--stack-name us-covid-stats-deployment \
	--capabilities CAPABILITY_IAM \
	--parameter-overrides GitHubRepo=${REPO} GitHubBranch=${BRANCH} \
	--no-fail-on-empty-changeset

PHONY: validate
validate:
	@aws cloudformation validate-template --template-body file://cloudformation.yml


PHONY: lint
lint:
	@cfn-lint cloudformation.yml
