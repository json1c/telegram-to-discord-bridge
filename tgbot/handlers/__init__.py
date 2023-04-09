from aiogram import Router


def get_handlers_router():
    from . import channel
    
    router = Router()
    channel_router = channel.get_channel_router()
    router.include_router(channel_router)
    
    return router
