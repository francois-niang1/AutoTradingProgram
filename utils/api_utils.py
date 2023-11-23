# Fonctions pour interagir avec les APIs

import ccxt
from config import BINANCE_API_KEY, BINANCE_SECRET_KEY

class BinanceClient:
    def __init__(self):
        self.client = ccxt.binance({
            'apiKey': BINANCE_API_KEY,
            'secret': BINANCE_SECRET_KEY,
        })

    def get_ticker_price(self, symbol):
        ticker = self.client.fetch_ticker(symbol)
        return ticker['last']