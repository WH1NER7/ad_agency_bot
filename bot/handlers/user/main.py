from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.database.main import MongoDBConnection
# from bot.database.methods.get import check_link
# from bot.database.methods.insert import create_user
# from bot.database.methods.update import upd_link
from bot.keyboards.inline import markup_lk, more_info_markup, cases_markup, cooperation_markup
from bot.keyboards.reply import start_kb_markup
# from bot.utils.misc import determine_uniqueness

db = MongoDBConnection(db_name="ad_agency")


class UpdLink(StatesGroup):
    waiting_link = State()


async def start(message: Message):
    user_real_name = message.from_user.first_name
    user_second_name = message.from_user.last_name
    user_link_nice = message.from_user.username

    user_id = message.from_user.id

    connection = message.bot.data['db_connection']
    await connection.insert_data(collection_name="users_info",
                                 data={'tg_id': user_id, "link": user_link_nice, "start": True, "percentage": "1/15"})

    # create_user(user_real_name, user_second_name, user_id, user_link_nice)
    await message.answer("Приветствие", reply_markup=start_kb_markup)
    await message.answer("Приветствие c доп информацией", reply_markup=markup_lk)
    # await message.("", reply_markup=)


async def more_info_mes(message: Message):
    await message.answer("Мы мы мы", reply_markup=more_info_markup)


async def cases_mes(message: Message):
    await message.answer("Кратко о кейсах", reply_markup=cases_markup)


async def cooperation_forms_mes(message: Message):
    await message.answer("Тарифы и форматы сотрудничества", reply_markup=cooperation_markup)


async def more_info(callback: CallbackQuery):
    await callback.message.edit_text("Мы мы мы", reply_markup=more_info_markup)


async def cases_info(callback: CallbackQuery):
    await callback.message.edit_text("Кратко о кейсах", reply_markup=cases_markup)


async def form_of_cooperation(callback: CallbackQuery):
    await callback.message.edit_text("Тарифы и форматы сотрудничества", reply_markup=cooperation_markup)


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(more_info_mes, content_types=['text'], text="Узнать о нас больше")
    dp.register_message_handler(cases_mes, content_types=['text'], text="Кейсы")
    dp.register_message_handler(cooperation_forms_mes, content_types=['text'], text="Формы сотрудничества")

    dp.register_callback_query_handler(more_info, lambda c: c.data == 'faq')
    dp.register_callback_query_handler(cases_info, lambda c: c.data == 'cases')
    dp.register_callback_query_handler(form_of_cooperation, lambda c: c.data == 'form_of_cooperation')

