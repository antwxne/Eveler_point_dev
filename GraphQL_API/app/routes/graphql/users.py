from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.controllers.user import get_all_users, get_user_by_id
from app.database import get_db


@strawberry.type
class User:
    id: strawberry.ID
    name: str
    firstname: str

    @strawberry.field
    def first_user(root) -> "User":
        return User(id=0, name="OUI", firstname="NON")  # type: ignore


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        db = next(get_db())

        return [
            User(id=user.id, name=user.name, firstname=user.firstname)  # type: ignore
            for user in get_all_users(db)
        ]

    @strawberry.field
    def user(self, id: int) -> User:
        db = next(get_db())
        user = get_user_by_id(id, db)
        return User(id=user.id, name=user.name, firstname=user.firstname)  # type: ignore


router = GraphQLRouter(schema=strawberry.Schema(query=Query))
