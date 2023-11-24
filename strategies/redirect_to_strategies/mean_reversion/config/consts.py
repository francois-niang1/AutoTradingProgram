import os
from settings import (
    STRATEGIES_STR,
    REDIRECT_TO_STRATEGIES_STR,
    MEAN_REVERSION_STR,
    CONFIG_STR,
    CONFIG_PY_STR,
    BUY_STR,
    MIN_DROP_STR,
    MAXIMUM_DROP_STR,
    BUY_PERCENTAGE_STR,
    REFILL_PERCENTAGE_STR,
    MAXIMUM_RISE_STR,
    SELL_STR,
    MIN_RISE_STR,
    MAXIMUM_RISE_STR,
    SELL_PERCENTAGE_STR,
    BUY_STR,
    load_json_from_URL,
)

PARAMS_PATH = os.path.join(
    STRATEGIES_STR,
    REDIRECT_TO_STRATEGIES_STR,
    MEAN_REVERSION_STR,
    CONFIG_STR,
    CONFIG_PY_STR,
)

PARAMS = load_json_from_URL(PARAMS_PATH)

MIN_DROP: int = PARAMS[BUY_STR][MIN_DROP_STR]
MAXIMUM_DROP: int = PARAMS[BUY_STR][MAXIMUM_DROP_STR]
BUY_PERCENTAGE: float = PARAMS[BUY_STR][BUY_PERCENTAGE_STR]
REFILL_PERCENTAGE_BUY: float = PARAMS[BUY_STR][REFILL_PERCENTAGE_STR]

MIN_RISE: int = PARAMS[SELL_STR][MIN_RISE_STR]
MAXIMUM_RISE: int = PARAMS[SELL_STR][MAXIMUM_RISE_STR]
SELL_PERCENTAGE: float = PARAMS[SELL_STR][SELL_PERCENTAGE_STR]
REFILL_PERCENTAGE_SELL: float = PARAMS[SELL_STR][REFILL_PERCENTAGE_STR]
