from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.order_event import OrderEvent, OrderEventCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class OrderEventResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, order_event_id: int, **kwargs) -> OrderEvent:
        """
        Get the details of a specific order event by its ID.

        Args:
            order_event_id (int): The unique identifier of the order event to retrieve.

        Returns:
            OrderEvent: An OrderEvent object representing the details of the specified order event.
        """
        
        data = await self.client._request("GET", f"/order_events/{order_event_id}", **kwargs)
        
        if data is None:
            return None
        
        return OrderEvent.model_validate(**data)
    
    async def create(self, order_event_create: OrderEventCreate, **kwargs) -> OrderEvent:
        """
        Create a new order event for a specific order.

        Args:
            order_event_create (OrderEventCreate): An OrderEventCreate object containing the details of the order event to create.
            
        Returns:
            OrderEvent: An OrderEvent object representing the newly created order event.
        """
        
        data = await self.client._request("POST", "/order_events", json=order_event_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        return OrderEvent.model_validate(**data)