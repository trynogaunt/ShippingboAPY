import pytest
from shippingboapy.models.order import Order

@pytest.mark.asyncio
async def test_get_order(mock_client):
    order = await mock_client.orders.get(order_id=123, headers={"Prefer": "code=200, dynamic=false"})
    assert order is not None
    assert isinstance(order, Order)
    assert order.id is not None
    assert isinstance(order.id, int)