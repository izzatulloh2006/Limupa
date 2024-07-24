# import os
# import yt_dlp
# import sqlite3
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils import executor
#
# TELEGRAM_TOKEN = '6644465503:AAHne_9_Gcxf3qIxk-apCttbx92GWq707-E'
# ADMIN_ID = '918485944'
#
# bot = Bot(token=TELEGRAM_TOKEN)
# dp = Dispatcher(bot)
#
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         username TEXT,
#         first_name TEXT,
#         last_name TEXT
#     )
# ''')
# conn.commit()
#
# def add_user(user):
#     cursor.execute('''
#         INSERT OR IGNORE INTO users (id, username, first_name, last_name)
#         VALUES (?, ?, ?, ?)
#     ''', (user.id, user.username, user.first_name, user.last_name))
#     conn.commit()
#
# def get_user_count():
#     cursor.execute('SELECT COUNT(*) FROM users')
#     count = cursor.fetchone()[0]
#     return count
#
# async def download_video(url, chat_id):
#     ydl_opts = {
#         'format': 'best',
#         'outtmpl': '%(id)s.%(ext)s',
#         'noplaylist': True,
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         filename = ydl.prepare_filename(info)
#         with open(filename, 'rb') as video:
#             await bot.send_video(chat_id, video)
#         os.remove(filename)
#
# @dp.message_handler(commands=['start'])
# async def start_welcome(message: types.Message):
#     user = message.from_user
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     status_button = KeyboardButton('/start')
#     markup.add(status_button)
#     await message.reply("Salom! Men Instagram va YouTube videolarini yuklab beradigan botman. Video havolasini yuboring.", reply_markup=markup)
#
# @dp.message_handler()
# async def send_video(message: types.Message):
#     if message.text.startswith('http'):
#         url = message.text
#         await download_video(url, message.chat.id)
#     elif message.text == '/start' and str(message.from_user.id) == ADMIN_ID:
#         count = get_user_count()
#         await message.reply(f"Botdan {count} ta foydalanuvchi foydalangan")
#     else:
#         await message.reply("Notog'ri url")
#
# executor.start_polling(dp, skip_updates=True)
