import httpx

from aiommost.channels import ChannelsClient
from aiommost.users import UsersClient


class MattermostClient:

    def __init__(self, host: str, token: str) -> None:
        self.token = token

        self.session = httpx.AsyncClient(
            base_url=f'{host}/api/v4',
            headers={
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            },
        )

        self.channels = ChannelsClient(self.session)
        self.users = UsersClient(self.session)

    async def close(self) -> None:
        await self.session.aclose()
