import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "nvslinkbot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
π€ My Name: <a href='http://t.me/mdisk_searche_bot'>Mdisk Search Robot</a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ Server: <a href='https://heroku.com'>Heroku</a>

π¨βπ» Created By: <a href='https://t.me/GreyMatter_Bots'>GreyMatter Bots</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» Developer : <a href='https://t.me/GreyMatter_Owner'>GreyMatter</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}π,

I'm Mdisk Search Robot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}π,

I'm Mdisk Search Robot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @GreyMatter_Bots</a></b>
"""

