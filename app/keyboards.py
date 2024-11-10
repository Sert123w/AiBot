'''from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
'''
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Чат")],
    [KeyboardButton(text="image")]
],
resize_keyboard=True, input_field_placeholder="Выберите пункт...")

cancel = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="Отмена")
]], resize_keyboard=True)