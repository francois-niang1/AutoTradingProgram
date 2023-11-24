import os
from settings.env.strings import *
from settings.env.log import logger

CONFIG_PATH: str = os.path.join(SETTINGS_STR,CONFIG_PY_STR)
LOGS_PATH: str = os.path.join(LOGS_STR,LOGS_TXT_STR)
LOGGER = logger()