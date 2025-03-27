# <============================================== IMPORTS =========================================================>
import os
from datetime import datetime

from PIL import Image
from pyrogram import filters
from telegraph import Telegraph, exceptions, upload_file

from Mikobot import app
from Mikobot.utils.errors import capture_err

# <=======================================================================================================>

TMP_DOWNLOAD_DIRECTORY = "tg-File/"
bname = "YaeMiko_Roxbot"  # ᴅᴏɴ'ᴛ ᴇᴅɪᴛ ᴛʜɪs ʟɪɴᴇ
telegraph = Telegraph()
r = telegraph.create_account(short_name=bname)
auth_url = r["auth_url"]


# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command(["tgm", "tmg", "telegraph"], prefixes="/"))
@capture_err
async def telegraph_upload(client, message):
    if message.reply_to_message:
        r_message = message.reply_to_message
        # Check if the replied message is an image
        if not (r_message.photo or (r_message.document and "image" in r_message.document.mime_type)):
            await message.reply_text("Please reply to an image file.")
            return

        start = datetime.now()
        downloaded_file_name = await client.download_media(
            r_message, file_name=TMP_DOWNLOAD_DIRECTORY
        )
        end = datetime.now()
        ms = (end - start).seconds
        h = await message.reply_text(f"Downloaded to file in {ms} seconds.")
        
        # Convert WebP to PNG if necessary
        if downloaded_file_name.endswith(".webp"):
            resize_image(downloaded_file_name)
        
        try:
            start = datetime.now()
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await h.edit_text(f"Error: {str(exc)}")
            os.remove(downloaded_file_name)
        else:
            # Check if media_urls is a list and not empty
            if isinstance(media_urls, list) and len(media_urls) > 0:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await h.edit_text(
                    f"""
➼ **Uploaded to [Telegraph](https://telegra.ph{media_urls[0]}) in {ms + ms_two} seconds.**\n 
➼ **Copy Link :** `https://telegra.ph{media_urls[0]}`""",
                    disable_web_page_preview=False,
                )
            else:
                await h.edit_text("Error uploading to Telegraph. Invalid response received.")
                os.remove(downloaded_file_name)
    else:
        await message.reply_text(
            "Reply to a message to get a permanent telegra.ph link."
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


# <=================================================== HELP ====================================================>
__help__ = """ 
➠ *TELEGRAPH*:

» /tgm, /tmg, /telegraph*:* `Get a Telegraph link for the replied image.`
 """

__mod_name__ = "TELEGRAPH"
# <================================================ END =======================================================>
