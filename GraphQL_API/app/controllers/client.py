from typing import Optional

from app.database import DatabaseSession
from app.models.user import Client


def create_client(db: DatabaseSession, name: str) -> Client:
    client = Client(name=name)
    db.add(client)
    db.commit()
    db.refresh(client)
    return client


def get_client_by_name(db: DatabaseSession, name: str) -> Optional[Client]:
    return db.query(Client).filter(Client.name == name).one_or_none()
