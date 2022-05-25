from pydantic import Field

from aiommost.schemas import Schema


class Post(Schema):
    uid: str = Field(alias='id')
    user_id: str
    channel_id: str
    root_id: str
    original_id: str
    message: str
