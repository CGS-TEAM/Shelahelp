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
    try:      
        name = update.text.split(None, 1)[1]
        req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
        IMG = req.text
        await update.reply_text("⚙️ Creating logo plz wait..")
        return
        await update.reply_photo(photo = IMG, caption = caption) 
    except Exception as e:
        await update.reply_text(f"Error: {e}")

                     
caption = """
✍️ Logo Generated Successfully✅
◇───────────────◇
👨‍💻 **Generated By** : [SheLaBot](https://t.me/TheSheLabot)
⚡️ **Powered By **  : [CGS OFFICIAL [ᴜᴘᴅᴀᴛᴇꜱ]](https://t.me/CGSUpdates)
◇───────────────◇️  
"""
# ==================== Logo ====================
