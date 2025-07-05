import logging
import sys


def setup_logger(level="INFO", logfile=None):
    root = logging.getLogger()

    screen_log_format = "[%(levelname).4s] [%(funcName)25s] %(message)s"
    file_log_format = (
        "[%(asctime)-15s] [%(levelname)08s]  [%(name)s] [%(funcName)s] %(message)s"
    )

    # default to INFO if level is invalid
    level = level.upper()
    level_value = getattr(logging, level, logging.INFO)

    # clear any existing handlers
    root.handlers = []
    root.setLevel(level_value)

    # screen handler
    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(level_value)
    screen_handler.setFormatter(logging.Formatter(screen_log_format))
    root.addHandler(screen_handler)

    # file handler, if logfile is provided
    if logfile is not None:
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(level_value)
        file_handler.setFormatter(logging.Formatter(file_log_format))
        root.addHandler(file_handler)

    return
