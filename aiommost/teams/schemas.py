from enum import Enum

from pydantic import Field

from aiommost.schemas import Schema


class TeamTypes(Enum):
    PUBLIC = "O"
    PRIVATE = "P"


class Team(Schema):
    uid: str = Field(alias="id")
    name: str
    display_name: str
    description: str
    type: TeamTypes
