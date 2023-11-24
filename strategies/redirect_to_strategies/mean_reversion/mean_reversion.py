class Mean_reversion:
    def __init__(self, initial_balance: int = 1000):
        self.balance: int = initial_balance
        self.holdings: int = 0
        self.profit_percentage: float = 0.2  # 20 % de la somme pour le gain

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

        min_drop: int = -20
        maximum_drop: int = -10
        buy_percentage: float = 0.2
        refill_percentage: float = 0.2

        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = (
            (current_price - historical_data[-1]) / historical_data[-1]
        ) * 100
        # Condition pour acheter lorsque le marché baisse de 10 à 20 %
        if min_drop <= price_change_percentage <= maximum_drop:
            # Calculer la quantité à acheter (20 % du solde actuel)
            amount_to_buy = buy_percentage * self.balance

            # Mettre de côté 20 % de la somme pour le gain
            self.balance -= refill_percentage * amount_to_buy
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
        min_rise: int = 10
        maximum_rise: int = 20
        sell_percentage: float = 0.2
        refill_percentage: float = 0.2

        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = (
            (current_price - historical_data[-1]) / historical_data[-1]
        ) * 100

        # Condition pour vendre lorsque le marché augmente de 10 à 20 %
        if min_rise <= price_change_percentage <= maximum_rise:
            # Calculer la quantité à vendre (20 % des holdings actuels)
            amount_to_sell = sell_percentage * self.holdings * current_price

            # Mettre de côté 20 % de la somme pour le gain
            self.balance += refill_percentage * amount_to_sell
            self.holdings -= refill_percentage * self.holdings

            return True

        return False
