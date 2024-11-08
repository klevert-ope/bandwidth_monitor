import os
import asyncio
from telegram import Bot

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Initialize the Telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_test_message():
    message = "📢 Test message from Bandwidth Monitor!"
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if __name__ == "__main__":
    asyncio.run(send_test_message())
