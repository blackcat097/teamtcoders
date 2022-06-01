## ©copyright infringement on Team Shadow Projects
## support: https://t.me/tgshadow_fighters
## network: https://t.me/teamshadowprojects


import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from image import START_IMG_URL, BOT_USERNAME, GROUP_SUPPORT, BOT_NAME
import random
from pyrogram.errors import UserNotParticipant
from plugins import __version__
from modules.__main__ import bot, me_bot
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
force_channel = "teamshadowprojects"

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):   
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, message.from_user.id) 
            if user.status == "kicked out":
                await message.reply_text("You are banned") 
                return
        except UserNotParticipant:
            await message.reply_photo(
                photo=random.choice(START_IMG_URL),
                caption="👋🏻ʜᴇʟʟᴏ {message.from_user.mention()} ʏᴏᴜʀ ɴᴏᴛ sᴜʙsᴄʀɪʙᴇ ᴍʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇ ᴀɴᴅ ᴜsᴇ ᴍᴇ..🔥", 
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔰ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ🔰", url=f"t.me/{force_channel}") 
                 ]]
                ) 
            )
            return
    await message.reply_photo(
        photo=random.choice(START_IMG_URL),
        caption=f"""**
👋🏻ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ 

ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs..
 
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) **
""",
    reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("• sᴜᴘᴘᴏʀᴛ", url="https://t.me/tgshadow_fighters"), 
            InlineKeyboardButton("• ᴄʜᴀɴɴᴇʟ", url="https://t.me/teamshadowprojects"), 
            ],[
            InlineKeyboardButton("• ɪɴғᴏʀᴍᴀᴛɪᴏɴ", callback_data="info"), 
            InlineKeyboardButton("• ᴅᴏɴᴀᴛᴇ", user_id=5287160769), 
            ],[
            InlineKeyboardButton("✚ ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ]]
            ) 
        ) 
    
    
@Client.on_message(commandpro(["/alive", "shadow"]) & filters.group & ~filters.edited)
async def alive(client: Client, message: Message):
    await message.reply_photo(
        photo=random.choice(START_IMG_URL),
        caption=f"""ʜᴇʟʟᴏ.. {message.from_user.mention()} ɪᴀᴍ ᴀʟɪᴠᴇ ɴᴏᴡ ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "(: ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="info")
                ]
            ]
        ),
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/02daf1a0d434a29f9d54c.jpg",
        caption=f""" ✨ **ʜᴇʟʟᴏ {message.from_user.mention()} !**\n
💘 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ sᴇᴛᴜᴘ ᴛʜɪs ʙᴏᴛ? ʀᴇᴀᴅ 💖 sᴇᴛᴛɪɴɢ ᴜᴘ ᴛʜɪs ʙᴏᴛ ɪɴ ɢʀᴏᴜᴘ **\n
💗 **ᴛᴏ ᴋɴᴏᴡ ᴘʟᴀʏ /ᴀᴜᴅɪᴏ? ʀᴇᴀᴅ 💖 ǫᴜɪᴄᴋ ᴜsᴇ ᴄᴏᴍᴍᴀɴᴅs **\n
💝 **ᴛᴏ ᴋɴᴏᴡ ᴇᴠᴇʀʏ sɪɴɢʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏғ ʙᴏᴛ? ʀᴇᴀᴅ 💖 ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs**\n """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ", callback_data="command_list")
                ]
            ]
        ),
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(c: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=random.choice(START_IMG_URL), 
        caption="😊 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ʙᴏᴛ sᴛᴀᴛᴜs:\n"
                f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
                f"• **ᴜsᴇʀ:** `{message.from_user.mention()}`\n"
                f"• **sᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`\n"
                f"• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** `{GROUP_SUPPORT}`"
              ) 


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(c: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text("💝 `ᴘᴏɴɢ!!`\n" f"💖 `{delta_ping * 1000:.3f} ms`")


@Client.on_callback_query(filters.regex("home_start"))
async def start_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("home start")
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ {message.from_user.mention()} ɪᴀᴍ ᴀ ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ᴍᴜsɪᴄ ʙᴏᴛ ɪᴀᴍ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ! **
**ɢʀᴏᴜᴘs ᴡɪᴛʜ sᴏᴍᴇ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs..**

**ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) !**
""", 
       ) 

@Client.on_callback_query(filters.regex("command_list"))
async def commands_set(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("command listlist") 
    await query.edit_message_text(
        f"""💗 ᴄᴏᴍᴍᴀɴᴅ ʟɪsᴛ ғᴏʀ ᴀʟʟ ᴜsᴇʀ.
» /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ
» /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs
» /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs
» /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)
» /help - ᴛᴏ sʜᴏᴡ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ (ғᴜʟʟ ʙᴏᴛ ɢᴜɪᴅᴇ)
⚡️ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} ᴀɪ__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "◁", callback_data="home_start")
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex("info"))
async def info(_, query: CallbackQuery):
    BOT_NAME = me_bot.first_name
    await query.answer("information")
    await query.edit_message_text(
        f"""✨ ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !
💘 ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ ɪs ᴀ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ɪɴ ʜᴇʀᴏᴋᴜ, ɪᴛ's ᴏɴʟɪɴᴇ sɪɴᴄᴇ 𝟷sᴛ ᴊᴜɴᴇ 𝟸𝟶𝟸𝟸 ᴀɴᴅ ɪᴛ's ᴄᴏɴsᴛᴀɴᴛʟʏ ᴜᴘᴅᴀᴛᴇᴅ \n
💗 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: v{version} \n
💝 ᴛʜɪs ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters) \n 
❣️ © ᴏɴ ʙᴇʜᴀʟғ ᴏғ [ᴛᴇᴀᴍ sʜᴀᴅᴏᴡ](https://t.me/tgshadow_fighters)
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="help_command")]]
        ),
    )
