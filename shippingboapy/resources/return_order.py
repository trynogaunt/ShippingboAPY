from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING, Literal
from shippingboapy.models.return_order import ReturnOrder
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ReturnOrderResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, return_order_id: int) -> ReturnOrder:
        """
        Get a return order by its ID.

        Args:
            return_order_id (int): The ID of the return order to retrieve.

        Returns:
            ReturnOrder: The return order with the specified ID.
        """
        data = await self.client._request("GET", f"return_orders/{return_order_id}")

        if data is None:
            raise ValueError(f"Return order with ID {return_order_id} not found.")

        return ReturnOrder.model_validate(data)
    
    async def list(self) -> list[ReturnOrder]:
        """
        List all return orders.

        Returns:
            list[ReturnOrder]: A list of all return orders.
        """
        data = await self.client._request("GET", "return_orders")

        if data is None:
            return []
        
        if isinstance(data, dict) and "return_orders" in data:
            data = data["return_orders"]

        return [ReturnOrder.model_validate(item) for item in data]