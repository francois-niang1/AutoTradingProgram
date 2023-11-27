from .trading_strategy_type import TradingStrategyType
from .trading_strategy import TradingStrategy
from .strategies import *

class TradingStrategyFactory:
    @staticmethod
    def create(strategy_type: TradingStrategyType) -> TradingStrategy:
        match strategy_type:
            case TradingStrategyType.MeanReversion:
                return MeanReversion()
            case TradingStrategyType.CoolStrategy:
                return OtherStrategy()
