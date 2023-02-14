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
<b>👋 ʜᴏɪ {m.from_user.mention}!

🗃️ ᴍᴜsɪᴄ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴜsᴇʀʙᴏᴛ

🔰 ᴛᴇʟᴇɢʀᴀᴍ ᴜsᴇʀʙᴏᴛ ᴛᴏ ᴘʟᴀʏ sᴏɴɢs ᴀɴᴅ ᴠɪᴅᴇᴏs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

👩‍💻 ᴏᴡᴇ ʙʏ 
• [ᴀᴇʟʟʏ](https://t.me/anu_pi)

📝 ʀᴇϙᴜɪʀᴇᴍᴇɴᴛs
• ᴘʏᴛʜᴏɴ 3.8+
• ғғᴍᴘᴇɢ
• ɴᴏᴅᴇᴊs ᴠ16+

📝 ʀᴇϙᴜɪʀᴇᴅ ᴠᴀʀɪᴀʙʟᴇs
• `ᴀᴘɪ_ɪᴅ` - ɢᴇᴛ ғʀᴏᴍ [ᴍʏ.ᴛᴇʟᴇɢʀᴀᴍ.ᴏʀɢ](ʜᴛᴛᴘs://ᴍʏ.ᴛᴇʟᴇɢʀᴀᴍ.ᴏʀɢ)
• `ᴀᴘɪ_ʜᴀsʜ` - ɢᴇᴛ ғʀᴏᴍ [ᴍʏ.ᴛᴇʟᴇɢʀᴀᴍ.ᴏʀɢ](ʜᴛᴛᴘs://ᴍʏ.ᴛᴇʟᴇɢʀᴀᴍ.ᴏʀɢ)
• `sᴇssɪᴏɴ` - ᴘʏʀᴏɢʀᴀᴍ sᴛʀɪɴɢ sᴇssɪᴏɴ.
• `sᴜᴅᴏ_ᴜsᴇʀ` -ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ɪᴅ ᴜsᴇᴅ ᴀs ᴀᴅᴍɪɴ
• `ʜɴᴅʟʀ` - ʜᴀɴᴅʟᴇʀ ᴛᴏ ʀᴜɴ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ
"""
    await m.reply(REPO, disable_web_page_preview=True)
