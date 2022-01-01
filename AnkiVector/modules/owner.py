from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram import idle, filters

OWNER_TEXT = """
*Oh 😉*
"""

@pbot.on_message(filters.regex(@kmsrk))
async def owner(client, message):
    await message.reply_text(
                    caption=OWNER_TEXT)
