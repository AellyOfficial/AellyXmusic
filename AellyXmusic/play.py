import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch

from config import HNDLR, bot, call_py
from AellyXmusic.helpers.queues import QUEUE, add_to_queue, get_queue

AMBILFOTO = [
    "https://te.legra.ph//file/4f848bc6241d3d0d102a4.jpg",
    "https://te.legra.ph//file/4eea09e5c1d1b24c482f1.jpg",
    "https://te.legra.ph//file/ed3ce4aaa98a067cbb5cf.jpg",
    "https://te.legra.ph//file/53b05316855dddc2905ed.jpg",
    "https://te.legra.ph//file/f263b8db1d2d3ce730da4.jpg",
    "https://te.legra.ph//file/81a7bc189d6991b8a72f9.jpg",
    "https://te.legra.ph//file/32f001e5e781da1634c60.jpg",
    "https://te.legra.ph//file/d7727950966680f22aa98.jpg",
    "https://te.legra.ph//file/04ec0b973cbb57af01f7e.jpg",
    "https://te.legra.ph//file/663bee83808d3b7e26559.jpg",
    "https://te.legra.ph//file/3c2de51ace094867a2b88.jpg",
    "https://te.legra.ph//file/09cb375e560f108a147a9.jpg",
    "https://te.legra.ph/file/f6bc459cbca6d6d9bd431.jpg",
    "https://te.legra.ph/file/9b97db9da19a5ed703a84.jpg",
]

IMAGE_THUMBNAIL = random.choice(AMBILFOTO)


def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# music player
def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:35] + "..."
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
            duration = r["duration"]
        return [songname, url, duration]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


# video player
def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:35] + "..."
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
            duration = r["duration"]
        return [songname, url, duration]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(filters.command(["play"], prefixes=f"{HNDLR}"))
