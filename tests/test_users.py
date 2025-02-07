import pytest

from aiommost.client import MattermostClient
from aiommost.errors import BadRequestError
from aiommost.users.schemas import User


async def test_user_created(client: MattermostClient, fake):
    username, email, password = fake.pystr().lower(), fake.email(), fake.password()

    user = await client.users.create(username, email, password)
    assert user.username == username


async def test_user_deleted(client: MattermostClient, fake):
    username, email, password = fake.pystr(), fake.email(), fake.password()

    user = await client.users.create(username, email, password)

    await client.users.delete(user.uid)


async def test_get_by_username_found(client: MattermostClient, create_user):
    existing_user: User = await create_user()

    user = await client.users.get_by_username(existing_user.username)
    assert user.username == existing_user.username


async def test_get_by_username_not_found(fake, client: MattermostClient):
    with pytest.raises(BadRequestError):
        await client.users.get_by_username(fake.pystr())


async def test_get_by_usernames(client: MattermostClient, create_user):
    first_user: User = await create_user()
    second_user: User = await create_user()

    users = await client.users.get_by_usernames([first_user.username, second_user.username])
    assert len(users) == 2


async def test_get_by_id_found(client: MattermostClient, create_user):
    existing_user: User = await create_user()

    user = client.users.get_by_id(existing_user.uid)
    assert existing_user.uid == user.uid


async def test_get_by_id_not_found(fake, client: MattermostClient):
    with pytest.raises(BadRequestError):
        await client.users.get_by_id(fake.pystr())
