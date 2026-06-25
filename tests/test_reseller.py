import pytest
from shippingboapy.models.reseller import Reseller

@pytest.mark.asyncio
async def test_list_resellers(mock_client):
    resellers = await mock_client.reseller.list()
    assert isinstance(resellers, list)
    for reseller in resellers:
        assert isinstance(reseller, Reseller)
        assert hasattr(reseller, "id")
        assert hasattr(reseller, "name")

async def test_get_reseller(mock_client):
    # Assuming there's a reseller with ID 1 for testing purposes
    reseller_id = 1
    reseller = await mock_client.reseller.get(reseller_id)
    assert isinstance(reseller, Reseller)
    assert hasattr(reseller, "id")
    assert hasattr(reseller, "name")