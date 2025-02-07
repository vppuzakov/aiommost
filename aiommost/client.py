import httpx

from aiommost.channels.client import ChannelsClient
from aiommost.posts.client import PostClient
from aiommost.users.client import UsersClient


class MattermostClient:

    def __init__(self, host: str, token: str, verify: bool | str = True) -> None:
        self.token = token
        self.verify = verify

        self.session = httpx.AsyncClient(
            base_url=f"{host}/api/v4",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            verify=verify,
        )

        self.channels = ChannelsClient(self.session)
        self.posts = PostClient(self.session)
        self.users = UsersClient(self.session)

    async def close(self) -> None:
        await self.session.aclose()
