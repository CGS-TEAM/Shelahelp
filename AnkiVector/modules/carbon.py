from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot, aiohttpsession as session
from AnkiVector.fsub import ForceSub

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

BUTTON = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="Join Bot Updates 🌷", url=f"https://t.me/CGSUpdates") 
        ],
        [
         InlineKeyboardButton(text="➕ADD SHELA YOUR GROUP➕", url=f"http://t.me/TheSheLaBot?startgroup=botstart") 
        ]
      ]      
    )

TEXT=f"""
Carbon create successfuly ✅✅

❋ ▱▱▰▰▱▱▰▰▱▱▰▰ ❋
  Powered By : [SheLa Bot](https://t.me/TheSheLaBot)
❋ ▱▱▰▰▱▱▰▰▱▱▰▰ ❋
"""


@pbot.on_message(filters.command(["carbon", f"carbon@TheSheLaBot"]))
async def carbon_func(client, message):
    FSub = await ForceSub(client, message)
    if FSub == 400:
        return
    if not message.reply_to_message:
        return await message.reply_text("Reply to a text message.")
    if not message.reply_to_message.text:
        return await message.reply_text("Reply to a text message.")
    m = await message.reply_text("Preparing")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await client.send_photo(message.chat.id, carbon,caption=TEXT,reply_markup= BUTTON)
    await m.delete()
    carbon.close()
