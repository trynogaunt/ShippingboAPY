from shippingboapy.client import Client
from shippingboapy.auth import TokenData
import pytest

@pytest.mark.asyncio
async def test_client_from_auth_code(mock_config):
    headers = {
        "Prefer": "code=200, dynamic=true",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    client = await Client.from_auth_code(
        auth_code="fd0847dbb559752d932dd3c1ac34ff98d27b11fe2fea5a864f44740cd7919ad0",
        app_id=mock_config.app_id,
        api_version=mock_config.api_version,
        client_id=mock_config.client_id,
        client_secret=mock_config.client_secret,
        redirect_uri=mock_config.redirect_uri,
        headers=headers
    )

    try:
        assert client is not None
        assert isinstance(client, Client)
        
        assert client.token is not None
        assert isinstance(client.token, TokenData)
        
        assert client.token.access_token is not None
        assert isinstance(client.token.access_token, str)
        
        assert client.token.refresh_token is not None
        assert isinstance(client.token.refresh_token, str)
        
        assert client.token.token_type is not None
        assert isinstance(client.token.token_type, str) 
        
        assert client.token.expires_in is not None
        assert isinstance(client.token.expires_in, int)
        
        assert client.token.scope is not None
        assert isinstance(client.token.scope, str)
        
        assert client.token.created_at is not None
        assert isinstance(client.token.created_at, int)
        
        assert client.config.app_id == mock_config.app_id
        assert client.config.api_version == mock_config.api_version
        assert client.config.client_id == mock_config.client_id
        assert client.config.client_secret == mock_config.client_secret
        assert client.config.redirect_uri == mock_config.redirect_uri
        assert client.config.auth_url == mock_config.auth_url
        assert client.config.api_url == mock_config.api_url
        assert client.session is not None
    finally:
        await client.session.aclose()

async def test_client_from_token(mock_config, mock_token_data):
    client = Client(
        access_token=mock_token_data.access_token,
        refresh_token=mock_token_data.refresh_token,
        app_id=mock_config.app_id,
        api_version=mock_config.api_version,
        client_id=mock_config.client_id,
        client_secret=mock_config.client_secret
    )

    try:
        assert client is not None
        assert isinstance(client, Client)
        
        assert client.token is not None
        assert isinstance(client.token, TokenData)
        
        assert client.token.access_token == mock_token_data.access_token
        assert client.token.refresh_token == mock_token_data.refresh_token
        assert client.token.token_type == "Bearer"
        assert client.token.expires_in == 3600
        assert client.token.scope == ""
        
        assert client.config.app_id == mock_config.app_id
        assert client.config.api_version == mock_config.api_version
        assert client.config.client_id == mock_config.client_id
        assert client.config.client_secret == mock_config.client_secret
    finally:
        await client.session.aclose()