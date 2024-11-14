import os
import time
import pytest
import requests

from telegram_bot import send_message_sync

# Set up the Telegram bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def clear_updates():
    """Clear existing updates to start fresh."""
    requests.get(f"{BASE_URL}/getUpdates", params={"offset": -1})

def get_updates(offset=None):
    """Retrieve the latest updates from Telegram, optionally with an offset."""
    params = {"offset": offset} if offset else {}
    try:
        response = requests.get(f"{BASE_URL}/getUpdates", params=params)
        response.raise_for_status()
        return response.json().get('result', [])
    except requests.RequestException as e:
        print(f"Failed to retrieve updates: {e}")
        return []

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    # Clear updates before and after each test
    clear_updates()
    yield
    clear_updates()

def test_send_message():
    test_message = "This is a test message from the Telegram bot."

    # Send the test message
    send_message_sync(test_message)

    # Retry to get updates with offset
    retries = 10
    updates = []
    last_update_id = None
    for _ in range(retries):
        time.sleep(5)
        updates = get_updates(offset=last_update_id)

        if updates:
            last_update_id = updates[-1]["update_id"] + 1
            if any(update.get('message', {}).get('text') == test_message for update in updates):
                break

    # Log the updates for debugging
    print("Updates:", updates)

    # Verify if the test message is in the updates
    assert len(updates) > 0, "No updates found."
    assert any(update.get('message', {}).get('text') == test_message for update in updates), \
        "Test message not found in updates."


if __name__ == "__main__":
    pytest.main()
