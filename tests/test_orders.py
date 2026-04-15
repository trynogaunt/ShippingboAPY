import pytest
from shippingboapy.models.order import Order, OrderSummary

@pytest.mark.asyncio
async def test_get_order(mock_client):
    order = await mock_client.orders.get(order_id=123, headers={"Prefer": "code=200, dynamic=false"})
    assert order is not None
    assert isinstance(order, Order)
    assert order.id is not None
    assert isinstance(order.id, int)

@pytest.mark.asyncio
async def test_list_orders(mock_client):
    orders = await mock_client.orders.list(limit=10, offset=0, search=[('origin_ref', 'eq', '123'), ('shipped_at', 'eq', '2023-01-01')], headers={"Prefer": "code=200, dynamic=false"})
    assert orders is not None
    assert isinstance(orders, list)
    assert len(orders) > 0
    for order in orders:
        assert isinstance(order, OrderSummary)
        assert order.id is not None
        assert isinstance(order.id, int)