-include .env
export


dev.activate:
	@python3 -m hatch -v -e ${env} shell


deps.outdated:
	@python3 -m pip list --outdated


ci.install.tool:
	@python3 -m pip install -q -U --index-url=${PIP_INDEX_URL} hatch


ci.build: clean
	@python3 -m hatch build


lint:
	@python3 -m hatch -v run lint:all aiommost
	@python3 -m hatch -v run lint:all tests


test:
	@python3 -m hatch -v run test.py${PYTHON_VERSION}:test ${args}


clean:
	@rm -rf dist


publish: build
	@python3 -m hatch publish
