import pytest
from shippingboapy.models.order_dispatch import OrderDispatch

@pytest.mark.asyncio
async def test_get_order_dispatch(mock_client):
    order_dispatch_id = 123
    order_dispatch = await mock_client.order_dispatches.get(order_dispatch_id)
    assert order_dispatch is not None
    assert isinstance(order_dispatch, OrderDispatch)