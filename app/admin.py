from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram.fsm.context import FSMContext

from app.database.requests import get_users
from app.states import Newsletter

admin = Router()

class Admin(Filter):
    async def __call__(self, message: Message):
        return message.from_user.id in [1163652007]
    
@admin.message(Admin(), Command("news"))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer("Текст рассылкы:")

@admin.message(Newsletter.message)
async def newsletter_message(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Начало!")
    users = await get_users()
    #print(users)
    for user in users:
        #print(user.tg_id)
        try:
            await message.send_copy(chat_id=user.tg_id)
        except Exception as e:
            print(e)
    await message.answer("Готово!")

    
