# <============================================== IMPORTS =========================================================>
import os
import aiohttp
from datetime import datetime
from PIL import Image
from pyrogram import filters
from Mikobot import app
from Mikobot.utils.errors import capture_err

# <=======================================================================================================>

TMP_DOWNLOAD_DIRECTORY = "tg-File/"
os.makedirs(TMP_DOWNLOAD_DIRECTORY, exist_ok=True)  # Ensure directory exists

# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command(["envs", "envsh", "envshare"], prefixes="/"))
@capture_err
async def envs_upload(client, message):
    if not message.reply_to_message:
        await message.reply_text("Reply to a file to upload it to Telegra.ph.")
        return

    r_message = message.reply_to_message
    
    if not (r_message.photo or r_message.document):
        await message.reply_text("Please reply to an image or file.")
        return

    try:
        start = datetime.now()
        downloaded_file_name = await client.download_media(
            r_message, file_name=TMP_DOWNLOAD_DIRECTORY
        )
        end = datetime.now()
        ms = (end - start).seconds
        h = await message.reply_text(f"Downloaded in {ms} seconds. Uploading to Telegra.ph...")

        # Convert WebP to PNG if needed
        if downloaded_file_name.lower().endswith(".webp"):
            resize_image(downloaded_file_name)

        file_url = await upload_to_telegraph(downloaded_file_name)
        
        if file_url:
            await h.edit_text(
                f"**✅ Uploaded to [Telegra.ph]({file_url})**\n"
                f"**🔗 Direct Link:** `{file_url}`",
                disable_web_page_preview=False
            )
        else:
            await h.edit_text("❌ Failed to upload to Telegra.ph. Check file format/size.")

    except Exception as e:
        await h.edit_text(f"❌ Error: {str(e)}")
    finally:
        if os.path.exists(downloaded_file_name):
            os.remove(downloaded_file_name)

async def upload_to_telegraph(file_path):
    try:
        async with aiohttp.ClientSession() as session:
            with open(file_path, "rb") as file:
                data = aiohttp.FormData()
                data.add_field('file', file, filename=os.path.basename(file_path))
                
                async with session.post("https://telegra.ph/upload", data=data) as response:
                    if response.status == 200:
                        result = await response.json()
                        if isinstance(result, list) and len(result) > 0 and 'src' in result[0]:
                            return f"https://telegra.ph{result[0]['src']}"
                    return None
    except Exception as e:
        print(f"Telegra.ph Upload Error: {e}")
        return None

def resize_image(image):
    try:
        with Image.open(image) as im:
            if im.format == 'WEBP':
                im.save(image, "PNG")
    except Exception as e:
        print(f"Image conversion error: {e}")
        raise
