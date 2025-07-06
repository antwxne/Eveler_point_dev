from typing import List

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from app.controllers.user import get_all_users, get_user_by_id
from app.database import get_db
from app.models import user as model

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(model.User)
class User:
    __exclude__ = ["password"]


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        db = next(get_db())
        return get_all_users(db)

    @strawberry.field
    def user(self, id: int) -> User:
        db = next(get_db())
        return get_user_by_id(id, db)


router = GraphQLRouter(schema=strawberry.Schema(query=Query))
