import random
from datetime import datetime
from pyrogram import filters
from Database.mongodb.karma_mongo import get_couple, save_couple
from Mikobot import app

# Additional images for couples
ADDITIONAL_IMAGES = [
    "https://telegra.ph/file/7ef6006ed6e452a6fd871.jpg",
    "https://telegra.ph/file/16ede7c046f35e699ed3c.jpg",
    "https://telegra.ph/file/f16b555b2a66853cc594e.jpg",
    "https://telegra.ph/file/7ef6006ed6e452a6fd871.jpg",
]

# Date functions
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    return dt_string.split(" ")

def dt_tom():
    day = int(dt()[0].split("/")[0]) + 1
    return f"{day}/{dt()[0].split('/')[1]}/{dt()[0].split('/')[2]}"

tomorrow = str(dt_tom())
today = str(dt()[0])

# Templates
C = """
•➵💞࿐ 𝐇𝐚𝐩𝐩𝐲 𝐜𝐨𝐮𝐩𝐥𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐝𝐚𝐲
╭──────────────
┊•➢ {} + ( PGM🎀😶 (https://t.me/Chalnayaaaaaarr) + 花火 (https://t.me/zd_sr07) + ゼロツー (https://t.me/wewewe_x) ) = 💞
╰───•➢♡
╭──────────────
┊•➢ 𝗡𝗲𝘄 𝗰𝗼𝘂𝗽𝗹𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗱𝗮𝘆 𝗺𝗮𝘆 𝗯𝗲 𝗰𝗵𝗼𝘀𝗲𝗻 𝗮𝘁 12AM {}
╰───•➢♡
"""

CAP = """
•➵💞࿐ 𝐇𝐚𝐩𝐩𝐲 𝐜𝐨𝐮𝐩𝐥𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐝𝐚𝐲
╭──────────────
┊•➢ {} + {} = 💞
╰───•➢♡
╭──────────────
┊•➢ 𝗡𝗲𝘄 𝗰𝗼𝘂𝗽𝗹𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗱𝗮𝘆 𝗺𝗮𝘆 𝗯𝗲 𝗰𝗵𝗼𝘀𝗲𝗻 𝗮𝘁 12AM {}
╰───•➢♡
"""

# Check permissions
async def check_permissions(bot, chat_id):
    try:
        chat = await bot.get_chat(chat_id)
        return chat.permissions.can_invite_users
    except Exception:
        return False

# Get valid user
async def get_valid_user(bot, user_id, chat_id):
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.user if member else None
    except Exception:
        return None

# Main couple function
@app.on_message(filters.command(["couple", "couples", "shipping"]) & ~filters.private)
async def nibba_nibbi(_, message):
    try:
        # Ensure bot has permissions
        if not await check_permissions(_, message.chat.id):
            return await message.reply_text("I don't have enough permissions to get chat members.")

        COUPLES_PIC = random.choice(ADDITIONAL_IMAGES)

        if message.from_user.id == 5540249238:
            me = await _.get_users(5540249238)
            await message.reply_photo(photo=COUPLES_PIC, caption=C.format(me.mention, tomorrow))
        else:
            chat_id = message.chat.id
            is_selected = await get_couple(chat_id, today)

            if not is_selected:
                list_of_users = [
                    i.user.id
                    async for i in _.get_chat_members(chat_id, limit=50)
                    if not i.user.is_bot
                ]

                if len(list_of_users) < 2:
                    return await message.reply_text("Not enough users in the group to form a couple.")

                c1_id, c2_id = random.sample(list_of_users, 2)

                c1_user = await get_valid_user(_, c1_id, chat_id)
                c2_user = await get_valid_user(_, c2_id, chat_id)

                if not c1_user or not c2_user:
                    return await message.reply_text("Error: Failed to fetch users. Please try again.")

                c1_mention = c1_user.mention
                c2_mention = c2_user.mention

                await _.send_photo(
                    chat_id,
                    photo=COUPLES_PIC,
                    caption=CAP.format(c1_mention, c2_mention, tomorrow),
                )

                couple = {"c1_id": c1_id, "c2_id": c2_id}
                await save_couple(chat_id, today, couple)

            else:
                # Retrieve previous couple
                c1_id = int(is_selected["c1_id"])
                c2_id = int(is_selected["c2_id"])

                c1_user = await get_valid_user(_, c1_id, chat_id)
                c2_user = await get_valid_user(_, c2_id, chat_id)

                if not c1_user or not c2_user:
                    return await message.reply_text("Error: One or both users are invalid or left the chat.")

                couple_selection_message = f"""
•➵💞࿐ 𝐇𝐚𝐩𝐩𝐲 𝐜𝐨𝐮𝐩𝐥𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐝𝐚𝐲
╭──────────────
┊•➢ [{c1_user.first_name}](tg://openmessage?user_id={c1_id}) + [{c2_user.first_name}](tg://openmessage?user_id={c2_id}) = 💞
╰───•➢♡
╭──────────────
┊•➢ 𝗡𝗲𝘄 𝗰𝗼𝘂𝗽𝗹𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗱𝗮𝘆 𝗺𝗮𝘆 𝗯𝗲 𝗰𝗵𝗼𝘀𝗲𝗻 𝗮𝘁 12AM {tomorrow}
╰───•➢♡"""
                await _.send_photo(chat_id, photo=COUPLES_PIC, caption=couple_selection_message)

    except Exception as e:
        print(e)
        await message.reply_text(f"An error occurred: {e}")
