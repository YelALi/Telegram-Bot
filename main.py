import asyncio
from aiogram import Bot,Dispatcher

from app.handlers import router
from app.database.models import async_main

async def main():
    bot = Bot(token='7267530430:AAFankrHPD-zlp9V79Uj_teq8_m5c8ndqvk')
    dp=Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
