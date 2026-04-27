from __future__ import annotations
from typing import TYPE_CHECKING, List, Literal
from shippingboapy.models.order import Order, OrderSummary, OrderCreate, OrderDetails, OrderItemCreate, OrderItemUpdate
from shippingboapy.exceptions import ValueError
from shippingboapy.models.filter import Filter, Operator
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
        
        return Order.model_validate(**data)
    
    async def list(self, 
                   limit: int = 50,  # The maximum number of orders to return in a single request. Default is 50 cause API limit.
                   offset: int = 0, 
                   search: List[tuple[str, str, str]] = None, 
                   tags: List[str] = None, 
                   sort: List[tuple[str, Literal["asc", "desc"]]] = None,
                   **kwargs) -> List[OrderSummary]:

        params = [
            ("limit", limit),
            ("offset", offset),
        ]
            
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
                key = f"search{filter_obj.to_params()}"
                
                if isinstance(item[2], list):
                    for value in item[2]:
                        params.append((key, str(value)))
                    else:
                        params.append((key, str(item[2])))
        
        if tags is not None:
            for tag in tags:
                params.append(("search[joins][order_tags][value__eq]", tag))
                
        if sort is not None:
            for item in sort:
                if len(item) != 2:
                    raise ValueError(f"Invalid sort item: {item}. Each sort item must be a tuple of (field, direction).")
                
                params.append((f"sort[{item[0]}]", str(item[1])))
                
        data = await self.client._request("GET", "/orders", params=params, **kwargs)
        
        if data is None:
            return []
        
        return [OrderSummary.model_validate(**item) for item in data]

    async def create(self, order_create: OrderCreate, **kwargs) -> OrderDetails:
        """
        Create a new order in the Shippingbo account.

        Args:
            order_create (OrderCreate): An OrderCreate object containing the details of the order to create.
        Returns:
            OrderDetails: An OrderDetails object representing the details of the created order.
        """
        
        if self.client.token.scope and "order" not in self.client.token.scope.split():
            raise ValueError("The access token does not have the required 'order' scope to create an order.")
        
        data = await self.client._request("POST", "/orders", json=order_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None

        return OrderDetails.model_validate(**data)

    async def update(self, order_id: int, state: str, **kwargs) -> OrderDetails:
        """
        Update an existing order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to update.
            state (str): The new state of the order.
        Returns:
            OrderDetails: An OrderDetails object representing the details of the updated order.
        """
        
        data = await self.client._request("PATCH", f"/orders/{order_id}", json={"state": state}, **kwargs)
        
        if data is None:
            return None
        
        return OrderDetails.model_validate(**data)
    
    async def recompute_mapped_products(self, order_id: int, **kwargs) -> OrderDetails:
        """
        Recompute the mapped products of an existing order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to update.
            
        Returns:
            OrderDetails: An OrderDetails object representing the details of the updated order.
        """
        
        data = await self.client._request("POST", f"/orders/{order_id}/recompute_mapped_products", **kwargs)
        
        if data is None:
            return None
        
        return OrderDetails.model_validate(**data)

    async def remove_from_run(self, order_id: int, destination_state: str, **kwargs) -> OrderDetails:
        """
        Remove an order from a run in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to remove from the run.
            destination_state (str): The state to set for the order after removing it from the run.
        Returns:
            OrderDetails: An OrderDetails object representing the details of the updated order.
        """
        
        data = await self.client._request("PATCH", f"/orders/{order_id}/remove_from_run", json={"destination_state": destination_state}, **kwargs)
        
        if data is None:
            return None
        
        return OrderDetails.model_validate(**data)

    async def redispatch(self, order_id: int, **kwargs) -> bool:
        """
        Redispatch an order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to redispatch.
        
        Returns:
            bool: True if the order was successfully redispatched, False otherwise.
        """
        data = await self.client._request("POST", f"/orders/{order_id}/retry_order_dispatch", **kwargs)
     
        return True if data is not None else False

    async def split(self, order_id: int, **kwargs) -> bool:
        """
        Split an order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to split.
        
        Returns:
            bool: True if the order was successfully split, False otherwise.    
        """
        raise NotImplementedError("TODO: implement once endpoint behavior confirmed")

    async def create_order_item(self, order_id: int, order_item_create: OrderItemCreate, **kwargs) -> OrderDetails:
        """
        Create a new order item for an existing order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to which the order item will be added.
            order_item_create (OrderItemCreate): An OrderItemCreate object containing the details of the order item to create.
        Returns:
            OrderDetails: An OrderDetails object representing the details of the updated order with the new order item.
        """
        
        data = await self.client._request("POST", f"/orders/{order_id}/order_items", json=order_item_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        return OrderDetails.model_validate(**data)
    
    async def update_order_item(self, order_id: int, order_items: List[OrderItemUpdate], **kwargs) -> OrderDetails:
        """
        Update the order items of an existing order in the Shippingbo account.

        Args:
            order_id (int): The unique identifier of the order to update.
            order_items (List[OrderItemUpdate]): A list of OrderItemUpdate objects representing the order items to update.
        Returns:
            OrderDetails: An OrderDetails object representing the details of the updated order.
        """
        
        data = await self.client._request("POST", f"/orders/{order_id}/update_order_items", json={"order_items": [order_item.model_dump(exclude_none=True, by_alias=True) for order_item in order_items]}, **kwargs)
        
        if data is None:
            return None
        
        return OrderDetails.model_validate(**data)