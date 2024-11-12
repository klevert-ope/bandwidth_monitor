import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder
from logging_config import setup_logging

# Set up logging
logger = setup_logging()

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Initialize the Telegram bot
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Adjust the connection pool size and timeout
bot.request.pool_size = 100  # Increase the pool size
bot.request.pool_timeout = 600  # Increase the pool timeout

async def send_telegram_message(message):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    logger.info(f"Sent message to Telegram: {message}")

def send_message_sync(message):
    asyncio.run(send_telegram_message(message))
