from aiogram import Bot, Dispatcher
from decouple import config

Token = config('Token')

bot = Bot(Token)
dp = Dispatcher(bot=bot)
ADMINS=(1045935241)