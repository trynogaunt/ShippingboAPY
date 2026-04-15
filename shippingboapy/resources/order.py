from __future__ import annotations
from typing import TYPE_CHECKING, List, Literal
from shippingboapy.models.order import Order, OrderSummary, OrderCreate,OrderCreated
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
        
        return Order(**data)
    
    async def list(self, 
                   limit: int = 50,  # The maximum number of orders to return in a single request. Default is 50 cause API limit.
                   offset: int = 0, 
                   search: List[tuple[str, str, str]] = None, 
                   tags: List[str] = None, 
                   sort: List[tuple[str, Literal["asc", "desc"]]] = None,
                   **kwargs) -> List[OrderSummary]:

        params = {
            "limit": limit,
            "offset": offset,
        }
            
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                params[f"search{Filter(field=item[0], operator=Operator(item[1]), value=item[2]).to_params()}"] = str(item[2])
        
        if tags is not None:
            for tag in tags:
                params["search[joins][order_tags][value__eq]"] = tag
                
        if sort is not None:
            for item in sort:
                if len(item) != 2:
                    raise ValueError(f"Invalid sort item: {item}. Each sort item must be a tuple of (field, direction).")
                
                params[f"sort[{item[0]}]"] = str(item[1])
                
        data = await self.client._request("GET", "/orders", params=params, **kwargs)
        
        if data is None:
            return []
        
        return [OrderSummary(**item) for item in data]

    async def create(self, order_create: OrderCreate, **kwargs) -> Order:
        """
        Create a new order in the Shippingbo account.

        Args:
            order_create (OrderCreate): An OrderCreate object containing the details of the order to create.
        Returns:
            Order: An Order object representing the details of the created order.
        """
        
        if self.client.token.scope and "order" not in self.client.token.scope.split():
            raise ValueError("The access token does not have the required 'order' scope to create an order.")
        
        data = await self.client._request("POST", "/orders", json=order_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None

        return OrderCreated(**data)