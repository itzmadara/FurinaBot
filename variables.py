import json
import os


def get_user_list(config, key):
    with open("{}/Mikobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 26334773 # Get this value from my.telegram.org/apps
    API_HASH = "3bc4c3c2416c746fb9d613e205e8a320"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://azqpmryu:Uj9aaVwhX6RFCx_QIJQkXEYmkYOJka4t@flora.db.elephantsql.com/azqpmryu"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS =  -1002219420074
    MESSAGE_DUMP = -1002219420074

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Filestation20:Vikash3108@cluster0.itxaht0.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "Anime_Station_Bots"
    SUPPORT_ID = -1001881709903

    # Database name
    DB_NAME = "Filestation20"

    # Bot token
    TOKEN = "6637953187:AAHSuCkUJ4JqHj-KggWU0MGnRa0YPDjWanI"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 1645068158
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = (
        "CAACAgUAAxkBAAEGWC5lloYv1tiI3-KPguoH5YX-RveWugACoQ4AAi4b2FQGdUhawbi91DQE"
    )

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
