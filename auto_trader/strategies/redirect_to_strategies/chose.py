from .mean_reversion import Mean_reversion
from .other import Other
from env import String


def choose(name: str, initial_balance: int) -> object:
    traductor: dict = {
        String.MEAN_REVERSION: Mean_reversion(initial_balance),
        String.OTHER: Other(initial_balance),
    }
    return traductor[name]
