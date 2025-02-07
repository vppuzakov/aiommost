from aiommost.client import MattermostClient


async def test_direct_channel_created(client: MattermostClient, create_user):
    user = await create_user()
    await client.channels.create_direct(user.uid, user.uid)
