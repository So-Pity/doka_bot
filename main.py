import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(
        text="Wait a minute..Who...ARE..You?"
    )
    if message.text in ['Pipiska', 'Пиписька']:
        await message.reply(text="Pipiska detected")  #Will be easter egg

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())