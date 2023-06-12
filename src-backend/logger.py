import json
from pathlib import Path
import os

'''
This Class handles the logging of data into the log file set by the settings class.
It provides static methods to be called whenever something is needed to be logged to handle levels of logging.
'''

class logger:
    filename = "production.log"
    json_data = None

    # For Development Purposes this var should be set to the config file you are trying to set

    @staticmethod
    def __init__(self):
        env_var_name = "AUCTION_SOFT_SETTINGS_PATH"
        if env_var_name in os.environ:  # If settings filepath is defined in environment
            f = open(os.getenv())
            self.json_data = json.load(f)

        if Path('~/settings.conf').exists():  # Hardcoded backup Path
            f = open('~/settings.conf')
            self.json_data = json.load(f)

