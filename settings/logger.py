import logging

def logger():
    logger_gui = logging.getLogger("GUI")
    logger_gui.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger_gui.addHandler(ch)
    return logger_gui

LOGGER_GUI = logger()