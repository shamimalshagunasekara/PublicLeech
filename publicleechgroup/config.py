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
