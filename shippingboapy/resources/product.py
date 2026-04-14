from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING, Literal
from shippingboapy.models.product import Product, ProductSummary, ProductCreate
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
            limit (int): The maximum number of products to return.
            offset (int): The number of products to skip before starting to collect the result set.
            search (dict[str, str]): A dictionary of search parameters to filter the products.
            sort (dict[Literal['id', 'updated_at'], str | int]): A dictionary specifying the sorting order of the results. The keys can be 'id' or 'updated_at', and the values can be 'asc' for ascending or null for descending.

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
                if key == "id" and not isinstance(value, int):
                    try:
                        value = int(value)
                    except ValueError:
                        raise ValueError(f"Invalid value for 'id' in sort: {value}. Expected an integer or a string that can be converted to an integer.")
                else:
                    value = str(value)
                    
                params[f"sort[{key}]"] = value
        
        data = await self.client._request("GET", "products", params=params, **kwargs)
       
       
        if data is None:
            return []
        
        return [ProductSummary(**item) for item in data.get("products", [])]
    
    async def get(self, product_id: int, **kwargs) -> Product:
        """
        Get the details of a specific product by its ID.

        Args:
            product_id (int): The unique identifier of the product to retrieve.

        Returns:
            Product: A Product object representing the details of the specified product.
        """
        
        data = await self.client._request("GET", f"/products/{product_id}", **kwargs)
        
        if data is None:
            return None
        
        return Product(**data)
    
    async def create(self, product_create: ProductCreate, **kwargs) -> Product:
        """
        Create a new product in the Shippingbo account.

        Args:
            product_create (ProductCreate): The product creation data.

        Returns:
            Product: A Product object representing the details of the newly created product.
        """
        
        data = await self.client._request("POST", "products", json=product_create.model_dump(exclude_none=True), **kwargs)
        
        if data is None:
            return None
        
        return Product(**data)
    
    async def delete(self, product_id: int, **kwargs) -> bool:
        """
        Delete a specific product by its ID.

        Args:
            product_id (int): The unique identifier of the product to delete.

        Returns:
            bool: True if the product was successfully deleted, False otherwise.
        """
        
        response = await self.client._request("DELETE", f"/products/{product_id}", **kwargs)
        if response is None:
            return False
        return True