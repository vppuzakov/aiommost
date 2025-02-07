import pytest

from aiommost.channels.schemas import ChannelTypes
from aiommost.client import MattermostClient
from aiommost.users.schemas import User


@pytest.fixture
def create_direct_channel(client: MattermostClient, create_user):
    async def inner(user_id: str | None = None):
        if not user_id:
            user: User = await create_user()
            user_id = user.uid


        return await client.channels.create_direct(
            first=user_id,
            second=user_id,
        )

    return inner


@pytest.fixture
def create_channel(faker, client, create_team):
    async def inner(
        team_id: str | None = None,
        name: str | None = None,
        display_name: str | None = None,
        channel_type: ChannelTypes = ChannelTypes.PUBLIC,
        header: str | None = None,
        purpose: str | None = None,
    ):
        if not team_id:
            team = await create_team()
            team_id = team.uid

        return await client.channels.create(
            team_id=team_id,
            name=name or faker.pystr(min_chars=4, max_chars=20).lower(),
            display_name=display_name or faker.pystr(),
            channel_type=channel_type,
            header=header,
            purpose=purpose,
        )

    return inner
