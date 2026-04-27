import pytest
from shippingboapy.models.logistician_service_config import LogisticianServiceConfig

@pytest.mark.asyncio
async def test_get_logistician_service_config(mock_client):
    config_id = 123  
    service_config = await mock_client.logistician_service_configs.get(config_id)
    
    assert service_config is not None
    assert isinstance(service_config, LogisticianServiceConfig)