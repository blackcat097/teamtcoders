from pyrogram import idle
from pyrogram import Client as Bot
from modules.clientbot import run
from modules.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from pyrogram import Client
from pytgcalls import PyTgCalls
    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)



with Client(":teamshadow:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()

bot.start()
run()
idle()
