import logging
import os

def setup_logging():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logging.basicConfig(level=log_level, format=log_format)

    # Create a logger for the application
    logger = logging.getLogger('bandwidth_monitor')

    # Optionally, add a file handler to log to a file
    log_file = os.getenv('LOG_FILE', 'bandwidth_monitor.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format))

    logger.addHandler(file_handler)

    return logger
