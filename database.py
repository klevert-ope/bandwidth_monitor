import sqlite3
from datetime import datetime
from logging_config import setup_logging

# Set up logging
logger = setup_logging()

def init_db():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bandwidth_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            bytes_used INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    logger.info("Database initialized successfully.")

def log_bandwidth_usage(bytes_used):
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    c.execute('INSERT INTO bandwidth_usage (bytes_used) VALUES (?)', (bytes_used,))
    conn.commit()
    conn.close()
    logger.info(f"Logged bandwidth usage: {bytes_used} bytes")

def get_total_bandwidth_used():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    c.execute('SELECT SUM(bytes_used) FROM bandwidth_usage')
    total_bytes = c.fetchone()[0]
    conn.close()
    return total_bytes if total_bytes else 0

def get_daily_bandwidth_usage():
    conn = sqlite3.connect('bandwidth_usage.db')
    c = conn.cursor()
    start_of_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    c.execute('SELECT SUM(bytes_used) FROM bandwidth_usage WHERE timestamp >= ?', (start_of_day,))
    daily_bytes = c.fetchone()[0]
    conn.close()
    return daily_bytes if daily_bytes else 0
