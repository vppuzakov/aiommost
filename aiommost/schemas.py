from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Schema(BaseModel):

    class Config:  # noqa: WPS431
        allow_population_by_field_name = True


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


class User(Schema):
    uid: str = Field(alias='id')
    username: str
    email: str
    firstname: str = Field(alias='first_name')
    lastname: str = Field(alias='last_name')
    nickname: str
