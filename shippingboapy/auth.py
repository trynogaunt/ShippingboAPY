from dataclasses import dataclass
from shippingboapy.config import ShippingBoConfig
import httpx
import time
from shippingboapy.exceptions import BadRequestError, UnauthorizedError, AuthenticationError, TokenRefreshError

@dataclass
class TokenData:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    created_at: int | None
    
def is_token_expired(token_data: TokenData) -> bool:
    """Check if the token has expired."""
    if token_data.created_at is None:
        return True
    current_time = int(time.time())
    return current_time >= token_data.created_at + token_data.expires_in

async def get_token(auth_code: str, session: httpx.AsyncClient, config: ShippingBoConfig, headers: dict | None = None) -> TokenData | None:
    """
    Get a valid access token, refreshing it if necessary.
    Args:
        auth_code (str): The authorization code to use for obtaining the access token.
        session (httpx.AsyncClient): The HTTP client session to use for making the request.
        config (ShippingBoConfig): The configuration object containing necessary parameters.
        headers (dict | None): Optional headers to include in the request.
    Returns:
        TokenData | None: The token data if the request is successful, otherwise None.
    Raises:
        BadRequestError: If the request is malformed or contains invalid parameters.
        UnauthorizedError: If the request is unauthorized.
        AuthenticationError: If there is an error obtaining the token.
    """
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': config.client_id,
        'client_secret' : config.client_secret,
        'redirect_uri': config.redirect_uri
    }
    
    response = await session.post(config.auth_url, json=payload, headers=headers)

    if response.status_code == 200:
        token_data = response.json()
    
        token = TokenData(
            access_token=token_data['access_token'],
            token_type=token_data['token_type'],
            expires_in=token_data['expires_in'],
            refresh_token=token_data['refresh_token'],
            scope=token_data['scope'],
            created_at= token_data.get('created_at', int(time.time()))
        )
    
        return token
    else:
        if response.status_code == 400:
            raise BadRequestError(f"Bad request: {response.status_code} - {response.text}")
        elif response.status_code == 401:
            raise UnauthorizedError(f"Unauthorized access: {response.status_code} - {response.text}")
        else:
            raise AuthenticationError(f"Failed to get token: {response.status_code} - {response.text}")
        
async def refresh_token(refresh_token: str, 
                        session: httpx.AsyncClient, 
                        config: ShippingBoConfig, 
                        headers: dict | None = None) -> TokenData | None: 
    """
    Refresh the access token using the refresh token.
    Args:
        refresh_token (str): The refresh token to use for refreshing the access token.
        session (httpx.AsyncClient): The HTTP client session to use for making the request.
        config (ShippingBoConfig): The configuration object containing necessary parameters.
        headers (dict | None): Optional headers to include in the request.
    Returns:
        TokenData | None: The new token data if the refresh is successful, otherwise None.
    Raises:
        TokenRefreshError: If there is an error refreshing the token.
    """
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': config.client_id,
        'client_secret': config.client_secret,
        'redirect_uri': config.redirect_uri
    }
    
    response = await session.post(config.auth_url, json=payload, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        return TokenData(
            access_token=token_data['access_token'],
            token_type=token_data['token_type'],
            expires_in=token_data['expires_in'],
            refresh_token=token_data['refresh_token'],
            scope=token_data['scope'],
            created_at=int(time.time())
        )
    else:
        raise TokenRefreshError(f"Failed to refresh token: {response.status_code} - {response.text}")