import orjson
from httpx import Response, codes


class ClientError(Exception):
    """Mattermost client error."""


class BadRequestError(ClientError):
    """Bad request error."""

    def __init__(self, code: str, message: str, detailed: str, request_id: str) -> None:
        super().__init__(f'[{request_id}] {message}')
        self.code = code
        self.request_id = request_id
        self.message = message
        self.detailed = detailed


def validate(response: Response) -> None:
    if response.status_code == codes.BAD_REQUEST:
        error = orjson.loads(response.content)
        raise BadRequestError(
            code=error['id'],
            request_id=error['request_id'],
            message=error['message'],
            detailed=error['detailed_error'],
        )

    response.raise_for_status()
