from typing import List

from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(UUID, primary_key=True, index=True, autoincrement=True, unique=True)
    name = Column(String, index=True, unique=True)
    users: Mapped[List["User"]] = relationship(back_populates="client")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True, autoincrement=True, unique=True)
    login = Column(String, index=True, unique=True)
    name = Column(String)
    firstname = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String, nullable=True, default=None)
    function = Column(String, nullable=True, default=None)
    company = Column(String, nullable=True, default=None)
    client_id = mapped_column(ForeignKey("clients.id"))
    client: Mapped[Client] = relationship(back_populates="users", single_parent=True)
