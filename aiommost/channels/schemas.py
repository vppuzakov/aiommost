from datetime import datetime
from typing import Optional

from pydantic import Field

from aiommost.schemas import Schema


class Channel(Schema):
    uid: str = Field(alias='id')
    team_id: str
    category: str = Field(alias='type')
    name: str
    display_name: str
    header: str
    purpose: str
    msg_count: Optional[int] = Field(alias='total_message_count')
    creator_id: str
    last_post_at: datetime
