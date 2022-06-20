-include .env
export

dev.install:
	@flit install --deps develop --symlink

lint:
	@flake8 aiommost
	@mypy aiommost

test:
	@pytest

build: clean
	@flit build --no-setup-py

clean:
	@rm -rf dist

publish: build
	@flit publish
