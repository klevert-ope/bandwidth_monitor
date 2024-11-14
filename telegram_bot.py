import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Set up the Telegram bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("Both TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables must be set.")

bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_message_async(message):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Message sent successfully.")
    except TelegramError as e:
        print(f"Failed to send message: {e}")

def send_message_sync(message):
    asyncio.run(send_message_async(message))
