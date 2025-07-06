from fastapi import APIRouter
from app.database import DatabaseSession
from app.schemas.user import CreateUser, CreatedUser
from app.controllers.user import create_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
def create_user_route(db: DatabaseSession, new_user: CreateUser) -> CreatedUser:
    return create_user(db, new_user)
