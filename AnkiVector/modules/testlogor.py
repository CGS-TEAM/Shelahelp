import os
import io
import requests
from bs4 import *
from pyrogram import filters, Client
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot
from AnkiVector.fsub import ForceSub
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

@pbot.on_message(filters.command(["sdlogo"]))
async def logo(bot, update):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await update.reply_text(message.chat.id, "😶 **Please Give me A Text For The Logo**.")
     return
 m = await update.reply_text(message.chat.id, "`⚙️ Creating Your logo..`")
 try:      
    name = update.text.split(None, 1)[1]
    req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
    IMG = req.text
    await update.reply_photo(messege.chat.id, photo = IMG, caption = caption.format(message.from_user.mention)) 
 except Exception as e:
    await update.reply_text(f"Error: {e}")

                     
caption = """
✍️ Logo Generated Successfully✅
◇───────────────◇
👨‍💻 **Generated By** : [SheLaBot](https://t.me/TheSheLabot)
🙋‍♂️ **Requestor** : {}
⚡️ **Powered By **  : [CGS OFFICIAL [ᴜᴘᴅᴀᴛᴇꜱ]](https://t.me/CGSUpdates)
◇───────────────◇️  
"""
# ==================== Logo ====================

