from pyrogram import idle
from pyrogram import Client as Bot
from modules.clientbot import run
from modules.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)


santhu = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(santhu,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(santhu, overload_quiet_mode=True)

with Client(":santhu:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with santhu as app:
    me_santhu = app.get_me()

bot.start()
run()
idle()
