from unittest.mock import AsyncMock
from shippingboapy.auth import refresh_token
import pytest
import httpx


@pytest.mark.asyncio
async def test_refresh_token(mock_config):
    async with httpx.AsyncClient() as mock_session:
        headers = {
            "Prefer": "code=200, dynamic=true",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        mock_response = await refresh_token(refresh_token="test_refresh_token", session=mock_session, config=mock_config, headers=headers)
        assert mock_response is not None
        assert mock_response.access_token is not None
        assert mock_response.token_type is not None
        assert mock_response.expires_in is not None
        assert mock_response.refresh_token is not None
        assert mock_response.scope is not None
        assert mock_response.created_at is not None