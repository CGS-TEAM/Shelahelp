from datetime import datetime, timedelta
from pyrogram import Client, filters, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.regex(@kmsrk))
async def ytdl(_, message):
    await message.reply_text(f"*Oh 😉")
            
