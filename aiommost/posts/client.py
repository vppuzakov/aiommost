from typing import Any

import orjson
from httpx import AsyncClient

from aiommost import errors
from aiommost.posts.schemas import Post


class PostClient:

    def __init__(self, session: AsyncClient) -> None:
        self.session = session

    async def create(
        self,
        channel_id: str,
        message: str,
        root_id: str | None = None,
        file_ids: list[str] | None = None,
        props: dict[str, Any] | None = None,
    ) -> Post:
        """Create new post in the channel."""
        url = "/posts"
        request = {
            "channel_id": channel_id,
            "message": message,
            "root_id": root_id,
            "file_ids": file_ids,
            "props": props,
        }

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        post = orjson.loads(response.content)
        return Post(**post)
