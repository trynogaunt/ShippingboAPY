import pytest
from shippingboapy.models.address_label import AddressLabel

@pytest.mark.asyncio
async def test_get_address_label(mock_client):
    address_label_id = 123
    address_label = await mock_client.address_labels.get(address_label_id)
    assert address_label is not None
    assert isinstance(address_label, AddressLabel)

@pytest.mark.asyncio
async def test_get_address_label_file(mock_client):
    address_label_id = 123
    data = await mock_client.address_labels.get_file(address_label_id, headers={"Prefer": "code=200, dynamic=true"})
    assert isinstance(data, bytes)