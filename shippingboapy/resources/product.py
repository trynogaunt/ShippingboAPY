from __future__ import annotations
from typing import Optional, cast
from shippingboapy.models.filter import Filter
from shippingboapy.resources.base_resource import Gettable, Updatable, Creatable, Deletable
from shippingboapy.models.product import Product, ProductCreate

class ProductResource(Gettable[Product], Updatable[Product, Product], Creatable[ProductCreate, Product], Deletable):
    _path = "products"
    _dict_headers = ["product"]
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

        print(f"List Products Response: {response}")  # Debugging line to print the response

        return [cast(Product, self._model.model_validate(item)) for item in response]