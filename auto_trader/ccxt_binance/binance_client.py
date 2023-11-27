import ccxt
from env import String, Const


class BinanceClient:
    def __init__(self):
        self.client: ccxt.binance = ccxt.binance(
            {
                String.API_KEY: Const.BINANCE_API_KEY,
                String.SECRET: Const.BINANCE_SECRET_KEY,
            }
        )

    def get_ticker_price(self, symbol :str) -> str:
        ticker: str = self.client.fetch_ticker(symbol)
        return ticker[String.LAST]
