from __future__ import annotations
from typing import TYPE_CHECKING, List
from shippingboapy.models.product_stock_variation import ProductStockVariation
from shippingboapy.models.filter import ProductVariationStockFilter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client


class ProductVariationStockResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list(self,
                   search: List[tuple[str,str,str]] = None) -> list[ProductStockVariation]:
        """
        Retrieve the stock variations for a specific product.

        Args:
            product_id (int): The unique identifier of the product for which to retrieve stock variations.
        """

        params = []
        
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                filter_obj = ProductVariationStockFilter(field=item[0], operator=Operator(item[1]), value=item[2])
                key = f"search{filter_obj.to_params()}"
                
                if isinstance(item[2], list):
                    for value in item[2]:
                        params.append((key, str(value)))
                else:
                    params.append((key, str(item[2])))
        
        data = await self.client._request("GET", "/product_stock_variations", params=params)
        if data is None:
            return []
        if isinstance(data, dict) and "product_stock_variations" in data:
            data = data.get("product_stock_variations", [])
        
        return [ProductStockVariation.model_validate(item) for item in data]
        
        