async def play(client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    m.chat.title
    if replied:
        if replied.audio or replied.voice:
            await m.delete()
            huehue = await replied.reply("**✧ ᴘʀᴏᴄᴇssɪɴɢ ʀᴇϙᴜᴇsᴛ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    songname = replied.audio.file_name[:35] + "..."
                duration = convert_seconds(replied.audio.duration)
            elif replied.voice:
                songname = "Voice Note"
                duration = convert_seconds(replied.voice.duration)
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/613f681a511feb6d1b186.jpg",
                    caption=f"""
**⌲ sᴏɴɢ ɪɴ ϙᴜᴇᴜᴇ ** `{pos}`
👀 **ᴛɪᴛʟᴇ:** [{songname}]({link})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **Request:** {m.from_user.mention}
""",
                )
            else:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/613f681a511feb6d1b186.jpg",
                    caption=f"""
**⌲ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ**
👀 **ᴛɪᴛʟᴇ:** [{songname}]({link})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ:** {m.from_user.mention}
""",
                )

    else:
        if len(m.command) < 2:
            await m.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴏғ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ғᴏʀ sᴇᴀʀᴄʜ")
        else:
            await m.delete()
            huehue = await m.reply("**✧ sᴇᴀʀᴄʜɪɴɢ ғᴏʀ sᴏɴɢ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await huehue.edit("`ғᴏᴜɴᴅ ɴᴏᴛʜɪɴ ғᴏʀ ɢɪᴠᴇɴ ϙᴜᴇʀʏ`")
            else:
                songname = search[0]
                url = search[1]
                duration = search[2]
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await huehue.edit(f"**ʏᴛᴅʟ ᴇʀʀᴏʀ ï¸** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await huehue.delete()
                        # await m.reply_to_message.delete()
                        await m.reply_photo(
                            photo=f"{IMAGE_THUMBNAIL}",
                            caption=f"""
**⌲ sᴏɴɢ ɪɴ ϙᴜᴇᴜᴇ ** `{pos}`
👀 **ᴛɪᴛʟᴇ:** [{songname}]({url})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ:** {m.from_user.mention}
""",
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await huehue.delete()
                            # await m.reply_to_message.delete()
                            await m.reply_photo(
                                photo=f"{IMAGE_THUMBNAIL}",
                                caption=f"""
**⌲ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ**
👀️ **ᴛɪᴛʟᴇ:** [{songname}]({url})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ:** {m.from_user.mention}
""",
                            )
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")


@Client.on_message(filters.command(["videoplay", "vplay"], prefixes=f"{HNDLR}"))
async def videoplay(client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    m.chat.title
    if replied:
        if replied.video or replied.document:
            await m.delete()
            huehue = await replied.reply("**✧ ᴘʀᴏᴄᴇssɪɴɢ ᴠɪᴅᴇᴏ....**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await huehue.edit(
                        "`Only 720, 480, 360 ᴀʟʟᴏᴡᴇᴅ` \n`ɴᴏᴡ sᴛᴇʀᴇᴀᴍɪɴɢ ɪɴ 720p`"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                elif replied.document:
                    songname = replied.document.file_name[:70]
            except BaseException:
                songname = "Video File"

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/613f681a511feb6d1b186.jpg",
                    caption=f"""
**⌲ ᴠɪᴅᴇᴏ ɪɴ ᴏᴜᴇᴜᴇ {pos}
👀️ ᴛɪᴛʟᴇ: [{songname}]({link})
💕 sᴛᴀᴛᴜs: Playing
😌 ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ: {m.from_user.mention}**
""",
                )
            else:
                if Q == 720:
                    hmmm = HighQualityVideo()
                elif Q == 480:
                    hmmm = MediumQualityVideo()
                elif Q == 360:
                    hmmm = LowQualityVideo()
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await m.reply_to_message.delete()
                await m.reply_photo(
                    photo="https://telegra.ph/file/613f681a511feb6d1b186.jpg",
                    caption=f"""
**⌲ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ
👀️ ᴛɪᴛʟᴇ: [{songname}]({link})
💕 sᴛᴀᴛᴜs: Playing
😌 ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ: {m.from_user.mention}**
""",
                )

    else:
        if len(m.command) < 2:
            await m.reply(
                "**ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴ ғᴏʀ sᴇsʀᴄʜ**"
            )
        else:
            await m.delete()
            huehue = await m.reply("**sᴇᴀʀᴄʜɪɴɢ sᴏɴɢ.. ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            hmmm = HighQualityVideo()
            if search == 0:
                await huehue.edit(
                    "**ғᴏᴜɴᴅ ɴᴏᴛʜɪɴɢ ғᴏʀ ϙᴜᴇʀʏ**"
                )
            else:
                songname = search[0]
                url = search[1]
                duration = search[2]
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await huehue.edit(f"**ʏᴛᴅʟ ᴇʀʀᴏʀ¸** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await huehue.delete()
                        # await m.reply_to_message.delete()
                        await m.reply_photo(
                            photo=f"{IMAGE_THUMBNAIL}",
                            caption=f"""
**⌲ ᴠɪᴅᴇᴏ ɪɴ ϙᴜᴇᴜᴇ** `{pos}`
👀️ **ᴛɪᴛʟᴇ:** [{songname}]({url})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ:** {m.from_user.mention}
""",
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await huehue.delete()
                            # await m.reply_to_message.delete()
                            await m.reply_photo(
                                photo=f"{IMAGE_THUMBNAIL}",
                                caption=f"""
**⌲ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ**
👀️ **ᴛɪᴛʟᴇ:** [{songname}]({url})
🥶 **ᴅᴜʀᴀᴛɪᴏɴ:** `{duration}`
💕 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`
😌 **ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ:** {m.from_user.mention}
""",
                            )
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")


@Client.on_message(filters.command(["playfrom"], prefixes=f"{HNDLR}"))
async def playfrom(client, m: Message):
    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply(
            f"**USAGE:** \n\n`{HNDLR}playfrom [chat_id/username]` \n`{HNDLR}playfrom [chat_id/username]`"
        )
    else:
        args = m.text.split(maxsplit=1)[1]
        if ";" in args:
            chat = args.split(";")[0]
            limit = int(args.split(";")[1])
        else:
            chat = args
            limit = 10
            lmt = 9
        await m.delete()
        hmm = await m.reply(f"**✧ ᴛᴀᴋᴇ {limit} ʀᴀɴᴅᴏᴍ sᴏɴɢ ғᴏʀᴍ {chat}**")
        try:
            async for x in bot.search_messages(chat, limit=limit, filter="audio"):
                location = await x.download()
                if x.audio.title:
                    songname = x.audio.title[:30] + "..."
                else:
                    songname = x.audio.file_name[:30] + "..."
                link = x.link
                if chat_id in QUEUE:
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                else:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(location),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                    # await m.reply_to_message.delete()
                    await m.reply_photo(
                        photo="https://telegra.ph/file/613f681a511feb6d1b186.jpg",
                        caption=f"""
**⌲ sᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢ ғʀᴏᴍ {chat}
👀️ ᴛɪᴛʟᴇ: [{songname}]({link})
💕 sᴛᴀᴛᴜs: Playing
😌 ᴜᴘᴏɴ ʀᴇϙᴜᴇsᴛ: {m.from_user.mention}**
""",
                    )
            await hmm.delete()
            await m.reply(
                f"âž• ᴀᴅᴅɪɴɢ {lmt} sᴏɴɢ ᴛᴏ ϙᴜᴇᴜᴇ\nâ€¢ ᴄʟʟɪᴄᴋ {HNDLR}ᴛᴏ ᴠɪᴇᴡ ᴘʟᴀʏʟɪsᴛ**"
            )
        except Exception as e:
            await hmm.edit(f"**ᴇʀʀᴏʀ** \n`{e}`")


@Client.on_message(filters.command(["playlist", "queue"], prefixes=f"{HNDLR}"))
async def playlist(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await m.delete()
            await m.reply(
                f"**✧ ɴᴏᴡ ᴘʟᴀʏɪɴɢ:** \n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`",
                disable_web_page_preview=True,
            )
        else:
            QUE = f"**✧ ɴᴏᴡ ᴘʟᴀʏɪɴɢ:** \n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}` \n\n**â¯ QUEUE LIST:**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                QUE = QUE + "\n" + f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`\n"
            await m.reply(QUE, disable_web_page_preview=True)
    else:
        await m.reply("**✧ ɴᴏᴛ ᴘʟᴀʏɪɴɢ ᴀɴᴜᴛʜɪɴɢ...**")
