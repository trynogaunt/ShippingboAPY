import pytest
from shippingboapy.models.address_label_summaries import AddressLabelSummaries

@pytest.mark.asyncio
async def test_get_address_label_summaries(mock_client):
    address_label_summaries = await mock_client.address_label_summaries.list()
    assert address_label_summaries is not None
    assert isinstance(address_label_summaries, list)
    assert all(isinstance(item, AddressLabelSummaries) for item in address_label_summaries)