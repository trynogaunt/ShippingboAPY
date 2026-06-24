import pytest
from shippingboapy.models.shipment_pallet import Pallet

@pytest.mark.asyncio
async def test_get_shipment_pallet(mock_client):
    # Replace with a valid pallet ID for testing
    pallet_id = 1
    pallet = await mock_client.shipment_pallets.get(pallet_id)
    
    assert isinstance(pallet, Pallet)

@pytest.mark.asyncio
async def test_list_shipment_pallets(mock_client):
    pallets = await mock_client.shipment_pallets.list()
    
    assert isinstance(pallets, list)
    for pallet in pallets:
        assert isinstance(pallet, Pallet)