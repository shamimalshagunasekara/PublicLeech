if not __name__.endswith("sample_config"):
    import sys
    print(
        "The README is there to be read. "
        "Extend this sample config to a config file, "
        "don't just rename and change values here. "
        "Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr
    )
    quit(1)

from dotenv import load_dotenv
from .get_cfg import get_config


# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


class Config:
    # get a token from @BotFather
    TG_BOT_TOKEN = 5005267086:AAEH1StoLvb4CiY7-uV_LV4RXX_QVow6MzI
    # The Telegram API things
    APP_ID = 1424314
    API_HASH = d1c1c9262bbae8f5eeb80ba47c9f3dff
    # Get these values from my.telegram.org
    # array to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = -1001410465876 
    # the download location, where the HTTP Server runs
    # Telegram maximum file upload siz
    # chunk size that should be used with requests
    # default thumbnail to be used in the video
    # maximum message length in Telegram
    # set timeout for subprocess
    
    SUDO_USERS = 1079261681
