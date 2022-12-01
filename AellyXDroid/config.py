class Config(object):
    LOGGER = True

    API_ID = 15035428
    API_HASH = "ab53c21e6be1535aa19312808b76e51a"
    TOKEN = "5271178420:AAHeIbRCHJRtFelp5VJeb3A89mcvp1qpFvc"
    OWNER_ID = 5233742848
    OWNER_USERNAME = "an_unic_or_n47"
    SUPPORT_CHAT = "t.me/anu_pui"
    JOIN_LOGGER = (-1001603837590)
    EVENT_LOGS = (-1001603837590)

    SQLALCHEMY_DATABASE_URI = "postgres://faisclyk:8qIQ96pzenRUW1X2xMfOjbwMTS0HAhP8@peanut.db.elephantsql.com/faisclyk"
    MONGO_DB_URI = "mongodb+srv://anu:anu@cluster0.n1mhees.mongodb.net/?retryWrites=true&w=majority"
    LOAD = [on]
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    ## Optional
    DRAGONS = [5233742848]
    DEV_USERS = [5233742848]
    DEMONS = [5233742848]
    TIGERS = [5233742848]
    WOLVES = [5233742848]

    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (8)
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "GUHZKUCUR2HQL1YG"
    TIME_API_KEY = "DD6YGKX1SRC8"
    BL_CHATS = [-1001603837590]
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://te.legra.ph/file/c6883f6ebb2e07242f2b3.png"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
