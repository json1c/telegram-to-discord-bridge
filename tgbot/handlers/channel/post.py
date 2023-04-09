from aiogram import F, Router, types

from tgbot.config import parse_config
from tgbot.services.discord_api import DiscordAPI

config = parse_config("config.toml")

router = Router()


@router.channel_post(F.chat.id == config.settings.telegram_channel_id)
async def forward_to_discord(message: types.Message, discord: DiscordAPI):
    await discord.send_message(
        config.settings.discord_channel_id,
        f"{message.text}\n\n{config.settings.caption}"
    )
