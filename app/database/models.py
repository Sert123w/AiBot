from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from datetime import datetime
from config import DB_URL

engine = create_async_engine(url=DB_URL, #создание подключения
                             echo=True) #все действия логируются в терминале
    
async_session = async_sessionmaker(engine)#создали объект подключения 


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    balance: Mapped[str] =mapped_column(String(15))

class AiType(Base):
    __tablename__ = "ai_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

class AiModel(Base):
    __tablename__ = "ai_models"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    ai_types: Mapped[int] = mapped_column(ForeignKey("ai_types.id"))
    prace: Mapped[str] = mapped_column(String(25))

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(25)) 
    user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[str] = mapped_column(String(50))
    create_at: Mapped[datetime]
    order: Mapped[str] = mapped_column(String(50))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
