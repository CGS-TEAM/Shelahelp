import os
import io
import requests
from bs4 import *
from pyrogram import filters	
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot
from AnkiVector.fsub import ForceSub
from AnkiVector import pbot as rose
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from requests import get
from pyrogram.types import Message

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
      
caption = """
✍️ Logo Generated Successfully✅
◇───────────────◇
👨‍💻 **Generated By** : [SheLaBot](https://t.me/TheSheLabot)
🙋‍♂️ **Requestor** : {}
⚡️ **Powered By **  : [CGS OFFICIAL [ᴜᴘᴅᴀᴛᴇꜱ]](https://t.me/CGSUpdates)
◇───────────────◇️  
"""
# ==================== Logo ====================

@pbot.on_message(filters.command("logo") & ~filters.edited & ~filters.bot)
async def logo(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶 **Please Give me A Text For The Logo**.")
     return
 m = await client.send_message(message.chat.id, "`⚙️ Creating Your logo..`")
 try:
    text = get_text(message)
    LOGO_API = f"https://single-developers.up.railway.up/logo?name={text}"
    randc = (LOGO_API)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    murl = requests.get(f"http://single-developers.up.railway.up/logo?name={text}").history[1].url
    fname = "szrosebot.png"
    img.save(fname, "png")
    await client.send_photo(message.chat.id, photo=murl, caption = caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{murl}"
                    )
                ],
            ]
          ),
    )
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @CGSsupport, {e}')
    await m.delete()

@rose.on_callback_query(filters.regex("picme"))
async def mylogo(_, query):
    mode = query.data.split()[1].strip()
    picmetext = picmetxt.format(query.from_user.mention)
    if mode == "me" and query.from_user.photo:
        await query.answer("😊Capture started....\n🤝share & support us\n@CGSsupport", show_alert=True)
        photoid = query.from_user.photo.big_file_id  
        photo = await rose.download_media(photoid)
        await query.edit_message_media(InputMediaPhoto(media=photo, caption = caption.format(message.from_user.mention)),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("◈──✌️Pic Me🙈──◈", callback_data="picme me")
                ],
                [
                    InlineKeyboardButton("◈──💁‍♂️Send Pm──◈", callback_data="picme pm")
                ],
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{murl}"
                    )
                ],
            ]
          ),)
        if os.path.exists(photo):os.remove(photo)
    if mode == "pm":
        try:
            photo = await rose.download_media(query.message.photo.file_id)
            await rose.send_photo(query.from_user.id, photo=photo, caption=caption.format(query.from_user.mention))
            if os.path.exists(photo):os.remove(photo)   
            return await query.answer("🥲 Sent to PM, Check your pm now.\n🎯share & support us\n@CGSsupport", show_alert=True) 
        except Exception as e:
            await query.answer("Please Frist Start This 👉 @TheSheLabot")
            print(str(e))
            if os.path.exists(photo):os.remove(photo)    
    
    
