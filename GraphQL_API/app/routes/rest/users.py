from typing import List, Optional

from fastapi import APIRouter, HTTPException

from app.controllers.user import create_user, get_all_users, get_user_by_id
from app.database import DatabaseSession
from app.models.user import User
from app.schemas.rest.user import CreatedUser, CreateUser

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/")
def create_user_route(new_user: CreateUser, bd: DatabaseSession) -> CreatedUser:
    created_user: User = create_user(new_user, bd)
    return CreatedUser(
        id=created_user.id,
        email=created_user.email,
        login=created_user.login,
        name=created_user.name,  # type: ignore
        firstname=created_user.firstname,
        phone=created_user.phone,
        function=created_user.function,
        company=created_user.company,
        client_id=created_user.client_id,
    )


@router.get("/")
def get_users_route(bd: DatabaseSession) -> List[CreatedUser]:
    return [
        CreatedUser(
            id=user.id,
            email=user.email,
            login=user.login,
            name=user.name,  # type: ignore
            firstname=user.firstname,
            phone=user.phone,
            function=user.function,
            company=user.company,
            client_id=user.client_id,
        )
        for user in get_all_users(bd)
    ]


@router.get("/{user_id}")
def get_user_by_id_route(user_id: int, bd: DatabaseSession) -> CreatedUser:
    user: Optional[User] = get_user_by_id(user_id, bd)
    if user is None:
        raise HTTPException(status_code=404, detail="user_id not found")
    return CreatedUser(
        id=user.id,
        email=user.email,
        login=user.login,
        name=user.name,  # type: ignore
        firstname=user.firstname,
        phone=user.phone,
        function=user.function,
        company=user.company,
        client_id=user.client_id,
    )
