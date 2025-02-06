import orjson
from httpx import AsyncClient

from aiommost import errors
from aiommost.users.schemas import User


class UsersClient:

    def __init__(self, session: AsyncClient) -> None:
        self.session = session

    async def create(self, username: str, email: str, password: str) -> User:
        """Add new user with specified username."""
        url = '/users'
        request = {
            'username': username,
            'email': email,
            'password': password,
        }

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        user = orjson.loads(response.content)
        return User(**user)

    async def delete(self, uid: str, permanent: bool = False) -> None:
        url = f'/users/{uid}'

        response = await self.session.delete(url, params={'permanent': permanent})
        errors.validate(response)

    async def get_by_usernames(self, usernames: list[str]) -> list[User]:
        """Get users with specified usernames."""
        url = '/users/usernames'
        request = usernames

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        users = orjson.loads(response.content)
        return [User(**user) for user in users]

    async def get_by_username(self, username: str) -> User:
        """Get user with specified username."""
        url = f'/users/username/{username}'

        response = await self.session.get(url)
        errors.validate(response)

        user = orjson.loads(response.content)
        return User(**user)

    async def get_by_id(self, user_id: str) -> User:
        """Get user by id"""
        url = f'/users/{user_id}'

        response = await self.session.get(url)
        errors.validate(response)

        user = orjson.loads(response.content)
        return User(**user)
