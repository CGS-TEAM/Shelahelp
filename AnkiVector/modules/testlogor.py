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

@pbot.on_message(filters.command(["hlogo"]))
async def hlogo(bot, update):
    try:      
        name = message.text.split(None, 1)[1]
        req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}").json
        IMG = req['url']
        await update.reply_photo(photo=IMG) 
    except Exception as e:
        await update.reply_text(f"Error: {e}")
