from aiommost.client import MattermostClient
from aiommost import schemas


async def test_direct_channel_created(client: MattermostClient, create_user):
    user: schemas.User = await create_user()
    await client.channels.create_direct(user.uid, user.uid)
