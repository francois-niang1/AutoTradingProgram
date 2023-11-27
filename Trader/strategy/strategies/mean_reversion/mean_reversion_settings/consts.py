import os
from env import String, load_json_from_URL


class MeanReversionSettings:
    PARAMS_PATH = os.path.join(
        String.TRADER,
        String.STRATEGY,
        String.STRATEGIES,
        String.MEAN_REVERSION,
        String.MEAN_REVERSION_SETTINGS,
        String.CONFIG_JSON,
    )
    PARAMS = load_json_from_URL(PARAMS_PATH)
    MIN_DROP: int = PARAMS[String.BUY][String.MIN_DROP]
    MAXIMUM_DROP: int = PARAMS[String.BUY][String.MAXIMUM_DROP]
    BUY_PERCENTAGE: float = PARAMS[String.BUY][String.BUY_PERCENTAGE]
    REFILL_PERCENTAGE_BUY: float = PARAMS[String.BUY][String.REFILL_PERCENTAGE]

    MIN_RISE: int = PARAMS[String.SELL][String.MIN_RISE]
    MAXIMUM_RISE: int = PARAMS[String.SELL][String.MAXIMUM_RISE]
    SELL_PERCENTAGE: float = PARAMS[String.SELL][String.SELL_PERCENTAGE]
    REFILL_PERCENTAGE_SELL: float = PARAMS[String.SELL][String.REFILL_PERCENTAGE]