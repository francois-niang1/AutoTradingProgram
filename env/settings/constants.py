import os
import logging
from .strings import String
from env.config import load_json_from_URL


def logger(logs_path: str) -> logging.Logger:
    logger_gui: logging.Logger = logging.getLogger("GUI")
    logger_gui.setLevel(logging.DEBUG)
    ch: logging.StreamHandler = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter: logging.StreamHandler = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger_gui.addHandler(ch)
    logging.basicConfig(filename=logs_path)
    return logger_gui


class Const:
    KEY_PATH: str = os.path.join(
        String.AUTO_TRADER, String.CCXT_BINANCE, String.KEY_JSON
    )
    KEYS: dict = load_json_from_URL(KEY_PATH)
    BINANCE_API_KEY: str = KEYS[String.BINANCE_API_KEY]
    BINANCE_SECRET_KEY: str = KEYS[String.BINANCE_SECRET_KEY]
    GLOBAL_CONFIG_PATH: str = os.path.join(String.SETTINGS, String.GLOBAL_JSON)
    GLOBAL_CONFIG: dict = load_json_from_URL(GLOBAL_CONFIG_PATH)
    INTERVAL: str = GLOBAL_CONFIG[String.INTERVAL]
    LIMIT: int = GLOBAL_CONFIG[String.LIMIT]
    EXECUTE_BUY_PERCENTAGE: float = GLOBAL_CONFIG[String.EXECUTE_BUY_PERCENTAGE]
    EXECUTE_SELL_PERCENTAGE: float = GLOBAL_CONFIG[String.EXECUTE_SELL_PERCENTAGE]
    LOGS_PATH: str = os.path.join(String.LOGS, String.LOGS_TXT)
    LOGGER = logger(LOGS_PATH)
