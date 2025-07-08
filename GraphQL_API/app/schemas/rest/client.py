from pydantic import BaseModel


class CreateClient(BaseModel):
    name: str


class CreatedClient(BaseModel):
    id: int
    name: str
