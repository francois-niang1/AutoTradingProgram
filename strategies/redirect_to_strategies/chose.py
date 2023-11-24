from strategies.redirect_to_strategies.mean_reversion import Mean_reversion
from strategies.redirect_to_strategies.other import Other

def choose(name: str) -> object:
    traductor: dict = {
        "Mean_reversion": Mean_reversion,
        "Other" : Other 
    }
    return traductor[name]