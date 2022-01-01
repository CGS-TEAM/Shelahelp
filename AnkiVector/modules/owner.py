from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram import idle, filters

OWNER_TEXT = """
*Oh 😉*
"""

@pbot.on_message(filters.regex("@kmsrk") & ~filters.private)
async def owner(_, message: Message):
    await message.reply_text(
                    caption=OWNER_TEXT)
