from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnkiVector import pbot, aiohttpsession as session
from AnkiVector.fsub import ForceSub

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
      
async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

text = get_text(message)
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
    if not message.reply_text:
        return await message.reply_text("give a name.")
    if not message.reply_text:
        return await message.reply_text("Reply to a text message.")
    m = await message.reply_text("⚙️ Please wait creating carbon..")
    carbon = await make_carbon.text
    await m.edit("Uploading")
    await client.send_photo(message.chat.id, carbon,caption=TEXT,reply_markup= BUTTON)
    await m.delete()
    carbon.close()
