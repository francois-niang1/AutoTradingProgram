class Other:
    def __init__(self, initial_balance: int):
        self.initial_balance = initial_balance

    def should_buy(self, current_price: float, historical_data: list) -> bool:
        return False

    def should_sell(self, current_price: float, historical_data: list) -> bool:
        return False
