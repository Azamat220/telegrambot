from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Token = config('Token')

bot = Bot(Token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
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

@dp.callback_query_handler(text="button_1")
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


@dp.callback_query_handler(text="button_2")
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

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    photo = open('image/img.png', 'rb')
    await bot.send_photo(message.chat.id, photo)
    # caption = 'Какие глазки! :eyes:'
    # await bot.send_photo(message.from_user.id, CAT_BIG_EYES,
    #                      caption=caption,
    #                      reply_to_message_id=message.message_id)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"{int(message.text)**2}")
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Мой господин {message.from_user.full_name}")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
