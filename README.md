# aiommost

Asyncio Mattermost client. Useful to write bots.

## Usage

```python
from aiommost import MattermostClient

client = MattermostClient(host, token)

# create direct channel
user = await client.users.get_by_username('someuser')
channel = await client.channels.direct(user.uid, user.uid)
```

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
