# <============================================== IMPORTS =========================================================>
import os
import requests
from datetime import datetime
from PIL import Image
from pyrogram import filters
from Mikobot import app
from Mikobot.utils.errors import capture_err

# <=======================================================================================================>

TMP_DOWNLOAD_DIRECTORY = "tg-File/"

# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command(["envs", "envsh", "envshare"], prefixes="/"))
@capture_err
async def envs_upload(client, message):
    if message.reply_to_message:
        r_message = message.reply_to_message
        
        # Check if the replied message is an image or file
        if not (r_message.photo or r_message.document):
            await message.reply_text("Please reply to an image or file.")
            return

        start = datetime.now()
        downloaded_file_name = await client.download_media(
            r_message, file_name=TMP_DOWNLOAD_DIRECTORY
        )
        end = datetime.now()
        ms = (end - start).seconds
        h = await message.reply_text(f"Downloaded in {ms} seconds. Uploading to Telegra.ph...")

        # Convert WebP to PNG if needed
        if downloaded_file_name.endswith(".webp"):
            resize_image(downloaded_file_name)

        try:
            # Upload to Telegra.ph
            file_url = await upload_to_telegraph(downloaded_file_name)

            if file_url:
                await h.edit_text(
                    f"**✅ Uploaded to [Telegra.ph]({file_url})**\n"
                    f"**🔗 Direct Link:** `{file_url}`",
                    disable_web_page_preview=False
                )
            else:
                await h.edit_text("❌ Failed to upload to Telegra.ph.")
        except Exception as e:
            await h.edit_text(f"❌ Error: {str(e)}")
        finally:
            os.remove(downloaded_file_name)
    else:
        await message.reply_text("Reply to a file to upload it to Telegra.ph.")


async def upload_to_telegraph(file_path):
    try:
        # Upload file to telegra.ph
        with open(file_path, "rb") as file:
            response = requests.post(
                "https://telegra.ph/upload",
                files={"file": file}
            )

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and 'src' in result[0]:
                return f"https://telegra.ph{result[0]['src']}"
        return None
    except Exception as e:
        print(f"Telegra.ph Upload Error: {e}")
        return None

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")

# <=================================================== HELP ====================================================>
__help__ = """ 
➠ **TELEGRA.PH UPLOAD**:
» `/envs`, `/envsh`, `/envshare` - Upload a file to Telegra.ph (Image Upload Service)
"""
__mod_name__ = "TELEGRA.PH"
# <================================================ END =======================================================>
