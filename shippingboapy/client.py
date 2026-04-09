import httpx
from config import ShippingBoConfig
from auth import TokenData

class Client:
    def __init__(self, access_token: str, 
                 refresh_token: str,
                 app_id: str = None,
                 api_version: str = None,
                 client_id: str = None,
                 client_secret: str = None,
                 ):
        self.config = ShippingBoConfig(
            app_id=app_id,
            api_version=api_version,
            client_id=client_id,
            client_secret=client_secret
        )
        self.token: TokenData | None = TokenData(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type= "Bearer",
            expires_in=3600,
            scope="",
            created_at = None
        )
        self.session = httpx.AsyncClient(timeout=self.config.timeout)

    def set_config(self, timeout: int = None, max_retries: int = None, retry_backoff_factor: float = None, redirect_uri: str = None, auth_url: str = None, api_url: str = None):
        if timeout is not None:
            self.config.timeout = timeout
            self.session.timeout = timeout
        if max_retries is not None:
            self.config.max_retries = max_retries
        if retry_backoff_factor is not None:
            self.config.retry_backoff_factor = retry_backoff_factor
        if redirect_uri is not None:
            self.config.redirect_uri = redirect_uri
        if auth_url is not None:
            self.config.auth_url = auth_url
        if api_url is not None:
            self.config.api_url = api_url
            
    async def close(self):
        await self.session.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self,  *args):
        await self.close()

