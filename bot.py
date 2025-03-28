from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import asyncio

API_TOKEN = '8192162280:AAGHwN2HKK21L4PCF1Jjuk3SAHTY-i5H8HE'

bot = Bot(token='8192162280:AAGHWN2HKK21L4PCF1Jjuk3SAHTY-i5H8HE')

dp = Dispatcher(bot)

# /start command handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Welcome message
    await message.reply("👋 Привет! Добро пожаловать в мой обучающий бот.")

    # Send intro video (video note)
    video = InputFile("intro.mp4")
    await bot.send_video_note(chat_id=message.chat.id, video_note=video)

    # Wait 3 seconds
    await asyncio.sleep(3)

    # Description
    await message.reply("📚 Это описание нашего обучения. Вы узнаете много нового и интересного!")

    # Payment button
    pay_button = InlineKeyboardButton(text="💳 Оплатить", url="https://your-payment-link.com")
    keyboard = InlineKeyboardMarkup().add(pay_button)
    await message.reply("Нажмите на кнопку ниже, чтобы оплатить:", reply_markup=keyboard)

# Run bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
