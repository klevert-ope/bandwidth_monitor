import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder
from telegram.error import TimedOut

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Initialize the Telegram bot
application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Initial connection pool size and timeout
bot.request.pool_size = 10
bot.request.pool_timeout = 10

async def send_test_message():
    message = "📢 Test message from Bandwidth Monitor!"
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Test message sent successfully!")
    except TimedOut:
        print("TimedOut exception encountered. Adjusting pool settings.")
        adjust_pool_settings()
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Test message sent successfully after adjusting pool settings!")

def adjust_pool_settings():
    global bot
    # Increase pool size and timeout
    new_pool_size = min(bot.request.pool_size * 2, 100)  # Limit to a reasonable maximum
    new_pool_timeout = min(bot.request.pool_timeout * 2, 600)  # Limit to a reasonable maximum

    # Update the bot's request settings
    bot.request.pool_size = new_pool_size
    bot.request.pool_timeout = new_pool_timeout

    print(f"Adjusted pool size to {new_pool_size} and pool timeout to {new_pool_timeout}")

if __name__ == "__main__":
    asyncio.run(send_test_message())
