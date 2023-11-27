from .config.consts import MeanReversionSettings


class Mean_reversion:
    def __init__(self, initial_balance: int):
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
        if (
            MeanReversionSettings.MIN_DROP
            <= price_change_percentage
            <= MeanReversionSettings.MAXIMUM_DROP
        ):
            # Calculer la quantité à acheter (20 % du solde actuel)
            amount_to_buy = MeanReversionSettings.BUY_PERCENTAGE * self.balance
            # Mettre de côté 20 % de la somme pour le gain
            self.balance -= MeanReversionSettings.REFILL_PERCENTAGE_BUY * amount_to_buy
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
        if (
            MeanReversionSettings.MIN_RISE
            <= price_change_percentage
            <= MeanReversionSettings.MAXIMUM_RISE
        ):
            # Calculer la quantité à vendre (20 % des holdings actuels)
            amount_to_sell = (
                MeanReversionSettings.SELL_PERCENTAGE * self.holdings * current_price
            )
            # Mettre de côté 20 % de la somme pour le gain
            self.balance += (
                MeanReversionSettings.REFILL_PERCENTAGE_SELL * amount_to_sell
            )
            self.holdings -= (
                MeanReversionSettings.REFILL_PERCENTAGE_SELL * self.holdings
            )
            return True
        return False
