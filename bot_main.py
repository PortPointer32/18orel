import subprocess

from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from create_main_bot import dp
from cfg.database import Database
from main_telegram_bot import Admin

db = Database('/home/str/18orel/cfg/database')


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def main():
    Admin.register_handler_admin(dp)

    executor.start_polling(dp, on_shutdown=shutdown)


if __name__ == '__main__':
    # subprocess.Popen(["/home/str/Alica/.venv/bin/python", "/home/str/Alica/telegram_bot/monitor.py"])
    subprocess.Popen(["/home/str/18orel/.venv/bin/python", "/home/str/18orel/telegram_bot/monitor.py"])

    main()
