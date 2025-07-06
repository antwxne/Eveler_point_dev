from typing import List

import strawberry
from fastapi import Depends
from strawberry.fastapi import GraphQLRouter

from app.controllers.user import get_all_users, get_user_by_id
from app.database import get_db


async def get_context(
    db_con=Depends(get_db),
):
    return {
        "db": db_con,
    }


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    firstname: str

    @strawberry.field
    def first_user(root, info: strawberry.Info) -> "User":
        db = info.context["db"]
        user = get_user_by_id(int(root.id), db)
        return User(id=user.id, name=user.name, firstname=user.firstname)  # type: ignore


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info: strawberry.Info) -> List[User]:
        db = info.context["db"]

        return [
            User(id=user.id, name=user.name, firstname=user.firstname)  # type: ignore
            for user in get_all_users(db)
        ]

    @strawberry.field
    def user(self, id: int, info: strawberry.Info) -> User:
        db = info.context["db"]
        user = get_user_by_id(id, db)
        return User(id=user.id, name=user.name, firstname=user.firstname)  # type: ignore


router = GraphQLRouter(
    schema=strawberry.Schema(query=Query), context_getter=get_context
)
