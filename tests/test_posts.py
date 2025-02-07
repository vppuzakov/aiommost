from aiommost.channels.schemas import Channel
from aiommost.client import MattermostClient


async def test_post_created(fake, client: MattermostClient, create_direct_channel):
    channel: Channel = await create_direct_channel()
    await client.posts.create(
        channel_id=channel.uid,
        message=fake.pystr(),
    )
