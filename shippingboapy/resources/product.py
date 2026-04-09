from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.product import Product
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ProductRessource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list(self, **kwargs) -> list[Product]:
        """
        Get the list of products in the Shippingbo account.

        Returns:
            list[Product]: A list of Product objects representing the products in the Shippingbo account.
        """
        data = await self.client._request("GET", "products", **kwargs)
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