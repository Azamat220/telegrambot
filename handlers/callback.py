from aiogram import types , Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("ELSE", callback_data="button_2")
    markup.add(button_2)

    question = "Площадь квадрата через диагональ"
    answer = [
        "d*d/2",
        "root d / 4",
        "d*d",
        "d",
        "r*r/2"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Амей",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):

    question = "Лучшие курсы программирования"
    answer = [
        "Attractor",
        "Geeks",
        "Ogogo",
        "Makers",
        "Best"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Туй Ата ",
        open_period=10
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")