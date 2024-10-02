import asyncio
import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from handlers import user_router
from aiogram import Bot, Dispatcher

async def main() -> None:
    """Запуск бота и Обработка Роутеров"""
    dp = Dispatcher()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode='HTML'))
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
        print("Bot started")
    except KeyboardInterrupt:
        print("Bot stopped")
