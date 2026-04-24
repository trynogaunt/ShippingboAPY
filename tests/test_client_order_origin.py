import pytest
from shippingboapy.models.client_order_origin import ClientOrderOrigin, ClientOrderOriginCreate

@pytest.mark.asyncio
async def test_create_client_order_origin(mock_client):
    client_order_origin_create = ClientOrderOriginCreate(
        display_name="Test Origin",
        name="Test Origin Name"
    )
    
    client_order_origin = await mock_client.client_order_origin.create(client_order_origin_create)
    
    assert client_order_origin is not None
    assert isinstance(client_order_origin, ClientOrderOrigin)
    assert isinstance(client_order_origin.id, int)
    assert isinstance(client_order_origin.created_at, str)
    assert isinstance(client_order_origin.updated_at, str)
    assert isinstance(client_order_origin.display_name, str)
    assert isinstance(client_order_origin.name, str)