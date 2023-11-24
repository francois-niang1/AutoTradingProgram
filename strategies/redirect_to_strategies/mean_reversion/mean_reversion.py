from settings import load_json_from_URL
from strategies.redirect_to_strategies.mean_reversion.config.consts import (
    MIN_DROP,
    MAXIMUM_DROP,
    BUY_PERCENTAGE,
    REFILL_PERCENTAGE_BUY,
    MIN_RISE,
    MAXIMUM_RISE,
    SELL_PERCENTAGE,
    REFILL_PERCENTAGE_SELL,
)

class Mean_reversion:
    def __init__(self, initial_balance: int = 1000):
        self.PARAMS: dict = load_json_from_URL()
        self.balance: int = initial_balance
        self.holdings: int = 0

    def should_buy(self, current_price: float, historical_data: list) -> bool:
        """
        Takes previous data and returns should we buy or not
        Args:
            current_price: int -> Current stock price
            historical_data: list -> The previous set of
            prices aroud this value
        Returns:
            bool -> The decision to buy or not
        """
        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = (
            (current_price - historical_data[-1]) / historical_data[-1]
        ) * 100
        # Condition pour acheter lorsque le marché baisse de 10 à 20 %
        if MIN_DROP <= price_change_percentage <= MAXIMUM_DROP:
            # Calculer la quantité à acheter (20 % du solde actuel)
            amount_to_buy = BUY_PERCENTAGE * self.balance
            # Mettre de côté 20 % de la somme pour le gain
            self.balance -= REFILL_PERCENTAGE_BUY * amount_to_buy
            self.holdings += amount_to_buy / current_price
            return True
        return False

    def should_sell(self, current_price: float, historical_data: list) -> bool:
        """
        Takes previous data and returns should we sell or not
        Args:
            current_price: int -> Current stock price
            historical_data: list -> The previous set of
            prices aroud this value
        Returns:
            bool -> The decision to sell or not
        """
        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = (
            (current_price - historical_data[-1]) / historical_data[-1]
        ) * 100

        # Condition pour vendre lorsque le marché augmente de 10 à 20 %
        if MIN_RISE <= price_change_percentage <= MAXIMUM_RISE:
            # Calculer la quantité à vendre (20 % des holdings actuels)
            amount_to_sell = SELL_PERCENTAGE * self.holdings * current_price
            # Mettre de côté 20 % de la somme pour le gain
            self.balance += REFILL_PERCENTAGE_SELL * amount_to_sell
            self.holdings -= REFILL_PERCENTAGE_SELL * self.holdings
            return True
        return False
