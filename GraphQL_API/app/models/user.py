from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    login = Column(String, index=True, unique=True)
    name = Column(String)
    firstname = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String, nullable=True, default=None)
    function = Column(String, nullable=True, default=None)
    company = Column(String, nullable=True, default=None)
