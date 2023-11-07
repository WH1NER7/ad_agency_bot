from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb_markup = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb_button1 = KeyboardButton("Узнать о нас больше")
start_kb_button2 = KeyboardButton("Кейсы")
start_kb_button3 = KeyboardButton("Формы сотрудничества")
start_kb_markup.add(start_kb_button1, start_kb_button2, start_kb_button3)
