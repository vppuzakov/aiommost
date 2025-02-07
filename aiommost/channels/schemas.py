from datetime import datetime

from pydantic import Field

from aiommost.schemas import Schema


class Channel(Schema):
    uid: str = Field(alias="id")
    team_id: str
    category: str = Field(alias="type")
    name: str
    display_name: str
    header: str
    purpose: str
    msg_count: int | None = Field(alias="total_msg_count")
    creator_id: str
    last_post_at: datetime
