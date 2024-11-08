# Bandwidth Monitor

This project monitors the bandwidth usage on a VPS and sends daily alerts to a Telegram chatbot. It also sets a bandwidth limit and sends an alert when the limit is reached.

## Features

- Monitors network bandwidth usage.
- Sends daily bandwidth usage reports to a Telegram chat.
- Alerts when the bandwidth limit is reached.
- Persists bandwidth usage data in an SQLite database.
- Configurable bandwidth limit using environment variables.

## Requirements

- Docker
- Docker Compose
- Python 3.x
- `psutil`
- `python-telegram-bot`

## Project Structure

```
bandwidth_monitor/
├── bandwidth_monitor.py
├── config.py
├── database.py
├── telegram_bot.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── test_network_usage.py
└── README.md
```

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/klevert-ope/bandwidth_monitor.git
cd bandwidth_monitor
```

### Step 2: Set Up Your Telegram Bot

1. Create a new bot using BotFather on Telegram and get the bot token.
2. Start a chat with your bot and get the chat ID.

### Step 3: Create a `.env` File

Create a `.env` file in the project root with the following content:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
BANDWIDTH_LIMIT_TB=2
```

### Step 4: Build and Run the Docker Container

```bash
docker-compose build
docker-compose up -d
```

## Testing

### Testing Network Usage

To test the `get_network_usage` function, you can run the `test_network_usage.py` script using Docker Compose.

1. **Run the Test Script**:

```bash
docker-compose run --rm test_network_usage
```

2. **Verify the Output**:

You should see output similar to the following:

```
Total Network Usage: 123456789 bytes
Total Network Usage: 117.73 MB
```

This output indicates that the `get_network_usage` function is working correctly and returning the total network usage in bytes and megabytes.

### Testing Telegram Integration

To test the Telegram integration, you can run the `test_telegram.py` script using Docker Compose.

1. **Run the Test Script**:

```bash
docker-compose run --rm test_telegram
```

2. **Verify the Test Message**:

After running the test script, check your Telegram chat to see if you received the test message. If you see the message "📢 Test message from Bandwidth Monitor!", it means that your Telegram integration is working correctly.

## Usage

### Daily Bandwidth Usage Alerts

The script sends a daily alert to your Telegram chat with the bandwidth usage for the day. The message includes the total bandwidth used in megabytes.

### Bandwidth Limit Alerts

The script sends an alert to your Telegram chat when the bandwidth limit is reached. The message includes the total bandwidth used in gigabytes.

### Error Alerts

The script sends an error message to your Telegram chat if any exceptions occur during execution.

## Clean Up

If the tests were successful, you can remove the `test_network_usage` and `test_telegram` services from your `docker-compose.yml` file to keep your configuration clean.

### `docker-compose.yml` (Cleaned Up)

```yaml
version: '3.8'

services:
  bandwidth_monitor:
    build: .
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}
      - BANDWIDTH_LIMIT_TB=${BANDWIDTH_LIMIT_TB}
    volumes:
      - ./bandwidth_usage.db:/app/bandwidth_usage.db
    restart: always
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.