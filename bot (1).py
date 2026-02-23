import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

logging.basicConfig(level=logging.INFO)

TOKEN    = os.environ["BOT_TOKEN"]
GAME_URL = os.environ.get("GAME_URL", "https://cosmicliker.netlify.app")

bot = Bot(token=TOKEN)
dp  = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🚀 Играть в Cosmic Clicker",
            web_app=WebAppInfo(url=GAME_URL)
        )
    ]])
    await message.answer(
        "👋 Привет, космонавт!\n\n"
        "⚡ Собирай энергию, строй генераторы и покоряй вселенную!\n\n"
        "Нажми кнопку ниже чтобы начать 👇",
        reply_markup=kb
    )

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
