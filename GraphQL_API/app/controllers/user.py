from typing import List, Optional

from app.database import DatabaseSession
from app.models.user import User
from app.schemas.rest.user import CreateUser


def create_user(
    new_user: CreateUser,
    db: DatabaseSession,
) -> User:
    to_insert: User = User(
        login=new_user.login,
        name=new_user.name,
        firstname=new_user.firstname,
        email=new_user.email,
        password=new_user.password,
        phone=new_user.phone,
        function=new_user.function,
        company=new_user.company,
    )
    db.add(to_insert)
    db.commit()
    db.refresh(to_insert)
    return to_insert


def get_user_by_id(user_id: int, db: DatabaseSession) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).one_or_none()


def get_all_users(db: DatabaseSession) -> List[User]:
    return db.query(User).all()
