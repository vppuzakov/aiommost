-include .env
export

dev.install:
	@flit install --deps develop --symlink

lint:
	@flake8 aiommost
	@mypy aiommost

test:
	@pytest

build:
	@flit build --no-setup-py
	@chmod 444 dist/*

publish:
	@flit publish
