import html
import json
import os
from typing import Optional

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from Mikobot import dispatcher
from Mikobot.plugins.helper_funcs.chat_status import dev_plus, sudo_plus
from Mikobot.plugins.helper_funcs.extraction import extract_user
from Mikobot.plugins.log_channel import gloggable

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "Mikobot/elevated_users.json")

# Initialize disaster levels structure
DISASTER_LEVELS = {
    "Dragon": "DRAGONS",
    "Demon": "DEMONS",
    "Wolf": "WOLVES",
    "Tiger": "TIGERS",
}

# Load existing data or create new structure
try:
    with open(ELEVATED_USERS_FILE, "r") as f:
        data = json.load(f)
    for level, key in DISASTER_LEVELS.items():
        DISASTER_LEVELS[level] = data.get(key, [])
except (FileNotFoundError, json.JSONDecodeError):
    data = {v: [] for v in DISASTER_LEVELS.values()}
    with open(ELEVATED_USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


async def check_user_id(user_id: int) -> Optional[str]:
    if not isinstance(user_id, int) or user_id <= 0:
        return "Invalid user ID"
    return None


async def update_elevated_users():
    with open(ELEVATED_USERS_FILE, "w") as f:
        json.dump({v: DISASTER_LEVELS[k] for k, v in DISASTER_LEVELS.items()}, f, indent=4)


async def add_disaster_level(update: Update, level: str, context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    bot = context.bot
    args = context.args
    
    try:
        user_id = await extract_user(message, context, args)
        if not user_id:
            await message.reply_text("Please specify a valid user!")
            return ""
            
        user_member = await bot.get_chat(user_id)
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")
        return ""

    # Check user ID validity
    if error := await check_user_id(user_id):
        await message.reply_text(error)
        return ""

    # Get proper disaster level key
    level_key = DISASTER_LEVELS.get(level)
    if not level_key:
        await message.reply_text("Invalid disaster level!")
        return ""

    rt = ""
    current_level = None

    # Check existing levels
    for lvl, key in DISASTER_LEVELS.items():
        if user_id in key:
            current_level = lvl
            break

    if current_level:
        if current_level == level:
            await message.reply_text(f"This user is already a {level} Disaster!")
            return ""
        DISASTER_LEVELS[current_level].remove(user_id)
        rt += f"Demoted {user_member.first_name} from {current_level} "

    # Add to new level
    DISASTER_LEVELS[level].append(user_id)
    rt += f"\nPromoted {user_member.first_name} to {level} Disaster!"

    # Update storage
    await update_elevated_users()

    # Send confirmation
    await message.reply_text(rt)

    # Log action
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n" if message.chat.type != "private" else ""
    ) + (
        f"#{level.upper()}\n"
        f"<b>Admin:</b> {html.escape(user.first_name)}\n"
        f"<b>User:</b> {html.escape(user_member.first_name)}"
    )
    
    return log_message


@dev_plus
@gloggable
async def addsudo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    return await add_disaster_level(update, "Dragon", context)


@sudo_plus
@gloggable
async def addsupport(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    return await add_disaster_level(update, "Demon", context)


@sudo_plus
@gloggable
async def addwhitelist(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    return await add_disaster_level(update, "Wolf", context)


@sudo_plus
@gloggable
async def addtiger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    return await add_disaster_level(update, "Tiger", context)


# Handler setup
SUDO_HANDLER = CommandHandler("addsudo", addsudo, block=False)
SUPPORT_HANDLER = CommandHandler(("addsupport", "adddemon"), addsupport, block=False)
TIGER_HANDLER = CommandHandler("addtiger", addtiger, block=False)
WHITELIST_HANDLER = CommandHandler(("addwhitelist", "addwolf"), addwhitelist, block=False)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(SUPPORT_HANDLER)
dispatcher.add_handler(TIGER_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)

__mod_name__ = "Disaster Levels"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    TIGER_HANDLER,
    WHITELIST_HANDLER,
]
