import httpx
from config import ShippingBoConfig
from auth import TokenData

class Client:
    def __init__(self, config: ShippingBoConfig):
        self.config = config
        self.token: TokenData | None = None
        self.session = httpx.AsyncClient(timeout=self.config.timeout)

    async def close(self):
        await self.session.aclose()
