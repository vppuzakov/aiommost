import pytest

from aiommost import errors
from aiommost.client import MattermostClient


async def test_direct_channel_created(client: MattermostClient, create_user):
    user = await create_user()
    await client.channels.create_direct(user.uid, user.uid)


async def test__get_by_id__found_channel(client, create_channel):
    existing = await create_channel()
    channel = await client.channels.get_by_id(channel_id=existing.uid)
    assert channel.uid == existing.uid


async def test__get_by_id__not_found_channel(client, create_channel, not_existing_id):
    with pytest.raises(errors.BadRequestError):
        await client.channels.get_by_id(channel_id=not_existing_id)
