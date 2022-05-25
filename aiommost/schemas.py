from pydantic import BaseModel


class Schema(BaseModel):

    class Config:  # noqa: WPS431
        allow_population_by_field_name = True
