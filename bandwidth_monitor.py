import psutil
import time
from datetime import datetime, timedelta
from config import BANDWIDTH_LIMIT
from database import init_db, log_bandwidth_usage, get_total_bandwidth_used, get_daily_bandwidth_usage
from telegram_bot import send_message_sync

def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent + net_io.bytes_recv

def main():
    # Initialize the database
    init_db()

    # Initialize variables
    start_time = datetime.now()
    last_bandwidth_used = get_network_usage()

    while True:
        try:
            # Get current network usage
            current_bandwidth_used = get_network_usage()
            bandwidth_used_since_last_check = current_bandwidth_used - last_bandwidth_used
            last_bandwidth_used = current_bandwidth_used

            # Log bandwidth usage
            log_bandwidth_usage(bandwidth_used_since_last_check)

            # Check if a day has passed
            if datetime.now() - start_time >= timedelta(days=1):
                # Send daily alert
                daily_bandwidth_used = get_daily_bandwidth_usage()
                message = f"📊 Daily Bandwidth Usage: {daily_bandwidth_used / (1024 * 1024):.2f} MB"
                send_message_sync(message)

                # Reset start time
                start_time = datetime.now()

            # Check if bandwidth limit is reached
            total_bandwidth_used = get_total_bandwidth_used()
            if total_bandwidth_used >= BANDWIDTH_LIMIT:
                message = f"⚠️ Bandwidth Limit Reached: {total_bandwidth_used / (1024 * 1024 * 1024):.2f} GB used"
                send_message_sync(message)
                break

            # Wait for a while before the next check
            time.sleep(3600)  # Check every hour

        except Exception as e:
            send_message_sync(f"❌ Error: {str(e)}")
            time.sleep(60)  # Wait for a minute before retrying

if __name__ == "__main__":
    main()
