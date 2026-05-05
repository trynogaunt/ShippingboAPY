from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from shippingboapy.models.filter import Filter, Operator
from shippingboapy.models.order_item_product_mapping import OrderItemProductMapping, OrderItemProductMappingCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client

class OrderItemProductMappingResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def create(self, order_item_product_mapping_create: OrderItemProductMappingCreate, **kwargs) -> OrderItemProductMapping:
        """
        Create a new order item product mapping.

        Args:
            order_item_product_mapping_create (OrderItemProductMappingCreate): An OrderItemProductMappingCreate object containing the details of the order item product mapping to create.
            
        Returns:
            OrderItemProductMapping: An OrderItemProductMapping object representing the newly created order item product mapping.
        """
        
        data = await self.client._request("POST", "/order_item_product_mappings", json=order_item_product_mapping_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        return OrderItemProductMapping.model_validate(data)
    
    async def get(self, order_item_product_mapping_id: int, **kwargs) -> OrderItemProductMapping:
        """
        Get the details of a specific order item product mapping by its ID.

        Args:
            order_item_product_mapping_id (int): The unique identifier of the order item product mapping to retrieve.

        Returns:
            OrderItemProductMapping: An OrderItemProductMapping object representing the details of the specified order item product mapping.
        """
        
        data = await self.client._request("GET", f"/order_item_product_mappings/{order_item_product_mapping_id}", **kwargs)
        
        if data is None:
            return None
        
        return OrderItemProductMapping.model_validate(data)
    
    async def list(self, search: Optional[List[tuple[str,str, str]]] = None, **kwargs) -> list[OrderItemProductMapping]:
        """List all order item product mappings.
        Returns:
            list[OrderItemProductMapping]: A list of OrderItemProductMapping objects representing all order item product mappings.
        """
        params = []
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError("Each search item must be a tuple of (field, operator, value)")
            
            filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
            key = f"search{filter_obj.to_params()}"
            
            if isinstance(item[2], list):
                for value in item[2]:
                    params.append((key, str(value)))
            else:
                params.append((key, str(item[2])))
        data = await self.client._request("GET", "/order_item_product_mappings", params=params, **kwargs)
        
        if data is None:
            return []
        
        return [OrderItemProductMapping.model_validate(item) for item in data]

    async def delete(self, **kwargs) -> bool:
        """
        Delete a specific order item product mapping by its ID.

        Args:
            order_item_product_mapping_id (int): The unique identifier of the order item product mapping to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        
        try:
            await self.client._request("DELETE", "/order_item_product_mappings", **kwargs)
            return True
        except Exception:
            return False
 