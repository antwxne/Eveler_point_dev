# from typing import List

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import Mapped, relationship

# from app.database import Base
# from app.models.user import User


# class Client(Base):
#     __tablename__ = "clients"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
#     name = Column(String, index=True, unique=True)
#     users: Mapped[List[User]] = relationship(back_populates="client")
