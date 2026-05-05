import pytest
from shippingboapy.models.order_item_product_mapping import OrderItemProductMapping, OrderItemProductMappingCreate

@pytest.mark.asyncio
async def test_create_order_item_product_mapping(mock_client):
    order_item_product_mapping_create = OrderItemProductMappingCreate(
        matched_quantity=10,
        order_item_field="name",
        order_item_value="Test Item",
        product_field="sku",
        product_value="TEST-SKU-001"
    )
    order_item_product_mapping = await mock_client.order_item_product_mappings.create(order_item_product_mapping_create)
    assert order_item_product_mapping is not None
    assert isinstance(order_item_product_mapping, OrderItemProductMapping)

@pytest.mark.asyncio
async def test_get_order_item_product_mapping(mock_client):
    order_item_product_mapping_id = 123
    order_item_product_mapping = await mock_client.order_item_product_mappings.get(order_item_product_mapping_id)
    assert order_item_product_mapping is not None
    assert isinstance(order_item_product_mapping, OrderItemProductMapping)

@pytest.mark.asyncio
async def test_list_order_item_product_mappings(mock_client):
    order_item_product_mappings = await mock_client.order_item_product_mappings.list()
    assert isinstance(order_item_product_mappings, list)
    for mapping in order_item_product_mappings:
        assert isinstance(mapping, OrderItemProductMapping)

@pytest.mark.asyncio
async def test_delete_order_item_product_mapping(mock_client):
    order_item_product_mapping_id = 123
    result = await mock_client.order_item_product_mappings.delete(order_item_product_mapping_id)
    assert result is True