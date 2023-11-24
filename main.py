# Fichier principal du programme

import logging
from strategies import Strategy
from utils.api_utils import BinanceClient
import time

# Configuration du module de journalisation
logging.basicConfig(filename='trading_log.txt')

def main():
    current_strategy: str = "Mean_reversion" 
    symbol = 'BTC/USDT'
    binance_client = BinanceClient()
    strategy = Strategy()

    while True:
        try:
            # Obtenir le prix actuel
            current_price = binance_client.get_ticker_price(symbol)

            # Obtenir des données historiques (à implémenter)
            historical_data = get_historical_data(binance_client.client, symbol)

            # Logique de trading
            if strategy.should_buy(current_price, historical_data):
                execute_buy_order(binance_client.client, symbol, 0.2)  # Acheter 20 % du solde

            elif strategy.should_sell(current_price, historical_data):
                execute_sell_order(binance_client.client, symbol, 0.2)  # Vendre 20 % des holdings

            # Pause entre les itérations (à ajuster selon la stratégie)
            time.sleep(60)

        except Exception as e:
            error_message = f"Une erreur s'est produite : {e}"
            logging.error(error_message)
            print(error_message)

def get_historical_data(binance_client, symbol, interval='1h', limit=50):
    try:
        # Utilisez l'API Binance pour obtenir les données historiques (klines)
        ohlcv = binance_client.fetch_ohlcv(symbol, interval, limit=limit)

        # Extrayez uniquement les prix de clôture (closes)
        historical_data = [candle[4] for candle in ohlcv]

        return historical_data

    except Exception as e:
        error_message = f"Une erreur s'est produite lors de la récupération des données historiques : {e}"
        logging.error(error_message)
        print(error_message)
        return []

def execute_buy_order(binance_client, symbol, percentage):
    try:
        # Obtenir le solde actuel
        balance = binance_client.fetch_balance()
        free_balance = balance['total']['USDT']

        # Calculer la quantité à acheter (un pourcentage du solde actuel)
        amount_to_buy = percentage * free_balance

        # Exécuter l'ordre d'achat au marché
        order = binance_client.create_market_buy_order(symbol, amount_to_buy)

        print(f"Ordre d'achat exécuté pour {symbol}. Montant : {amount_to_buy}. ID de commande : {order['id']}")

    except Exception as e:
        error_message = f"Une erreur s'est produite lors de l'exécution de l'ordre d'achat : {e}"
        logging.error(error_message)
        print(error_message)

def execute_sell_order(binance_client, symbol, percentage):
    try:
        # Obtenir le solde actuel de l'actif détenu
        holdings = binance_client.fetch_balance()[symbol.replace('/', '')]['free']

        # Calculer la quantité à vendre (un pourcentage des holdings actuels)
        amount_to_sell = percentage * float(holdings)

        # Exécuter l'ordre de vente au marché
        order = binance_client.create_market_sell_order(symbol, amount_to_sell)

        print(f"Ordre de vente exécuté pour {symbol}. Montant : {amount_to_sell}. ID de commande : {order['id']}")

    except Exception as e:
        error_message = f"Une erreur s'est produite lors de l'exécution de l'ordre de vente : {e}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    main()