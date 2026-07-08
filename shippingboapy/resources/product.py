from __future__ import annotations
from typing import Optional, cast, Literal
from shippingboapy.models.filter import Filter
from shippingboapy.resources.base_resource import Gettable, Updatable, Creatable, Deletable
from shippingboapy.models.product import Product, ProductCreate, ProductStocksInformations

class ProductResource(Gettable[Product], Updatable[Product, Product], Creatable[ProductCreate, Product], Deletable):
    _path = "products"
    _model = Product
 
    async def list(self, limit: str = 50, offset: str = 0, is_pack: str = None, search: Optional[list[Filter]] = None) -> list[Product]:
        """
        List all products with optional filtering.

        Args:
            search (list[Filter], optional): A list of Filter objects representing the search criteria.

        Returns:
            list[Product]: A list of products that match the search criteria.
        """

        params = {"limit": limit, "offset": offset, "is_pack": is_pack}
        
        if search is not None:
            for filter_obj in search:
                key = f"search{filter_obj.to_params()}"
                params[key] = str(filter_obj.value)

        response = await self.client._request("GET", self._path, params=params)
        
        if response is None:
            return []
        
        response = self._unwrap(response)



        return [cast(Product, self._model.model_validate(item)) for item in response]
    
    async def get_product_stocks(self, product_id: int | str) -> dict:
        """
        Get the stock information for a specific product.

        Args:
            product_id (int | str): The ID of the product.

        Returns:
            dict: The stock information for the specified product.
        """
        response = await self.client._request("GET", f"{self._path}/product_stocks/{product_id}")

        if response is None:
            return {}

        response = self._unwrap(response)

        return cast(ProductStocksInformations, self._model.model_validate(response))
    
    async def update_by_key(self, key: Literal["user_ref", "ean13"], value: str, physical_stock: int = None, stock: int = None) -> Product:
        """
        Update a product by its key.

        Args:
            key (Literal["user_ref", "ean13"]): The key of the product to update.
            value (str): The value of the key to identify the product.

        Returns:
            Product: The updated product.
        """
        response = await self.client._request("PATCH", f"{self._path}/{key}/{value}")

        if response is None:
            raise ValueError(f"Product with key {key} and value {value} not found or could not be updated.")
        
        response = self._unwrap(response)

        return cast(Product, self._model.model_validate(response))