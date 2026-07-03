from dataclasses import dataclass
from shippingboapy.config import ShippingBoConfig
import httpx
import time
from shippingboapy.exceptions import BadRequestError, UnauthorizedError, AuthenticationError, TokenRefreshError
from typing import Callable, Any, Awaitable
import inspect

@dataclass
class TokenData:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    created_at: int | None

async def get_remaining_token_lifetime(token_data: TokenData) -> int:
    """Time remaining before the token expires. Returns -1 if the token is unknown or expired."""
    if token_data.created_at is None or token_data.expires_in is None:
        return -1  # inconnu, à traiter comme expiré
    now = int(time.time())
    return (token_data.created_at + token_data.expires_in) - now
    
async def is_token_expired(token_data: TokenData, session: httpx.AsyncClient) -> bool:
    """Check if the token has expired, en fetchant les métadonnées si besoin."""
    
    if token_data.created_at is None or token_data.expires_in is None:
        token_info = await get_token_information(token_data.access_token, session)
        if token_info:
            scopes = token_info.get("scopes", [])
            token_data.scope = " ".join(scopes) if isinstance(scopes, list) else str(scopes)
            token_data.expires_in = int(token_info.get("expires_in_seconds", 0))
            token_data.created_at = int(time.time())
        else:
            return True

    return await get_remaining_token_lifetime(token_data) <= 0

async def get_token(auth_code: str, session: httpx.AsyncClient, config: ShippingBoConfig, headers: dict[str, Any] | None = None) -> TokenData | None:
    """
    Get a valid access token, refreshing it if necessary.
    Args:
        auth_code (str): The authorization code to use for obtaining the access token.
        session (httpx.AsyncClient): The HTTP client session to use for making the request.
        config (ShippingBoConfig): The configuration object containing necessary parameters.
        headers (dict[str, Any] | None): Optional headers to include in the request.
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
            raise BadRequestError(status_code=response.status_code, message=f"Bad request: {response.text}")
        elif response.status_code == 401:
            raise UnauthorizedError(status_code=response.status_code, message=f"Unauthorized access: {response.text}")
        else:
            raise AuthenticationError(f"Failed to get token: {response.status_code} - {response.text}")
        
async def refresh_token(refresh_token: str, 
                        session: httpx.AsyncClient, 
                        config: ShippingBoConfig, 
                        headers: dict[str, Any] | None = None,
                        on_refresh: Callable[[TokenData], Awaitable[None]] | None = None) -> TokenData: 
    """
    Refresh the access token using the refresh token.
    Args:
        refresh_token (str): The refresh token to use for refreshing the access token.
        session (httpx.AsyncClient): The HTTP client session to use for making the request.
        config (ShippingBoConfig): The configuration object containing necessary parameters.
        headers (dict[str, Any] | None): Optional headers to include in the request.
        on_refresh (Callable[[TokenData], Awaitable[None]] | None): Optional callback function to be called after a successful token refresh. The function should accept a TokenData object as its argument.
    Returns:
        TokenData: The new token data if the refresh is successful.
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
        if on_refresh is not None:
            result = on_refresh(TokenData(
                access_token=token_data['access_token'],
                token_type=token_data['token_type'],
                expires_in=token_data['expires_in'],
                refresh_token=token_data['refresh_token'],
                scope=token_data['scope'],
                created_at=int(time.time())
            ))
            if inspect.isawaitable(result):
                await result
            
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
    
async def get_token_information(access_token: str, session: httpx.AsyncClient) -> dict[str, Any]:
    """
    Get information about the access token.
    Args:
        access_token (str): The access token to get information about.
        session (httpx.AsyncClient): The HTTP client session to use for making the request.
        config (ShippingBoConfig): The configuration object containing necessary parameters.
        headers (dict[str, Any] | None): Optional headers to include in the request.
    Returns:
        dict[str, Any]: The token information if the request is successful.
    Raises:
        BadRequestError: If the request is malformed or contains invalid parameters.
        UnauthorizedError: If the request is unauthorized.
        AuthenticationError: If there is an error obtaining the token information.
    """
    auth_headers = {}
    auth_headers['Authorization'] = f'Bearer {access_token}'
    
    response = await session.get(url="https://oauth.shippingbo.com/oauth/token/info", headers=auth_headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        if response.status_code == 400:
            raise BadRequestError(status_code=response.status_code, message=f"Bad request: {response.text}")
        elif response.status_code == 401:
            raise UnauthorizedError(status_code=response.status_code, message=f"Unauthorized access: {response.text}")
        else:
            raise AuthenticationError(f"Failed to get token information: {response.status_code} - {response.text}")