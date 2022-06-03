







@Client.on_message(command("id") & ~filters.edited) 
async def id(c: Client, message: Message):
    text = """
**ᴛʜɪs ɪs ʏᴏᴜʀ ᴄʜᴀᴛ ɪᴅ** : `{}`"""
    await message.reply_text(
        text=text.format(
            message.chat.id
        ), 
    ) 
