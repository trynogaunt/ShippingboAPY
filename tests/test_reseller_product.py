import pytest
from shippingboapy.models.reseller_product import ResellerProduct

@pytest.mark.asyncio
async def test_list_reseller_products(mock_client):
    search_filters = [("product_id", "eq", 1)]
    reseller_products = await mock_client.reseller_product.list(search=search_filters)
    assert isinstance(reseller_products, list)
    for reseller_product in reseller_products:
        assert isinstance(reseller_product, ResellerProduct)
        assert hasattr(reseller_product, "id")
        assert hasattr(reseller_product, "reseller_id")
        assert hasattr(reseller_product, "product_id")
        assert hasattr(reseller_product, "reseller_ref")
        assert hasattr(reseller_product, "active")
        assert hasattr(reseller_product, "available_stock")
        assert hasattr(reseller_product, "physical_stock")

@pytest.mark.asyncio
async def test_get_reseller_product(mock_client):
    # Assuming there's a reseller product with ID 1 for testing purposes
    reseller_product_id = 1
    reseller_product = await mock_client.reseller_product.get(reseller_product_id)
    assert isinstance(reseller_product, ResellerProduct)
    assert hasattr(reseller_product, "id")
    assert hasattr(reseller_product, "reseller_id")
    assert hasattr(reseller_product, "product_id")
    assert hasattr(reseller_product, "reseller_ref")
    assert hasattr(reseller_product, "active")
    assert hasattr(reseller_product, "available_stock")
    assert hasattr(reseller_product, "physical_stock")

@pytest.mark.asyncio
async def test_create_reseller_product(mock_client):
    new_reseller_product = ResellerProduct(
        id=123,
        reseller_id=1,
        product_id=456,
        reseller_ref="REF123",
        active=True,
        available_stock=100,
        physical_stock=50
    )
    created_reseller_product = await mock_client.reseller_product.create(new_reseller_product)
    assert isinstance(created_reseller_product, ResellerProduct)

@pytest.mark.asyncio
async def test_update_reseller_product(mock_client):
    reseller_product_id = 123  # Assuming this ID exists for testing purposes
    updated_reseller_product = ResellerProduct(
        id=reseller_product_id,
        reseller_id=1,
        product_id=456,
        reseller_ref="REF123_UPDATED",
        active=False,
        available_stock=80,
        physical_stock=40
    )
    updated_product = await mock_client.reseller_product.update(reseller_product_id, updated_reseller_product)
    assert isinstance(updated_product, ResellerProduct)