import pytest

from aiommost.client import MattermostClient


@pytest.fixture
def create_user(client: MattermostClient, fake):
    async def inner(username: str | None = None,
                    email: str | None = None,
                    password: str | None = None):
        return await client.users.create(
            username=username or fake.pystr().lower(),
            email=email or fake.email(),
            password=password or fake.password(),
        )

    return inner
