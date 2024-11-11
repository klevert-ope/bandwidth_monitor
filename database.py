import sqlite3
from datetime import datetime, timedelta
from logging_config import setup_logging

# Set up logging
logger = setup_logging()

def init_db():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS bandwidth_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                bytes_used INTEGER
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS monthly_bandwidth_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                month TEXT,
                bytes_used INTEGER
            )
        ''')
        conn.commit()
        logger.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logger.error(f"Error initializing database: {e}")
    finally:
        conn.close()

def log_bandwidth_usage(bytes_used):
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO bandwidth_usage (bytes_used) VALUES (?)', (bytes_used,))
        conn.commit()
        logger.info(f"Logged bandwidth usage: {bytes_used} bytes")
    except sqlite3.Error as e:
        logger.error(f"Error logging bandwidth usage: {e}")
    finally:
        conn.close()

def update_monthly_bandwidth_usage(bytes_used):
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    month = datetime.now().strftime("%Y-%m")
    try:
        c.execute('SELECT bytes_used FROM monthly_bandwidth_usage WHERE month = ?', (month,))
        result = c.fetchone()
        if result:
            c.execute('UPDATE monthly_bandwidth_usage SET bytes_used = bytes_used + ? WHERE month = ?', (bytes_used, month))
        else:
            c.execute('INSERT INTO monthly_bandwidth_usage (month, bytes_used) VALUES (?, ?)', (month, bytes_used))
        conn.commit()
        logger.info(f"Updated monthly bandwidth usage for {month}: {bytes_used} bytes")
    except sqlite3.Error as e:
        logger.error(f"Error updating monthly bandwidth usage: {e}")
    finally:
        conn.close()

def get_total_bandwidth_used():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    try:
        c.execute('SELECT SUM(bytes_used) FROM bandwidth_usage')
        total_bytes = c.fetchone()[0]
        return total_bytes if total_bytes else 0
    except sqlite3.Error as e:
        logger.error(f"Error getting total bandwidth used: {e}")
        return 0
    finally:
        conn.close()

def get_daily_bandwidth_usage():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    start_of_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    try:
        c.execute('SELECT SUM(bytes_used) FROM bandwidth_usage WHERE timestamp >= ?', (start_of_day,))
        daily_bytes = c.fetchone()[0]
        return daily_bytes if daily_bytes else 0
    except sqlite3.Error as e:
        logger.error(f"Error getting daily bandwidth usage: {e}")
        return 0
    finally:
        conn.close()

def get_monthly_bandwidth_usage():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    month = datetime.now().strftime("%Y-%m")
    try:
        c.execute('SELECT bytes_used FROM monthly_bandwidth_usage WHERE month = ?', (month,))
        monthly_bytes = c.fetchone()[0]
        return monthly_bytes if monthly_bytes else 0
    except sqlite3.Error as e:
        logger.error(f"Error getting monthly bandwidth usage: {e}")
        return 0
    finally:
        conn.close()

def delete_old_data():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    one_month_ago = datetime.now() - timedelta(days=30)
    try:
        c.execute('DELETE FROM bandwidth_usage WHERE timestamp < ?', (one_month_ago,))
        conn.commit()
        logger.info("Old data deleted successfully.")
    except sqlite3.Error as e:
        logger.error(f"Error deleting old data: {e}")
    finally:
        conn.close()
