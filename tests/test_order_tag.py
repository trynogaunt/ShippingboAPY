import pytest
from shippingboapy.models.tag import OrderTag, OrderTagCreate

@pytest.mark.asyncio
async def test_create_order_tag(mock_client):

    order_tag_create = OrderTagCreate(
        order_id=123,
        value="Test Tag"
    )
    
    order_tag = await mock_client.order_tags.create(order_tag_create, headers={"Prefer": "code=200, dynamic=true"})
    
    assert order_tag is not None
    assert isinstance(order_tag, OrderTag)
    assert order_tag.id is not None
    assert isinstance(order_tag.id, int)
    
@pytest.mark.asyncio
async def test_get_order_tag(mock_client):

    order_tag = await mock_client.order_tags.get(order_tag_id=123, headers={"Prefer": "code=200, dynamic=true"})
    
    assert order_tag is not None
    assert isinstance(order_tag, OrderTag)
    assert order_tag.id is not None
    assert isinstance(order_tag.id, int)
    assert order_tag.order_id is not None
    assert isinstance(order_tag.order_id, int)
    assert order_tag.value is not None
    assert isinstance(order_tag.value, str)

@pytest.mark.asyncio
async def test_delete_order_tag(mock_client):

    result = await mock_client.order_tags.delete(order_tag_id=123, headers={"Prefer": "code=200, dynamic=true"})
    
    assert result is True or result is False
    assert isinstance(result, bool)