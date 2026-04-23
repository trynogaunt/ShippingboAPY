import pytest
from shippingboapy.models.address_label_config import AddressLabelConfig

@pytest.mark.asyncio
async def test_list_address_label_configs(client):
    address_label_configs = await client.address_label_configs.list()
    
    assert isinstance(address_label_configs, list)
    for config in address_label_configs:
        assert isinstance(config, AddressLabelConfig)