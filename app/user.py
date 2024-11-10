from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.keyboards as kb
from app.states import Chat, Image
from aiogram.fsm.context import FSMContext

from app.generators import gpt_text_test, gpt_image
from app.database.requests import set_user, get_user, calculate

from decimal import Decimal

user = Router()

@user.message(F.text == "Отмена")
@user.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await message.answer("Добро пожаловать!", reply_markup= kb.main)
    await state.clear()

@user.message(F.text == "Чат")
async def chatting(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Chat.text)
        await message.answer("Введите запрос", reply_markup= kb.cancel)
    else:
        await message.answer("Нет монеу")

@user.message(Chat.text)
async def chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        state.set_state(Chat.wait)
        # response = await gpt_text(message.text, "gpt-3.5")
        response = await gpt_text_test()

        await calculate(message.from_user.id, response['usage'], "GPT-3.5")
    
        await message.answer(response["response"], reply_markup= kb.cancel)
        await state.set_state(Chat.text)
        #await state.clear()
    else:
        await message.answer("Нет монеу")

@user.message(Image.wait)
@user.message(Chat.wait)
async def wait_wait(message: Message):
    await message.answer("Подожди минутку...")
#--------------------------------------------------------------------------------------

@user.message(F.text == "image")
async def chatting(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(Image.text)
        await message.answer("Введите запрос", reply_markup= kb.cancel)
    else:
        await message.answer("Нет монеу")

@user.message(Image.text)
async def chat_response(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        state.set_state(Image.wait)
        # response = await gpt_text(message.text, "gpt-3.5")
        response = await gpt_image()

        await calculate(message.from_user.id, response['usage'], "dall-e-3")

        print(response)
        
        try:
            await message.answer_photo(photo=response["response"], reply_markup= kb.cancel)
        except Exception as e:
            print(e)
            await state.set_state(Image.text)
        #await state.clear()
    else:
        await message.answer("Нет монеу")





