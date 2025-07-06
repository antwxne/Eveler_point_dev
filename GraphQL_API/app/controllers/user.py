from app.schemas.user import CreateUser
from app.database import DatabaseSession
from app.models.user import User


def create_user(db: DatabaseSession, new_user: CreateUser) -> User:
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
