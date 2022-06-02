from modules.database.import dbusers
from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command("status"), group=5)
async def status(bot, update):

    total_users = await db.total_users_count()
    text = "**ʙᴏᴛ sᴛᴀᴛᴜs**\n"
    text += f"\n**ᴛᴏᴛᴀʟ ᴜsᴇʀs:** `{total_users}`"

    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

