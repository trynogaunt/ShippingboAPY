import pytest
from shippingboapy.models.carrier import Carrier

@pytest.mark.asyncio
async def test_get_carrier(mock_client):
    carrier = await mock_client.carrier.list()
    
    assert carrier is not None
    assert isinstance(carrier, list)
    assert all(isinstance(item, Carrier) for item in carrier)