from aiogram import Dispatcher

from tgbot.config import Config


def register_middlewares(dp: Dispatcher, config: Config):
    from . import discord
    
    discord.register_middleware(dp, config)
    
