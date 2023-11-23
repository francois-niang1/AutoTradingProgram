# simple_strategy.py
class SimpleStrategy:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.holdings = 0
        self.profit_percentage = 0.2  # 20 % de la somme pour le gain

    def should_buy(self, current_price, historical_data):
        if not historical_data:
            return False  # Assurez-vous que vous avez suffisamment de données historiques

        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = ((current_price - historical_data[-1]) / historical_data[-1]) * 100

        # Condition pour acheter lorsque le marché baisse de 10 à 20 %
        if -20 <= price_change_percentage <= -10:
            # Calculer la quantité à acheter (20 % du solde actuel)
            amount_to_buy = 0.2 * self.balance

            # Mettre de côté 20 % de la somme pour le gain
            self.balance -= 0.2 * amount_to_buy
            self.holdings += amount_to_buy / current_price

            return True

        return False

    def should_sell(self, current_price, historical_data):
        if not historical_data:
            return False  # Assurez-vous que vous avez suffisamment de données historiques

        # Calculer la variation en pourcentage par rapport à la période précédente
        price_change_percentage = ((current_price - historical_data[-1]) / historical_data[-1]) * 100

        # Condition pour vendre lorsque le marché augmente de 10 à 20 %
        if 10 <= price_change_percentage <= 20:
            # Calculer la quantité à vendre (20 % des holdings actuels)
            amount_to_sell = 0.2 * self.holdings * current_price

            # Mettre de côté 20 % de la somme pour le gain
            self.balance += 0.2 * amount_to_sell
            self.holdings -= 0.2 * self.holdings

            return True

        return False