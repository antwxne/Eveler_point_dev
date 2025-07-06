from typing import Optional

from pydantic import BaseModel


class CreateUser(BaseModel):
    login: str
    name: str
    firstname: str
    password: str
    email: str
    phone: Optional[str] = None
    function: Optional[str] = None
    company: Optional[str] = None


class CreatedUser(BaseModel):
    id: int
    login: str
    name: str
    firstname: str
    email: str
    phone: Optional[str] = None
    function: Optional[str] = None
    company: Optional[str] = None
