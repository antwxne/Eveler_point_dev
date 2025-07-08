from typing import Any

import strawberry
from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyLoader

from app.database import get_db
from app.routes.graphql import users


async def get_context(
    db_con=Depends(get_db),
) -> dict[str, Any]:
    return {"db": db_con, "sqlalchemy_loader": StrawberrySQLAlchemyLoader(db_con)}


router = GraphQLRouter(
    schema=strawberry.Schema(query=users.Query), context_getter=get_context
)
