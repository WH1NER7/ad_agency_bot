from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from os import getenv

from sys import exit
import logging

from bot.database.main import MongoDBConnection
from bot.handlers.main import register_all_handlers


async def __on_start_up(dp: Dispatcher) -> None:
    connection = MongoDBConnection(host='localhost', port=27017, db_name='ad_agency')
    await connection.connect()
    dp.bot.data['db_connection'] = connection  # Сохраняем экземпляр в объекте bot.data

    register_all_handlers(dp)


def start_bot():
    bot_token = getenv("BOT_TOKEN")
    if not bot_token:
        exit("Error: no token provided")
    bot = Bot(token=bot_token, parse_mode="HTML")
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)


