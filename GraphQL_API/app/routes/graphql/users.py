from typing import List, Optional

import strawberry

from app.controllers.client import get_client_by_name
from app.controllers.user import get_all_users, get_user_by_id
from app.database import DatabaseSession
from app.schemas.graphql.user import Client, User


@strawberry.type
class Query:
    @strawberry.field
    def users(self, info: strawberry.Info) -> List[User]:
        db: DatabaseSession = info.context["db"]
        return get_all_users(db)

    @strawberry.field
    def user(self, id: int, info: strawberry.Info) -> Optional[User]:
        db: DatabaseSession = info.context["db"]
        return get_user_by_id(id, db)  # type: ignore

    @strawberry.field
    def client(self, name: str, info: strawberry.Info) -> Optional[Client]:
        db: DatabaseSession = info.context["db"]
        a = get_client_by_name(db, name)
        return a
