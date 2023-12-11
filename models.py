from sqlalchemy import create_engine, Integer, String, ForeignKey, BigInteger, select, Column, types, text, UUID
from sqlalchemy.orm import as_declarative, mapped_column, Mapped, Session, sessionmaker, declarative_base, relationship
import uuid


@as_declarative()
class AbstractModel:
    # id: Mapped[uuid.UUID] = mapped_column(
    #     types.Uuid,
    #     default=uuid.uuid4(),
    #     primary_key=True,
    #    # init=False,
    #     server_default=text("gen_random_uuid()")

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class UserModel(AbstractModel):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(BigInteger)


class StuffsModel(AbstractModel):
    __tablename__ = 'stuffs'
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    count: Mapped[int] = mapped_column()
    price: Mapped[int] = mapped_column()


class OrdersModel(AbstractModel):
    __tablename__ = 'orders'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    stuff_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'))
    count_stuff: Mapped[int] = mapped_column()

    stuff = relationship("StuffsModel", backref='order')