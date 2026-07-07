from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable, Updatable
from shippingboapy.models.order import Order, OrderCreate, OrderSummary, ArchivedOrder, SuborderSplit, Suborder, OrderItemUpdate, OrderUpdate
from shippingboapy.models.filter import Filter
from typing import List, Optional, Literal

#TODO Finishing Order endpoint implementation, done until remove from run, all endpoint before are implemented, but not tested yet. Need to implement the rest of the endpoints and test all of them.

class OrderResource(Gettable[Order], Creatable[OrderCreate, Order], Updatable[Order, OrderUpdate]):
    _path = "orders"
    _dict_header = "order"
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
            order_id (int): The ID of the order to split the suborder for.
            suborder (SuborderSplit): The suborder to split.
        
        Returns:
            None
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/split_suborder", json=suborder.model_dump(by_alias=True, exclude_none=True))

        if response is None:
            raise ValueError(f"Suborder with number {suborder.numberOfTheItem} not found or could not be split.")
    
    async def get_suborders(self, order_id: int) -> list[Suborder]:
        """
        Get all suborders for a given order.

        Args:
            order_id (int): The ID of the order to get suborders for.
        
        Returns:
            list[Suborder]: A list of all suborders for the given order.
        """

        response = await self.client._request("GET", f"{self._path}/{order_id}/suborders")

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [Suborder.model_validate(item) for item in response]
    
    async def update_order_items(self, order_id: int | str, order_items: list[OrderItemUpdate]) -> Order:
        """
        Update the items of an order.

        Args:
            order_id (int | str): The ID of the order to update.
            order_items (list[OrderItemUpdate]): A list of OrderItemUpdate objects representing the updated order items.
        
        Returns:
            Order: The updated order.
        """
        response = await self.client._request("PATCH", f"{self._path}/{order_id}/update_order_items", json={"order_items": [item.model_dump(by_alias=True, exclude_none=True) for item in order_items]})

        if response is None:
            raise ValueError(f"Order with ID {order_id} not found or could not be updated.")
        
        response = self._unwrap(response)

        return Order.model_validate(response)
    
    #TODO rework all order models
    async def add_order_item(self, order_id: int | str, order_item: OrderItemUpdate) -> Order:
        """
        Add an item to an order.

        Args:
            order_id (int | str): The ID of the order to add the item to.
            order_item (OrderItemUpdate): The OrderItemUpdate object representing the item to add.
        
        Returns:
            Order: The updated order with the new item added.
        """
        response = await self.client._request("POST", f"{self._path}/{order_id}/add_order_item", json=order_item.model_dump(by_alias=True, exclude_none=True))

        if response is None:
            raise ValueError(f"Order with ID {order_id} not found or could not be updated.")
        
        response = self._unwrap(response)

        return Order.model_validate(response)