from pydantic import Field

from aiommost.schemas import Schema


class User(Schema):
    uid: str = Field(alias='id')
    username: str
    email: str
    firstname: str = Field(alias='first_name')
    lastname: str = Field(alias='last_name')
    nickname: str
