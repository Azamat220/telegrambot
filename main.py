from aiogram.utils import executor
from config import dp
from handlers import client, callback, end
import logging

callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
end.register_handlers_end(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
