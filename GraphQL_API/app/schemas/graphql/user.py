from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from app.models.user import Client as ClientModel
from app.models.user import User as UserModel

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(UserModel)
class User:
    __exclude__ = ["password"]


@strawberry_sqlalchemy_mapper.type(ClientModel)
class Client: ...


strawberry_sqlalchemy_mapper.finalize()
