import logging
from logging.handlers import RotatingFileHandler

def configure_logging(logger_level=None):

    if not logger_level:
        logger_level = logging.INFO

    # Create the root logger
    root_logger = logging.getLogger()

    # Set the root logger level
    root_logger.setLevel(logger_level)

    # Create a console handler and set its level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logger_level)

    # Create a file handler with log rotation and set its level
    file_handler = RotatingFileHandler('root.log', mode='w')
    file_handler.setLevel(logger_level)

    # Create a formatter
    formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s]:: %(message)s")

    # Set the formatter for the handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the root logger
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

