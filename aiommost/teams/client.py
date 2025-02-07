import orjson
from httpx import AsyncClient

from aiommost import errors
from aiommost.teams.schemas import Team, TeamTypes


class TeamClient:

    def __init__(self, session: AsyncClient) -> None:
        self.session = session

    async def create(self, name: str, display_name: str, team_type: TeamTypes) -> Team:
        """Create public or private team."""
        url = "/teams"
        request = {
            "name": name,
            "display_name": display_name,
            "type": team_type.value,
        }

        response = await self.session.post(url, content=orjson.dumps(request))
        errors.validate(response)

        team = orjson.loads(response.content)
        return Team(**team)
