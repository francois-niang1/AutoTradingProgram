from auto_trader.strategies.redirect_to_strategies.mean_reversion import Mean_reversion
from auto_trader.strategies.redirect_to_strategies.other import Other
from settings import MEAN_REVERSION_STR, OTHER_STR


def choose(name: str, initial_balance: int) -> object:
    traductor: dict = {
        MEAN_REVERSION_STR: Mean_reversion(initial_balance),
        OTHER_STR: Other(initial_balance),
    }
    return traductor[name]
