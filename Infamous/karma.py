# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/f426d88230795d1fdf3a1-e6ceb7628d7c82c236.jpg",
    "https://telegra.ph/file/2c9896c728b9475fe075f-bd65e022804aa17787.jpg",
    "https://telegra.ph/file/f00924ffe442b1a288c17-b47ded1a63ebeb1fa2.jpg",
    "https://telegra.ph/file/7a44dfd5e4ca52b2ff578-bdeef004789e9c96cd.jpg",
    "https://telegra.ph/file/d1cd41d4352c6b4f5b459-4dc463d3ace2e0baa9.jpg",
    "https://telegra.ph/file/c0f46801453fd1cb7e89f-6f56d5117f3c70fb63.jpg",
    "https://telegra.ph/file/1624216d188b2ef68f5ed-da54abf587fd4eb8a1.jpg",
]

HEY_IMG = "https://telegra.ph/file/ec699b8d507d1a7611067-c1012daccba3ef9dd1.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/68940987fb2fff34d2c32-376015f799ee66aa5b.jpg",
    "https://telegra.ph/file/ace1442303afb84d3f1c0-10cfaf69755eaeba3c.jpg",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ʀᴀɪᴅᴇɴ, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="extra_command_handler"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="SUPPORT", url="https://t.me/raiden_gc"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Anime_Station_Bots"),
        ib(text="SUPPORT", url="https://t.me/raiden_gc"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ʀᴀɪᴅᴇɴ* 🫧 [ㅤ](https://telegra.ph/file/d1cd41d4352c6b4f5b459-4dc463d3ace2e0baa9.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
