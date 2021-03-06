from typing import Dict, List, Union

from modules.database.dblocal import db

pytgdb = db.pytg
admindb = db.admin


async def get_active_chats() -> list:
    chats = pytgdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_active_chat(chat_id: int) -> bool:
    chat = await pytgdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if is_served:
        return
    return await pytgdb.insert_one({"chat_id": chat_id})


async def remove_active_chat(chat_id: int):
    is_served = await is_active_chat(chat_id)
    if not is_served:
        return
    return await pytgdb.delete_one({"chat_id": chat_id})
