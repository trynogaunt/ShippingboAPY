import pytest
from shippingboapy.models.product_stock_variation import ProductStockVariation

@pytest.mark.asyncio
async def test_list_product_variation_stock(mock_client):
    stock_variations = await mock_client.product_variation_stock.list()
    
    assert isinstance(stock_variations, list)
    for variation in stock_variations:
        assert isinstance(variation, ProductStockVariation)
        assert isinstance(variation.id, int)
        assert isinstance(variation.product_id, int)
        assert isinstance(variation.quantity, int)