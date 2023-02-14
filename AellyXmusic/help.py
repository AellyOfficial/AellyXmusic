# Aelly [@AellyOfficial
# Don't remove credits ⚠️

import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋ʜᴏɪ {m.from_user.mention}!

🛠 ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ

⚡ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴇᴠᴇʀʏᴏɴᴇ
• {HNDLR}ᴘʟᴀʏ [sᴏɴɢ ᴛɪᴛʟᴇ | ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ | ʀᴇᴘʟʏ ᴀᴜᴅɪᴏ ғɪʟᴇ] - ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ
• {HNDLR}ᴠɪᴅᴇᴏᴘʟᴀʏ [ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ | ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ | ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ғɪʟᴇ] - ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ
• {HNDLR}ᴘʟᴀʏʟɪsᴛ ᴛᴏ ᴠɪᴇᴡ ᴘʟᴀʏʟɪsᴛ
• {HNDLR}ᴘɪɴɢ - ᴛᴏ ᴄʜᴇᴄᴋ sᴛᴀᴛᴜs
• {HNDLR}ɪᴅ - ᴛᴏ sᴇᴇ ᴜsᴇʀ ɪᴅ
• {HNDLR}ᴠɪᴅᴇᴏ - ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ | ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴛᴏ sᴇᴀʀᴄʜ ᴠɪᴅᴇᴏ
• {HNDLR}sᴏɴɢ - sᴏɴɢ ᴛɪᴛʟᴇ | ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ sᴏɴɢs
• {HNDLR}ʜᴇʟᴘ - ᴛᴏ sᴇᴇ ᴀ ʟɪsᴛ ᴏғ ᴄᴏᴍᴍᴀɴᴅs
• {HNDLR}ᴊᴏɪɴ- ᴛᴏ ᴊᴏɪɴ | ᴛᴏ ɢʀᴏᴜᴘ 

⚡ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴀʟʟ ᴀᴅᴍɪɴs
• {HNDLR}ʀᴇsᴜᴍᴇ - ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ᴘʟᴀʏɪɴɢ ᴀ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ
• {HNDLR}ᴘᴀᴜsᴇ - ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ ᴘʟᴀʏʙᴀᴄᴋ ᴏғ ᴀ sᴏɴɢ ᴏʀ ᴠɪᴅᴇᴏ
• {HNDLR}sᴋɪᴘ - ᴛᴏ sᴋɪᴘ sᴏɴɢs ᴏʀ ᴠɪᴅᴇᴏs
• {HNDLR}ᴇɴᴅ - ᴛᴏ ᴇɴᴅ ᴘʟᴀʏʙᴀᴄᴋ</ʙ>
"""
    await m.reply(HELP)
