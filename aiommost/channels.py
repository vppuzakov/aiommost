import orjson
from httpx import AsyncClient

from aiommost import errors, schemas


class ChannelsClient:

    def __init__(self, session: AsyncClient) -> None:
        self.session = session

    async def create_direct(self, first: str, second: str) -> schemas.Channel:
        """Create direct channel between users."""
        url = '/channels/direct'
        request = [first, second]

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        channel = orjson.loads(response.content)
        return schemas.Channel(**channel)
