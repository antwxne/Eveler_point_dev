from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import Base, engine
from app.routes.graphql.router import router as graphql_router
from app.routes.rest import client as rest_client
from app.routes.rest import users as rest_users

load_dotenv()

app = FastAPI()
app.include_router(rest_users.router)
app.include_router(rest_client.router)
app.include_router(graphql_router)


@app.get("/healthcheck")
async def ping():
    return "OK"


Base.metadata.create_all(engine)
