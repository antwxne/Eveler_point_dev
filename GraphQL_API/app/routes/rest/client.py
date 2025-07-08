from fastapi import APIRouter

from app.controllers.client import create_client
from app.database import DatabaseSession
from app.models.user import User
from app.schemas.rest.client import CreateClient, CreatedClient

router = APIRouter(prefix="/client", tags=["client"])


@router.post("/")
def create_client_route(new_user: CreateClient, bd: DatabaseSession) -> CreatedClient:
    created_client: User = create_client(bd, new_user.name)
    return CreatedClient(id=created_client.id, name=created_client.name)
