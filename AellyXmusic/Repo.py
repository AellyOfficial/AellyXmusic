#Aelly [ @AellyOfficial
# Don't remove credits ⚠️


import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hoi {m.from_user.mention}!

🗃️ Music And Video Player UserBot

🔰 Telegram UserBot To Play Songs And Videos In Telegram Voice Chat.

👩‍💻 Owe by 
• [Aelly](https://t.me/anu_pi)

📝 Requirements
• Python 3.8+
• FFMPEG
• Nodejs v16+

[Anu](https://t.me/an_unic_or_n47)

📝 Required Variables
• `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
• `SESSION` - Pyrogram String Session.
• `SUDO_USER` -Telegram Account ID Used As Admin
• `HNDLR` - Handler to run your userbot
"""
    await m.reply(REPO, disable_web_page_preview=True)
