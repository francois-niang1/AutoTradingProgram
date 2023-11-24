from settings import LOGS_PATH
import logging


def logger() -> logging.Logger:
    logger_gui: logging.Logger = logging.getLogger("GUI")
    logger_gui.setLevel(logging.DEBUG)
    ch: logging.StreamHandler = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter: logging.StreamHandler = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger_gui.addHandler(ch)
    logging.basicConfig(filename=LOGS_PATH)
    return logger_gui
