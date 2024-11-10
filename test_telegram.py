import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Initialize the Telegram bot
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Adjust the connection pool size and timeout
bot.request.pool_size = 10  # Increase the pool size
bot.request.pool_timeout = 60  # Increase the pool timeout

async def send_test_message():
    message = "📢 Test message from Bandwidth Monitor!"
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    print("Test message sent successfully!")

if __name__ == "__main__":
    asyncio.run(send_test_message())
