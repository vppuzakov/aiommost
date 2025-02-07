import pytest

from aiommost.teams.schemas import TeamTypes


@pytest.fixture
def create_team(faker, client):
    async def inner(
        name: str | None = None,
        display_name: str | None = None,
        team_type: TeamTypes = TeamTypes.PUBLIC,
    ):
        return await client.teams.create(
            name=name or faker.pystr(min_chars=10, max_chars=20).lower(),
            display_name=display_name or faker.pystr(),
            team_type=team_type,
        )

    return inner
