import pytest
import time
from unittest.mock import patch
from shippingboapy.config import ShippingBoConfig
from shippingboapy.auth import TokenData
from shippingboapy.client import Client
    
@pytest.fixture
def mock_config():
    with patch.dict("os.environ", {
        "APP_ID": "447",
        "API_VERSION": "1",
        "CLIENT_ID": "jZgZZTwwdJXzBTN8btkssqO6UrbZriha5DX0rxdqj14",
        "CLIENT_SECRET": "vqVUUuChI7UNZ-z0DKdYILr0XY0QbOslD1clDRlBmoAt",
        "AUTH_URL": "https://stoplight.io/mocks/shippingbo/api/256683485/oauth/token",
        "API_URL": "https://stoplight.io/mocks/shippingbo/api/757519129",
        "REDIRECT_URI": "urn:ietf:wg:oauth:2.0:oob",
        "MAX_RETRIES": "3",
        "RETRY_BACKOFF_FACTOR": "0.5",
        "TIMEOUT": "30"
    }):
        yield ShippingBoConfig()

@pytest.fixture
def mock_token_data():
    return TokenData(
        access_token="jZgZZTwwdJXzBTN8btkssqO6UrbZriha5DX0rxdqj14",
        token_type="Bearer",
        expires_in=3600,
        refresh_token="vqVUUuChI7UNZ-z0DKdYILr0XY0QbOslD1clDRlBmoA",
        scope="",
        created_at=int(time.time())
    )

@pytest.fixture
def mock_client(mock_config, mock_token_data):
    client = Client(
        access_token=mock_token_data.access_token,
        refresh_token=mock_token_data.refresh_token,
        app_id=mock_config.app_id,
        api_version=mock_config.api_version,
        client_id=mock_config.client_id,
        client_secret=mock_config.client_secret
    )
    yield client
