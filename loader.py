from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from database.db_sqlite import Database


TOKEN = '6555890706:AAGG-_uXI4GD567DzHX3wjyCz-gmr6REtYc'
ADMIN = 5945737121

dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
db = Database(path_to_db='database/main.db')
