import pytest
from shippingboapy.models.client_order_source import ClientOrderSource, ClientOrderSourceCreate

@pytest.mark.asyncio
async def test_create_client_order_source(mock_client):
    client_order_source_create = ClientOrderSourceCreate(
        display_name="Test Source",
        name="Test Source Name"
    )
    
    client_order_source = await mock_client.client_order_source.create(client_order_source_create)
    
    assert client_order_source is not None
    assert isinstance(client_order_source, ClientOrderSource)
    assert isinstance(client_order_source.id, int)
    assert isinstance(client_order_source.created_at, str)
    assert isinstance(client_order_source.updated_at, str)
    assert isinstance(client_order_source.display_name, str)
    assert isinstance(client_order_source.name, str)