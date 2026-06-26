from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable, Updatable
from shippingboapy.models.order import Order, OrderCreate, OrderSummary, ArchivedOrder, SuborderSplit
from shippingboapy.models.filter import Filter
from typing import List, Optional, Literal

#TODO Finishing Order endpoint implementation, done until remove from run, all endpoint before are implemented, but not tested yet. Need to implement the rest of the endpoints and test all of them.

class OrderResource(Gettable[Order], Creatable[OrderCreate, Order], Updatable[Order, Order]):
    _path = "orders"
    _model = Order
    _list_model = OrderSummary

    async def list(self, limit: int = 50, offset: int = 0, search: Optional[List[Filter]] = None, sort: Optional[Literal["asc", "desc"]] = "asc") -> list[OrderSummary]:
        """
        List all orders.

        Returns:
            list[OrderSummary]: A list of all lightweight orders.
        """

        params = {
            "limit": limit,
            "offset": offset,
            "sort": sort,
        }

        if search:
            for item in search:
                key = f"search{item.to_params()}"
                params[key] = str(item.value)
            
        response = await self.client._request("GET", self._path, params=params)

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [ArchivedOrder.model_validate(item) if item.get("archived") else OrderSummary.model_validate(item) for item in response]

    async def recompute(self, order_id: int | str) -> Order:
        """
        Recompute an order by its ID.

        Args:
            order_id (int | str): The ID of the order to recompute.

        Returns:
            Order: The recomputed order.
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/recompute_mapped_products")

        if response is None:
            raise ValueError(f"Order with ID {order_id} not found or could not be recomputed.")
        
        response = self._unwrap(response)

        return Order.model_validate(response)
    

    async def remove_from_run(self, order_id: int | str) -> Order:
        """
        Remove an order from a run by its ID.

        Args:
            order_id (int | str): The ID of the order to remove from the run.
        
        Returns:
            Order: The order after being removed from the run.
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/remove_from_run")

        if response is None:
            raise ValueError(f"Order with ID {order_id} not found or could not be removed from the run.")
        
        response = self._unwrap(response)

        return Order.model_validate(response)
 

    async def redispatch(self, order_id: int | str) -> None:
        """
        Redispatch an order by its ID.

        Args:
            order_id (int | str): The ID of the order to redispatch.
        
        Returns:
            Order: The order after being redispatched.
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/retry_order_dispatch")

        if response is None:
            raise ValueError(f"Order with ID {order_id} not found or could not be redispatched.")
        
    async def split(self, order_id: int, suborder: SuborderSplit) -> None:
        """
        Split a suborder.

        Args:
            suborder (SuborderSplit): The suborder to split.
        
        Returns:
            None
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/split_suborder", json=suborder.model_dump(by_alias=True, exclude_none=True))

        if response is None:
            raise ValueError(f"Suborder with number {suborder.numberOfTheItem} not found or could not be split.")