from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.tag import OrderTag, OrderTagCreate
from shippingboapy.exceptions import ValueError
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class OrderTagResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def create(self, order_tag_create: OrderTagCreate, **kwargs) -> OrderTag:
        """
        Create a new order tag in the Shippingbo account.

        Args:
            order_tag_create (OrderTagCreate): An OrderTagCreate object representing the order tag to create.  
            
        Returns:
            OrderTag: An OrderTag object representing the created order tag.
        """
        data = await self.client._request("POST", "/order_tags", json=order_tag_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        return OrderTag(**data)

    async def get(self, order_tag_id: int, **kwargs) -> OrderTag:
        """
        Retrieve an existing order tag from the Shippingbo account.

        Args:
            order_tag_id (int): The unique identifier of the order tag to retrieve.
            
        Returns:
            OrderTag: An OrderTag object representing the retrieved order tag.
        """
        
        data = await self.client._request("GET", f"/order_tags/{order_tag_id}", **kwargs)
        
        if data is None:
            return None
        
        return OrderTag(**data)
    
    async def delete(self, order_tag_id: int, **kwargs) -> bool:
        """
        Delete an existing order tag from the Shippingbo account.

        Args:
            order_tag_id (int): The unique identifier of the order tag to delete.
        
        Returns:
            bool: True if the order tag was successfully deleted, False otherwise.
        
        """
        result = await self.client._request("DELETE", f"/order_tags/{order_tag_id}", **kwargs)
        
        if result is None:
            return False
        
        return True