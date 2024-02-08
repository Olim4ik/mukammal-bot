from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command(commands=['command']))
async def bot_command(message: types.Message):
    await message.answer(
        f"Custom command with no function yet. {message.from_user.full_name}")
