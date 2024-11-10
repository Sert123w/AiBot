from app.database.models import async_session
from app.database.models import User, AiModel, AiType, Order
from sqlalchemy import select, update, delete, desc

from decimal import Decimal

def connection(func):
    async def inner(*arg, **kwarg):
        async with async_session() as session:
            return await func(session, *arg, **kwarg)
    return inner

#@connection
async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, balance = "0"))
            await session.commit()

async def get_user(tg_id):
    async with async_session() as session: #открываем ссессию 
        return await session.scalar(select(User).where(User.tg_id == tg_id))
    
async def calculate(tg_id, summ, model_name):
    async with async_session() as session: #открываем ссессию 
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        model = await session.scalar(select(AiModel).where(AiModel.name == model_name))
        new_balance = Decimal(user.balance) - (Decimal(model.prace)*Decimal(summ))
        
        await session.execute(update(User).where(User.id == user.id).values(balance = str(new_balance)))
        await session.commit()

async def get_users():
    async with async_session() as session: #открываем ссессию 
        return await session.scalars(select(User))