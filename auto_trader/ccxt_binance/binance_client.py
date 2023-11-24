# Fonctions pour interagir avec les APIs

import ccxt
from settings import (
    LAST_STR,
    API_KEY_STR,
    SECRET_STR,
    BINANCE_API_KEY,
    BINANCE_SECRET_KEY,
)


class BinanceClient:
    def __init__(self):
        self.client = ccxt.binance(
            {
                API_KEY_STR: BINANCE_API_KEY,
                SECRET_STR: BINANCE_SECRET_KEY,
            }
        )

    def get_ticker_price(self, symbol):
        ticker = self.client.fetch_ticker(symbol)
        return ticker[LAST_STR]
