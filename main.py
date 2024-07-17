import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

BOT_TOKEN = "7097305320:AAFT0Vn7W__zE2w-IpUPS0FgRQtNFYyVoms"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher

print(bot)
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())