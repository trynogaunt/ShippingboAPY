from __future__ import annotations
from shippingboapy.exceptions import ValueError
from shippingboapy.models.filter import Filter, Operator
from typing import TYPE_CHECKING, List
from shippingboapy.models.reseller_product import ResellerProduct
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ResellerProductResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, reseller_id: int) -> ResellerProduct:
        """
        Get a specific reseller product.

        Args:
            reseller_id (int): The unique identifier of the reseller.

        Returns:
            ResellerProduct: A ResellerProduct object representing the details of the specified reseller product.
        """


        data = await self.client._request("GET", f"reseller_products/{reseller_id}")

        if data is None:
            raise ValueError(f"Reseller product with ID {reseller_id} not found.")

        if isinstance(data, dict) and "reseller_product" in data:
            data = data["reseller_product"]
        
        return ResellerProduct.model_validate(data)
    
    async def list(self, 
                   search: List[tuple[str, str, str]]) -> list[ResellerProduct]:
        """
        Get the list of reseller products for a specific reseller.

        Args:
            search (List[tuple[str, str, str]]): A list of tuples representing the search filters.

        Returns:
            list[ResellerProduct]: A list of ResellerProduct objects representing the details of the reseller's products.
        """
        params = {}

        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError("Each search filter must be a tuple of (field, operator, value).")

                filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
                key = f"search{filter_obj.to_params()}"

                if isinstance(item[2], list):
                    for value in item[2]:
                        params[str(key)] = value
                else:
                    params[str(key)] = item[2]
        
        if key := "search[product_id__eq]" not in params:
            raise ValueError("The search filter must include a 'product_id' filter.")
        
        data = await self.client._request("GET", "reseller_products", params=params)

        if data is None:
            return []
        
        if isinstance(data, dict) and "reseller_products" in data:
            data = data["reseller_products"]
        
        return [ResellerProduct.model_validate(reseller_product) for reseller_product in data]
    
    async def create(self, reseller_product_create: ResellerProduct) -> ResellerProduct:
        """
        Create a new reseller product.

        Args:
            reseller_product_create (ResellerProduct): The reseller product creation object containing the details of the reseller product to be created.

        Returns:
            ResellerProduct: The newly created ResellerProduct object.
        """
        
        data = await self.client._request("POST", "reseller_products", json=reseller_product_create.model_dump(by_alias=True))

        if data is None:
            raise ValueError("Failed to create reseller product.")

        if isinstance(data, dict) and "reseller_product" in data:
            data = data["reseller_product"]
        
        return ResellerProduct.model_validate(data)
    
    async def update(self, reseller_id: int, reseller_product_update: ResellerProduct) -> ResellerProduct:
        """
        Update an existing reseller product.

        Args:
            reseller_id (int): The unique identifier of the reseller product to be updated.
            reseller_product_update (ResellerProduct): The reseller product update object containing the updated details of the reseller product.

        Returns:
            ResellerProduct: The updated ResellerProduct object.
        """
        
        data = await self.client._request("PATCH", f"reseller_products/{reseller_id}", json=reseller_product_update.model_dump(by_alias=True))

        if data is None:
            raise ValueError(f"Failed to update reseller product with ID {reseller_id}.")

        if isinstance(data, dict) and "reseller_product" in data:
            data = data["reseller_product"]
        
        return ResellerProduct.model_validate(data)