from pydantic import BaseModel


class Schema(BaseModel):

    class Config:
        allow_population_by_field_name = True
