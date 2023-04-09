import aiohttp


class DiscordAPI:
    endpoint_url = "https://discord.com/api/v10/"
    
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.session = None
        
    async def request(self, path: str, data: dict):
        if self.session is None:
            self.session = aiohttp.ClientSession(
                headers={
                    "Authorization": f"Bot {self.bot_token}",
                    "User-Agent": "DiscordBot (https://google.com, 1)"
                },
            )
            
            await self.session.__aenter__()
        
        async with self.session.post(f"{self.endpoint_url}{path}", data=data) as response:
            return await response.json()
    
    async def send_message(self, channel_id: int, text: str):
        return await self.request(
            f"/channels/{channel_id}/messages",
            {"content": text}
        )
