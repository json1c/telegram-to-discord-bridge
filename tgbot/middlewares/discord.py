from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Update
from cachetools import TTLCache

from tgbot.config import Config
from tgbot.services.discord_api import DiscordAPI


class DiscordBotMiddleware(BaseMiddleware):
    def __init__(self, config: Config):
        self.discord = DiscordAPI(config.bot.discord_token)

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        data["discord"] = self.discord

        return await handler(event, data)


def register_middleware(dp: Dispatcher, config: Config):
    discord_bot_middleware = DiscordBotMiddleware(config=config)
    dp.channel_post.middleware(discord_bot_middleware)
