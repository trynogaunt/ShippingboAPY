import pytest
from shippingboapy.models.address_label_config import AddressLabelConfig, AddressLabelConfigDetails

@pytest.mark.asyncio
async def test_list_address_label_configs(mock_client):
    address_label_configs = await mock_client.address_label_configs.list()
    
    assert isinstance(address_label_configs, list)
    for config in address_label_configs:
        assert isinstance(config, AddressLabelConfig)

@pytest.mark.asyncio
async def test_get_address_label_config(mock_client):
    address_label_config = await mock_client.address_label_configs.get(1)

    assert address_label_config is not None
    assert isinstance(address_label_config, AddressLabelConfigDetails)