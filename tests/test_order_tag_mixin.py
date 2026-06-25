import pytest

@pytest.mark.asyncio
async def test_order_tag_resource_get(mock_client):
    from shippingboapy.models.order_tag import OrderTag

    # Mock the client and its _request method
    response = await mock_client.order_tags.get(1)

    assert isinstance(response, OrderTag)
    assert hasattr(response, "id")
    assert hasattr(response, "order_id")
    assert hasattr(response, "value")

