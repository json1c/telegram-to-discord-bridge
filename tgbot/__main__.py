import asyncio
import logging

import coloredlogs
from aiogram import Bot, Dispatcher

from tgbot.config import Config, parse_config
from tgbot.handlers import get_handlers_router
from tgbot.middlewares import register_middlewares


async def on_startup(dispatcher: Dispatcher, bot: Bot, config: Config):
    register_middlewares(dp=dispatcher, config=config)

    bot_info = await bot.get_me()

    logging.info(f"Name - {bot_info.full_name}")
    logging.info(f"Username - @{bot_info.username}")
    logging.info(f"ID - {bot_info.id}")

    logging.debug(f"Groups Mode - {bot_info.can_join_groups}")
    logging.debug(f"Privacy Mode - {not bot_info.can_read_all_group_messages}")
    logging.debug(f"Inline Mode - {bot_info.supports_inline_queries}")

    logging.error("Bot started!")


async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    logging.warning("Stopping bot...")
    await dispatcher.fsm.storage.close()
    await bot.session.close()


async def main():
    coloredlogs.install(level=logging.INFO)

    router = get_handlers_router()
    config = parse_config("config.toml")
    dp = Dispatcher()

    bot = Bot(config.bot.telegram_token)

    dp.include_router(router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await dp.start_polling(bot, config=config)


if __name__ == "__main__":
    asyncio.run(main())
