import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logging.basicConfig(level=log_level, format=log_format)

    # Create a logger for the application
    logger = logging.getLogger('bandwidth_monitor')

    # Optionally, add a rotating file handler to log to a file
    log_file = os.getenv('LOG_FILE', 'bandwidth_monitor.log')
    max_bytes = 10 * 1024 * 1024  # 10 MB
    backup_count = 5  # Keep 5 backup files

    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))

    logger.addHandler(file_handler)

    return logger
