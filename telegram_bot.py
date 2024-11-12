import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder
from telegram.error import TimedOut
from logging_config import setup_logging

# Set up logging
logger = setup_logging()

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Initialize the Telegram bot
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Initial connection pool size and timeout
bot.request.pool_size = 10
bot.request.pool_timeout = 10

async def send_telegram_message(message):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logger.info(f"Sent message to Telegram: {message}")
    except TimedOut:
        logger.warning("TimedOut exception encountered. Adjusting pool settings.")
        adjust_pool_settings()
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logger.info(f"Sent message to Telegram after adjusting pool settings: {message}")

def adjust_pool_settings():
    global bot
    # Increase pool size and timeout
    new_pool_size = min(bot.request.pool_size * 2, 100)  # Limit to a reasonable maximum
    new_pool_timeout = min(bot.request.pool_timeout * 2, 600)  # Limit to a reasonable maximum

    # Update the bot's request settings
    bot.request.pool_size = new_pool_size
    bot.request.pool_timeout = new_pool_timeout

    logger.info(f"Adjusted pool size to {new_pool_size} and pool timeout to {new_pool_timeout}")

def send_message_sync(message):
    asyncio.run(send_telegram_message(message))