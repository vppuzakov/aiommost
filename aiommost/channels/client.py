import orjson
from httpx import AsyncClient

from aiommost import errors
from aiommost.channels.schemas import Channel, ChannelTypes


class ChannelsClient:

    def __init__(self, session: AsyncClient) -> None:
        self.session = session

    async def create_direct(self, first: str, second: str) -> Channel:
        """Create direct channel between users."""
        url = "/channels/direct"
        request = [first, second]

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        channel = orjson.loads(response.content)
        return Channel(**channel)

    async def create(self,
                     team_id: str,
                     name: str,
                     display_name: str,
                     channel_type: ChannelTypes,
                     purpose: str | None = None,
                     header: str | None = None) -> Channel:
        """Create public or private channel."""
        url = "/channels"
        request = {
            "team_id": team_id,
            "name": name,
            "display_name": display_name,
            "purpose": purpose,
            "header": header,
            "type": channel_type.value,
        }

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        channel = orjson.loads(response.content)
        return Channel(**channel)

    async def get_by_id(self, channel_id: str) -> Channel:
        """Get channel info by channel id."""
        url = f"/channels/{channel_id}"

        response = await self.session.get(url)
        errors.validate(response)

        channel = orjson.loads(response.content)
        return Channel(**channel)
