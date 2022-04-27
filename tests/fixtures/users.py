import pytest

from aiommost.client import MattermostClient


@pytest.fixture()
def create_user(client: MattermostClient, fake):
    async def inner(username: str = None, email: str = None, password: str = None):
        return await client.users.create(
            username=username or fake.pystr().lower(),
            email=email or fake.email(),
            password=password or fake.password(),
        )

    return inner
