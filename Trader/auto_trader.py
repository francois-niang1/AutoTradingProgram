import time
import ccxt

from .strategy import TradingStrategy, TradingStrategyFactory, TradingStrategyType
from .ccxt_binance import BinanceClient
from env import String, Const


def auto_trade():
    binance_client: BinanceClient = BinanceClient()
    strategy: TradingStrategy = TradingStrategyFactory.create(
        TradingStrategyType.MeanReversion
    )

    while True:
        try:
            # Obtenir le prix actuel
            current_price: int = binance_client.get_ticker_price(String.SYMBOL)

            # Obtenir des données historiques (à implémenter)
            historical_data: list[int] = get_historical_data(
                binance_client.client, String.SYMBOL
            )

            # Logique de trading
            if strategy.should_buy(current_price, historical_data):
                execute_buy_order(
                    binance_client.client, String.SYMBOL, Const.EXECUTE_BUY_PERCENTAGE
                )  # Acheter 20 % du solde

            elif strategy.should_sell(current_price, historical_data):
                execute_sell_order(
                    binance_client.client, String.SYMBOL, Const.EXECUTE_SELL_PERCENTAGE
                )  # Vendre 20 % des holdings

            # Pause entre les itérations (à ajuster selon la stratégie)
            time.sleep(60)

        except Exception as e:
            error_message: str = f"Une erreur s'est produite : {e}"
            Const.LOGGER.error(error_message)


def get_historical_data(
    binance_client: ccxt.binance,
    symbol: str,
    interval: str = Const.INTERVAL,
    limit: int = Const.LIMIT,
) -> list[int]:
    try:
        # Utilisez l'API Binance pour obtenir les données historiques (klines)
        ohlcv: list[list] = binance_client.fetch_ohlcv(
            symbol, interval=interval, limit=limit
        )

        # Extrayez uniquement les prix de clôture (closes)
        historical_data: list[int] = [candle[4] for candle in ohlcv]

        return historical_data

    except Exception as e:
        error_message: str = f"Une erreur s'est produite lors de la récupération des données historiques : {e}"
        Const.LOGGER.error(error_message)
        return []


def execute_buy_order(
    binance_client: ccxt.binance, symbol: str, percentage: float
) -> None:
    try:
        # Obtenir le solde actuel
        balance: float = binance_client.fetch_balance()
        free_balance: float = balance[String.TOTAL][String.USDT]

        # Calculer la quantité à acheter (un pourcentage du solde actuel)
        amount_to_buy: float = percentage * free_balance

        # Exécuter l'ordre d'achat au marché
        order = binance_client.create_market_buy_order(symbol, amount_to_buy)

        print(
            f"Ordre d'achat exécuté pour {String.SYMBOL}. Montant : {amount_to_buy}. ID de commande : {order['id']}"
        )

    except Exception as e:
        error_message: str = (
            f"Une erreur s'est produite lors de l'exécution de l'ordre d'achat : {e}"
        )
        Const.LOGGER.error(error_message)


def execute_sell_order(
    binance_client: ccxt.binance, symbol: str, percentage: float
) -> None:
    try:
        # Obtenir le solde actuel de l'actif détenu
        holdings: int = binance_client.fetch_balance()[String.SYMBOL.replace("/", "")][
            String.FREE
        ]

        # Calculer la quantité à vendre (un pourcentage des holdings actuels)
        amount_to_sell: float = percentage * float(holdings)

        # Exécuter l'ordre de vente au marché
        order = binance_client.create_market_sell_order(String.SYMBOL, amount_to_sell)

        print(
            f"Ordre de vente exécuté pour {String.SYMBOL}. Montant : {amount_to_sell}. ID de commande : {order['id']}"
        )

    except Exception as e:
        error_message: str = (
            f"Une erreur s'est produite lors de l'exécution de l'ordre de vente : {e}"
        )
        Const.LOGGER.error(error_message)
