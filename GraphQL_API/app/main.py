from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import Base, engine
from app.routes.graphql import users as graphql_users
from app.routes.rest import users as rest_users

load_dotenv()

app = FastAPI()
app.include_router(rest_users.router, prefix="/users", tags=["Users"])
app.include_router(graphql_users.router, prefix="/graphql", tags=["GraphQL"])


@app.get("/")
async def ping():
    return "OK"


Base.metadata.create_all(engine)
