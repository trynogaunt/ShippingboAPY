from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING, Literal
from shippingboapy.models.order import Order
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class OrderResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, order_id: int, **kwargs) -> Order:
        """
        Get the details of a specific order by its ID.

        Args:
            order_id (int): The unique identifier of the order to retrieve.

        Returns:
            Order: An Order object representing the details of the specified order.
        """
        
        data = await self.client._request("GET", f"/orders/{order_id}", **kwargs)
        
        if data is None:
            return None
        
        return Order(**data)