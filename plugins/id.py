## ©copyright infringement on Team Shadow Projects
## support: https://t.me/tgshadow_fighters
## network: https://t.me/teamshadowprojects



from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
from modules.helpers.filters import command
from modules.helpers.command import commandpro

@Client.on_message(command("id") & ~filters.edited) 
async def id(c: Client, message: Message):
    text = """
**ᴛʜɪs ɪs ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ** : `{}`"""
    await message.reply_text(
        text=text.format(
            message.chat.id
        ), 
    ) 


@Client.on_callback_query(filters.regex("id"))
async def id(_, query: CallbackQuery):
    await query.answer("chat id")
    await query.edit_message_text(
        f"""👋🏻 **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
➠ **/id ᴛʏᴘᴇ ɪᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀʀᴇ ᴘᴇʀsᴏɴᴀʟ !**""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("•◁•", callback_data="command_list")]]
        ),
    )
