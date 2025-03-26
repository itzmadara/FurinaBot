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
    DATABASE_URL = "postgresql://postgres:3Ivn8HBlWFVJidvL@ripely-appeasing-nightjar.data-1.use1.tembo.io:5432/postgres"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS =  -1002504420962
    MESSAGE_DUMP = -1002591554488

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Filestation20:Vikash3108@cluster0.itxaht0.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "raiden_gc"
    SUPPORT_ID = -1002674794291

    # Database name
    DB_NAME = "Filestation20"

    # Bot token
    TOKEN = "8185055017:AAEMOZrePAzI1S3N7OiE_toflTNOGPvP7io"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6473663036
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos", "6796872274")
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
