import pytest
from shippingboapy.models.product import Product, ProductSummary, ProductCreate, ProductStocksInformations

@pytest.mark.skip(reason="Spotlight mock API expect body for GET /products/{id} endpoint, which is not standard. Need to find a better solution for testing this endpoint.")
async def test_get_product(mock_client):
    product = await mock_client.products.get(product_id=123, headers={"Prefer": "code=200, dynamic=true"})
    assert product is not None
    assert isinstance(product, Product)
    assert product.id is not None
    assert isinstance(product.id, int)
    assert product.id == 123

@pytest.mark.asyncio
async def test_list_products(mock_client):
    products = await mock_client.products.list(limit=10, offset=0, headers={"Prefer": "code=200, dynamic=true"})
    assert products is not None
    assert isinstance(products, list)
    assert all(isinstance(product, ProductSummary) for product in products)
    
@pytest.mark.asyncio
async def test_create_product(mock_client):
    product_create = ProductCreate(
        title="Test Product",
        user_ref="TEST-REF-001",
        weight=500,
        width=200,
        length=300,
        height=100,
        product_additional_fields_to_add=[{"key": "color", "value": "red"}, {"key": "size", "value": "M"}],
        product_barcodes_attributes=[{"key": "ean13", "value": "1234567890123"}]
    )
    
    created_product = await mock_client.products.create(product_create, headers={"Prefer": "code=200, dynamic=true"})
    
    assert created_product is not None
    assert isinstance(created_product, Product)
    assert isinstance(created_product.title, str)
    assert isinstance(created_product.user_ref, str)
    assert isinstance(created_product.weight, int)
    assert isinstance(created_product.width, int)
    assert isinstance(created_product.length, int)
    assert isinstance(created_product.height, int)
    
@pytest.mark.asyncio
async def test_delete_product(mock_client):
    product_id = 123
    deletion = await mock_client.products.delete(product_id, headers={"Prefer": "code=200, dynamic=true"})
    assert deletion is True

@pytest.mark.skip(reason="Spotlight mock API expect body for PATCH /products/{id} endpoint, which is not standard. Need to find a better solution for testing this endpoint.")
@pytest.mark.asyncio
async def test_get_stocks_information(mock_client):
    product_id = 123
    stocks_info = await mock_client.products.get_stocks_information(product_id, headers={"Prefer": "code=200, dynamic=true"})
    assert stocks_info is not None
    assert isinstance(stocks_info, ProductStocksInformations)
    assert isinstance(stocks_info.available_stock, int)