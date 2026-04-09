from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.product import Product
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ProductRessource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list(self) -> list[Product]:
        """
        Get the list of products in the Shippingbo account.

        Returns:
            list[Product]: A list of Product objects representing the products in the Shippingbo account.
        """
        response = await self.client.session.get(f"{self.client.config.api_url}/products", headers={"Authorization": f"Bearer {self.client.token.access_token}"})
        if response.status_code == 200:
            products_data = response.json()
            return [Product(**product) for product in products_data]
        else:
            response.raise_for_status()