import os

# Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'YOUR_TELEGRAM_CHAT_ID')

# Database file
DATABASE_FILE = 'bandwidth_usage.db'

# Bandwidth limit in TB (read from environment variable)
BANDWIDTH_LIMIT_TB = float(os.getenv('BANDWIDTH_LIMIT_TB', 2))  # Default to 2 TB if not set
BANDWIDTH_LIMIT = BANDWIDTH_LIMIT_TB * 1024 * 1024 * 1024 * 1024  # Convert TB to bytes
