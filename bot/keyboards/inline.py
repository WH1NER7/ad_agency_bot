from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup_lk = InlineKeyboardMarkup(row_width=1)
inline_btn_1 = InlineKeyboardButton('Узнать о нас больше', callback_data='faq')
inline_btn_2 = InlineKeyboardButton('Кейсы', callback_data='cases')
inline_btn_3 = InlineKeyboardButton('Формы сотрудничества', callback_data='form_of_cooperation')
markup_lk.add(inline_btn_1, inline_btn_2, inline_btn_3)


more_info_markup = InlineKeyboardMarkup(row_width=1)
more_info_markup.add(inline_btn_3, inline_btn_2)

cases_markup = InlineKeyboardMarkup(row_width=1)
case_btn_1 = InlineKeyboardButton('Кейс 1', callback_data='case1')
case_btn_2 = InlineKeyboardButton('Кейс 2', callback_data='case2')
case_btn_3 = InlineKeyboardButton('Кейс 3', callback_data='case3')
case_btn_4 = InlineKeyboardButton('Сотрудничать с нами', callback_data='cooperate_with_us')
cases_markup.add(case_btn_1, case_btn_2, case_btn_3, case_btn_4)


cooperation_markup = InlineKeyboardMarkup(row_width=1)
cooperation_markup.add(case_btn_4)


# markup_competition = InlineKeyboardMarkup(row_width=1)
# competition_btn_1 = InlineKeyboardButton('Добавить ссылку на Reels', callback_data='reels_link')
# markup_competition.add(competition_btn_1)
#
# markup_link = InlineKeyboardMarkup(row_width=1)
# link_btn_1 = InlineKeyboardButton('Хочу изменить', callback_data='reels_link_upd')
# markup_link.add(link_btn_1)