from auto_trader.strategies.redirect_to_strategies import choose


class Strategy:
    def __init__(self, name: str, initial_balance: int):
        self.strategy: object = choose(name, initial_balance)

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

    def should_buy(self, current_price: float, historical_data: list) -> bool:
        if self.verify_historical_data(historical_data):
            return False
        return self.strategy.should_buy(current_price, historical_data)

    def should_sell(self, current_price: float, historical_data: list) -> bool:
        if self.verify_historical_data(historical_data):
            return False
        return self.strategy.should_sell(current_price, historical_data)
