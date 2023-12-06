from sqlalchemy import create_engine, Integer, String, ForeignKey, BigInteger, select, Column, UUID
from sqlalchemy.orm import as_declarative, mapped_column, Mapped, Session, sessionmaker, declarative_base
import uuid


Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(BigInteger)


class StuffsModel(Base):
    __tablename__ = 'stuffs'
    id:Mapped[str]= mapped_column(UUID(), primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    count: Mapped[int] = mapped_column()
    price: Mapped[int] = mapped_column()


class OrdersModel(Base):
    __tablename__ = 'orders'
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    stuff_id: Mapped[int] = mapped_column(ForeignKey('stuffs.id'))
    count_stuff:Mapped[int]= mapped_column()
