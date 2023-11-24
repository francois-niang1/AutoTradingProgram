import os
from settings.env.strings import *
from settings.config import load_json_from_URL

KEY_PATH: str = os.path.join(AUTO_TRADER_STR, CCXT_BINANCE_STR, KEY_JSON_STR)
KEYS: dict = load_json_from_URL(KEY_PATH)
BINANCE_API_KEY: str = KEYS[BINANCE_API_KEY_STR]
BINANCE_SECRET_KEY: str = KEYS[BINANCE_SECRET_KEY_STR]

GLOBAL_CONFIG_PATH: str = os.path.join(SETTINGS_STR, GLOBAL_JSON_STR)
GLOBAL_CONFIG: dict = load_json_from_URL(GLOBAL_CONFIG_PATH)
INTERVAL: str = GLOBAL_CONFIG[INTERVAL_STR]
LIMIT: int = GLOBAL_CONFIG[LIMIT_STR]
EXECUTE_BUY_PERCENTAGE: float = GLOBAL_CONFIG[EXECUTE_BUY_PERCENTAGE_STR]
EXECUTE_SELL_PERCENTAGE: float = GLOBAL_CONFIG[EXECUTE_SELL_PERCENTAGE_STR]

import logging

LOGS_PATH: str = os.path.join(LOGS_STR, LOGS_TXT_STR)


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


LOGGER = logger()
