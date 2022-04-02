# aiommost

Asyncio Mattermost client. Useful to write bots.

## Contributing Guide

Main dependencies:

- `httpx`
- `pydantic`

Developer dependencies:

- `mypy`
- `wemake-python-styleguide`
- `pytest`

Install dependencies:

```bash
make dev.install
```

Before push:

```bash
$ make lint && make test
...
```

