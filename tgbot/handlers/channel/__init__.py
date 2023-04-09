from aiogram import Router


def get_channel_router():
    from . import post
    
    router = Router()
    router.include_router(post.router)
    
    return router
