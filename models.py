from sqlalchemy import create_engine, Integer, String, ForeignKey, BigInteger, select
from sqlalchemy.orm import as_declarative, mapped_column, Mapped, Session, sessionmaker
import uuid


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column( autoincrement=True, primary_key=True)


class UserModel(AbstractModel):
    __tablename__ = "users"
    name: Mapped[str]= mapped_column()
    fullname: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(BigInteger)


class StuffsModel(AbstractModel):
    __tablename__ = 'stuffs'
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    count: Mapped[int]=  mapped_column()
    price: Mapped[int] = mapped_column()


class OrdersModel(AbstractModel):
    __tablename__ = 'orders'
    user_id:Mapped[int]= mapped_column(ForeignKey('users.id'))
    staff_id:Mapped[int]= mapped_column(ForeignKey('stuffs.id'))


