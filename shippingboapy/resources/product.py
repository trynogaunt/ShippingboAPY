from __future__ import annotations
from typing import TYPE_CHECKING, Literal
from shippingboapy.models.product import Product
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ProductRessource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list(self, 
                   is_pack: bool = False,
                   limit: int = 0,
                   offset: int = 0,
                   search: dict[str, str] | None = None,
                   sort: dict[Literal['id', 'updated_at'], str | int] | None = None,
                   **kwargs) -> list[Product]:
        """
        Get the list of products in the Shippingbo account.

        Args:
            is_pack (bool): Filter products by pack status.

        Returns:
            list[Product]: A list of Product objects representing the products in the Shippingbo account.
        """
        
        params = {}
        if is_pack:
            params["is_pack"] = is_pack
        
        params["limit"] = limit
        params["offset"] = offset
        
        if search:
            for key, value in search.items():
                if key == "updated_at":
                    params[f"search[{key}][]"] = value
                else:
                    params[f"search[{key}]"] = value
        
        if sort:
            for key, value in sort.items():
                params[f"sort[{key}]"] = value
        
        
        data = await self.client._request("GET", "products", params=params)
        return [Product(**item) for item in data.get("products", [])]
    
    async def get(self, product_id: int, **kwargs) -> Product:
        """
        Get the details of a specific product by its ID.

        Args:
            product_id (int): The unique identifier of the product to retrieve.

        Returns:
            Product: A Product object representing the details of the specified product.
        """
        data = await self.client._request("GET", f"/products/{product_id}", **kwargs)
        return Product(**data)