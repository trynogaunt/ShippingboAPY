import pytest
from shippingboapy.models.order_event import OrderEvent, OrderEventCreate

@pytest.mark.asyncio
async def test_get_order_event(mock_client):
    order_event_id = 123
    order_event = await mock_client.order_events.get(order_event_id)
    assert order_event is not None
    assert isinstance(order_event, OrderEvent)

@pytest.mark.asyncio
async def test_create_order_event(mock_client):
    order_event_create = OrderEventCreate(
        order_id=123,
        title="Order Shipped",
        message="Order status changed to 'shipped'.",
        display_ps_enabled=True,
        level="info"
    )
    order_event = await mock_client.order_events.create(order_event_create)
    assert order_event is not None
    assert isinstance(order_event, OrderEvent)