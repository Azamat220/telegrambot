from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

async def process_photo_command(message: types.Message):
    photo = open('image/img.png', 'rb')
    await bot.send_photo(message.chat.id, photo)

async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Сколько нот в октаве?"
    answer = [
        "Где то 10",
        "Что такое октава?",
        "7",
        "8",
        "Я иду смотреть тт"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ниче страшного",
        open_period=10,
        reply_markup=markup
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_photo_command,commands=['photo'])
    dp.register_message_handler(quiz_1, commands=['quiz'])

