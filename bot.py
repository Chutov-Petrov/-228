from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '7862542822:AAHZb98VPleLDePavpNbLvpQNHEGXbJ9I04'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "Привет! Я простой бот. Задайте мне вопрос.")

@dp.message_handler(lambda message: message.text.lower() == "привет")
async def greet_user(message: types.Message):
    await message.reply("Привет! Как дела?")

@dp.message_handler(lambda message: message.text.lower() == "круто")
async def greet_user(message: types.Message):
    await message.reply("Ага, согласен")

@dp.message_handler(lambda message: message.text.lower() == "всё хорошо")
async def greet_user(message: types.Message):
    await message.reply("Я рад за тебя!")

@dp.message_handler(lambda message: message.text.lower() == "у тебя как дела?")
async def greet_user(message: types.Message):
    await message.reply("У меня тоже хорошо")

@dp.message_handler(lambda message: message.text.lower() == "го в бравл")
async def greet_user(message: types.Message):
    await message.reply("Го")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
