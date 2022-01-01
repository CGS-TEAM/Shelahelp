import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot


@pbot.on_message(filters.text
                   & filters.group
                   & ~filters.edited
                   & filters.regex(@kmsrk))
async def ytdl_with_button(_, message: Message):
    await message.reply_text(
        "**Oh 😉 **",
