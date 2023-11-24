from strategies.redirect_to_strategies import choose

class Strategy:
    def __init__(self, name: str):
        self.strategy: object = choose(name)()

    def should_buy(self, current_price: float, historical_data: list) -> bool:
        return self.strategy.should_buy(current_price, historical_data)

    def should_sell(self, current_price: float, historical_data: list) -> bool:
        return self.strategy.should_sell(current_price, historical_data)
