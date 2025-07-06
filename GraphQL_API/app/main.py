from dotenv import load_dotenv
from fastapi import FastAPI

from app.database import Base, engine
from app.routes import user

load_dotenv()

app = FastAPI()
app.include_router(user.router)


@app.get("/")
async def ping():
    return "OK"


Base.metadata.create_all(engine)
