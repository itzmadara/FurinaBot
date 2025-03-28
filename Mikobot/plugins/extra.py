from time import gmtime, strftime, time
from pyrogram import filters
from pyrogram.types import Message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes
from Mikobot import LOGGER, app, function
from Mikobot.plugins.helper_funcs.chat_status import check_admin

UPTIME = time()

# Working sticker ID that won't cause MEDIA_EMPTY error
VALID_STICKER_ID = "CAACAgUAAxkBAAIBT2YvV4oVd5vAAW3XwABH-6_3y1rQZQAC8RYAAmRyiVRQ3T0vZ6wQqDAE"

@app.on_message(filters.command("id"))
async def get_id(client: Client, message: Message):
    try:
        chat = message.chat
        user = message.from_user
        text = f"**๏ [Message ID]({message.link})** » `{message.id}`\n"
        text += f"**๏ [{user.mention}](tg://user?id={user.id})** » `{user.id}`\n"
        
        if len(message.command) > 1:
            try:
                target_user = await client.get_users(message.command[1])
                text += f"**๏ [{target_user.mention}](tg://user?id={target_user.id})** » `{target_user.id}`\n"
            except Exception:
                await message.reply_text("User not found")
                return

        text += f"**๏ [Chat ID](https://t.me/{chat.username if chat.username else ''})** » `{chat.id}`\n"

        if message.reply_to_message:
            reply = message.reply_to_message
            text += f"\n**๏ [Replied Message ID]({reply.link})** » `{reply.id}`\n"
            text += f"**๏ [Replied User ID](tg://user?id={reply.from_user.id})** » `{reply.from_user.id}`\n"

            if reply.forward_from_chat:
                text += f"\n๏ Forwarded channel {reply.forward_from_chat.title} has ID `{reply.forward_from_chat.id}`\n"
            
            if reply.sender_chat:
                text += f"\n๏ Replied chat/channel ID: `{reply.sender_chat.id}`"

        # Send the sticker first
        await message.reply_sticker(sticker=VALID_STICKER_ID)
        # Then send the text
        await message.reply_text(text, disable_web_page_preview=True)

    except Exception as e:
        LOGGER.error(f"Error in /id command: {e}")
        await message.reply_text("An error occurred while processing your request.")

@check_admin(only_dev=True)
async def send_logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        try:
            with open("Logs.txt", "rb") as log_file:
                await context.bot.send_document(
                    chat_id=user.id,
                    document=log_file,
                    filename="Logs.txt",
                    caption="Bot logs",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Close", callback_data="close_logs")]
                    ])
                )
        except FileNotFoundError:
            await update.message.reply_text("Log file not found")
    except Exception as e:
        LOGGER.error(f"Error in logs command: {e}")
        await update.message.reply_text("Failed to send logs")

async def close_logs_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.delete()

@app.on_message(filters.command("pyroping"))
async def pyro_ping(_, message: Message):
    try:
        start_time = time()
        reply_msg = await message.reply_text("Pinging...")
        delta_ping = (time() - start_time) * 1000  # Convert to milliseconds
        
        uptime = strftime("%Hh %Mm %Ss", gmtime(time() - UPTIME))
        
        await reply_msg.edit_text(
            f"<b>Pyro-Pong!</b>\n"
            f"<code>{delta_ping:.3f} ms</code>\n\n"
            f"Uptime: <code>{uptime}</code>"
        )
    except Exception as e:
        LOGGER.error(f"Error in pyroping: {e}")
        await message.reply_text("Failed to calculate ping")

# Register handlers
function(CommandHandler("logs", send_logs, block=False))
function(CallbackQueryHandler(close_logs_callback, pattern="^close_logs$", block=False))

__help__ = """
➠ *Commands*:
» /id - Get user and chat IDs
» /pyroping - Check bot response time
» /logs - Get bot logs (admin only)
"""

__mod_name__ = "EXTRA"
