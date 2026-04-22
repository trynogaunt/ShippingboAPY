from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.order_dispatch import OrderDispatch
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class OrderDispatchResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, order_dispatch_id: int, **kwargs) -> OrderDispatch:
        """
        Get the details of the order dispatch associated with a specific order.

        Args:
            order_dispatch_id (int): The unique identifier of the order dispatch for which to retrieve the details.

        Returns:
            OrderDispatch: An OrderDispatch object representing the details of the order dispatch associated with the specified order.
        """
        
        data = await self.client._request("GET", f"/order_dispatches/{order_dispatch_id}", **kwargs)
        
        if data is None:
            return None
        
        return OrderDispatch(**data)