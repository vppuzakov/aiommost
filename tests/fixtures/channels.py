import pytest

from aiommost.client import MattermostClient
from aiommost.users.schemas import User


@pytest.fixture()
def create_direct_channel(client: MattermostClient, create_user):
    async def inner(user_id: str = None):
        if not user_id:
            user: User = await create_user()
            user_id = user.uid

        return await client.channels.create_direct(
            first=user_id,
            second=user_id,
        )

    return inner
