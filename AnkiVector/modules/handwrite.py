import requests
from requests import get
from pyrogram.types import Message
from bs4 import *
from pyrogram import filters	
from AnkiVector.fsub import ForceSub
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot

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

@pbot.on_message(filters.command("write") & ~filters.edited & ~filters.bot)
async def write(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶Please give a text handwrite.")
     return
 m = await client.send_message(message.chat.id, "✍️ handwrite started..")
 try:
    text = get_text(message)
    API = 'https://single-developers.herokuapp.com/write'
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)   
    img = req.history[1].url
    fname = "shelaot.png"
    caption = f"""
✍️ Written Successfully✅
◇───────────────◇
👨‍💻 **Generated By** : [SheLaBot](https://t.me/TheSheLabot)
🙋‍♂️ **Requestor** : {}
⚡️ **Powered By **  : [CGS OFFICIAL [ᴜᴘᴅᴀᴛᴇꜱ]](https://t.me/CGSUpdates)
◇───────────────◇️
    
    """
    await m.delete()
    await client.send_photo(message.chat.id, photo=img, caption = caption,           
             reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{img}"
                    )
                ]
            ]
          ),
    )
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @slbotzone, {e}')
