

'''
This class reads and is a provider for all the settings.

1. Looks for environment variable setting telling where the config file is.
2. Looks in static path for file "~/.AuctionServe_settings.conf"
3. If it cannot find a settings conf it copies the example over with the default settings and loads that.
'''

class Settings:

    is_dev = True  # For Development Purposes early

    def __init__(self):
        print("Settings Class Init...")



