import keepalive  # ✅ REQUIRED for Render free port issue

import asyncio
import importlib

from pyrogram import idle

import config
from SONALI import LOGGER, app, userbot
from SONALI.core.call import RAUSHAN
from SONALI.misc import sudo
from SONALI.plugins import ALL_MODULES
from SONALI.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "STRING SESSION NOT FILLED, PLEASE FILL PYROGRAM V2 SESSION"
        )

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("SONALI.plugins" + all_module)

    LOGGER("SONALI.plugins").info("ALL FEATURES LOADED SUCCESSFULLY")

    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()

    LOGGER("SONALI").info("SONALI MUSIC BOT STARTED")

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("SONALI").info("SONALI MUSIC BOT STOPPED")


if __name__ == "__main__":
    asyncio.run(init())
