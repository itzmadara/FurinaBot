import os
import requests
from datetime import datetime
from PIL import Image
from pyrogram import filters
from Mikobot import app
from Mikobot.utils.errors import capture_err

TMP_DOWNLOAD_DIRECTORY = "tg-File/"

@app.on_message(filters.command(["envs", "envsh", "envshare"], prefixes="/"))
@capture_err
async def envs_upload(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a file to upload it to envs.sh.")

    r_message = message.reply_to_message
    if not (r_message.photo or r_message.document):
        return await message.reply_text("Only images/files are supported.")

    start = datetime.now()
    downloaded_file_name = await client.download_media(
        r_message, file_name=TMP_DOWNLOAD_DIRECTORY
    )
    if not downloaded_file_name:
        return await message.reply_text("Failed to download the file.")

    # Convert WebP to PNG if needed
    if downloaded_file_name.lower().endswith(".webp"):
        resize_image(downloaded_file_name)

    h = await message.reply_text("Uploading to envs.sh...")

    try:
        with open(downloaded_file_name, "rb") as file:
            response = requests.post(
                "https://envs.sh",
                files={"file": (os.path.basename(downloaded_file_name), file)},
                timeout=10
            )
        
        if response.status_code == 200:
            # Try parsing JSON first, fallback to text
            try:
                file_url = response.json().get("url", response.text.strip())
            except:
                file_url = response.text.strip()
            
            await h.edit_text(
                f"**✅ Uploaded Successfully!**\n"
                f"**🔗 URL:** {file_url}\n"
                f"**📁 File:** `{os.path.basename(downloaded_file_name)}`",
                disable_web_page_preview=False
            )
        else:
            await h.edit_text(f"❌ Upload Failed (Status: {response.status_code})")
    except Exception as e:
        await h.edit_text(f"❌ Error: {str(e)}")
    finally:
        if os.path.exists(downloaded_file_name):
            os.remove(downloaded_file_name)

def resize_image(image_path):
    try:
        im = Image.open(image_path)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        im.save(image_path, "PNG")
    except Exception as e:
        print(f"Image conversion error: {e}")

__help__ = """ 
➠ **Upload Files to envs.sh**:
» `/envs`, `/envsh`, `/envshare` - Upload any file and get a direct link.
"""
__mod_name__ = "File Upload"
