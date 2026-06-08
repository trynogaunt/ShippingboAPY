from pydantic_settings import BaseSettings, SettingsConfigDict

class ShippingBoConfig(BaseSettings):
    app_id: str
    api_version: str
    client_secret: str
    client_id: str
    auth_url: str = "https://oauth.shippingbo.com/oauth/token"
    api_url: str = "https://app.shippingbo.com"
    staging_api_url: str = "https://oms-staging.shippingbo.com"
    redirect_uri: str = "urn:ietf:wg:oauth:2.0:oob"
    max_retries: int = 3
    retry_backoff_factor: float = 0.5
    timeout : int = 30
