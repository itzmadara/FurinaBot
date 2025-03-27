# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/1b90f5a97abd259ff90d7-bf5915ad61711c0bf1.jpg",
    "https://telegra.ph/file/97a45a0f204821b758676-5115862a68714376e3.jpg",
    "https://telegra.ph/file/f0cb5e32b65e517002fb9-2346f210cc0ce1ca32.jpg",
    "https://telegra.ph/file/f392b911407a738d3ba99-46a710b5ae05477eeb.jpg",
    "https://telegra.ph/file/b96cb69cf364b3c5c5638-c9f36de5df917ae38a.jpg",
    "https://telegra.ph/file/da3b0fe110c6cee663b57-eb6e3ad0e68f21e054.jpg",
    "https://telegra.ph/file/b40a58989d456234c827b-52bd898870fc0d49ee.jpg",
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
🫧 *ʀᴀɪᴅᴇɴ* 🫧 [ㅤ](https://telegra.ph/file/d0a9888e9ecc025550d59-8b8f77f6642294a148.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
