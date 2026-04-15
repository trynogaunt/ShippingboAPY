import pytest
from shippingboapy.models.order import Order, OrderSummary, OrderCreate, OrderItemCreate

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
        
@pytest.mark.asyncio
async def test_create_order(mock_client):
    order_create = OrderCreate(
        origin_ref="test_order_001",
        shipping_address_id=123,
        origin="test",
        origin_created_at="2023-01-01T12:00:00Z",
        source="Test_source",
        source_ref="test_source_ref",
        order_items_attributes=[
            OrderItemCreate(        
                price_tax_included_cents = 1000,
                price_tax_included_currency = "EUR",
                product_ean="1234567890123",
                product_ref=None,
                product_source=None,
                product_source_ref=None,
                quantity=None,
                source=None,
                source_ref=None,
                tax_cents=None,
                tax_currency=None,
                title=None,
                computed_prices=None,
                additional_content= {}
            )
            ]
       
    )
    
    order = await mock_client.orders.create(order_create, headers={"Prefer": "code=200, dynamic=true"})
    assert order is not None
    assert isinstance(order, Order)
    assert order.id is not None
    assert isinstance(order.id, int)