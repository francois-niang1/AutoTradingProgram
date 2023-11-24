# Fichier de configuration pour les clés API et autres paramètres

BINANCE_API_KEY = 'clé_api'
BINANCE_SECRET_KEY = 'clé_secrète'


def verify_historical_data(self, historical_data: list) -> bool:
    """
    Making sure we have suffisient historical data
    Args:
        historical_data: list -> an array that either has
        or has not content
    Returns:
        Bool -> False if array is empty else True
    """
    return not (not historical_data)