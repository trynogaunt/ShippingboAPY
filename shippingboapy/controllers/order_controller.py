from .abstract_controller import AbstractController
from ..models.order_model import Order

class OrderController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "orders"
        self.wrapper_key = "order"
    
    def get_by_id(self, order_id):
        """
        Get a Product by its ID.
        
        :param product_id: The ID of the Product to retrieve.
        :return: The Product object.
        """
        endpoint = f"{self.endpoint}/{order_id}"
        
        response = self._get(endpoint)
        return Order(response) if response else None
    
    def get_many(self, limit=50, offset=0, sort="desc", **kwargs):
        """
        Get many orders.
        
        :param params: Optional parameters to filter the orders.
        :return: A list of Order objects.
        """
        order_list = []
        if limit > 50:
            raise ValueError("Limit parameter must be less than or equal to 50.")
        if offset < 0:
            raise ValueError("Offset parameter must be greater than or equal to 0.")
        if not isinstance(limit, int):
            raise ValueError("Limit parameter must be an integer.")
        if not isinstance(offset, int):
            raise ValueError("Offset parameter must be an integer.")
        if not isinstance(sort, str):
            raise ValueError("Sort parameter must be a string.")
        if not isinstance(kwargs, dict):
            raise ValueError("Filter parameters must be a dictionary.")
        if sort not in ["asc", "desc"]:
            raise ValueError("Sort parameter must be 'asc' or 'desc'.")
        
        shipment_tag = ["shipping_ref", "package_id", "carrier_name"]
        for key, value in kwargs.items():
            if key not in ["status", "created_at", "updated_at"]:
                raise ValueError(f"Invalid filter parameter: {key}.")
        endpoint = self.endpoint
        params = {
            "limit": limit if limit < 50 else 50,
            "offset": offset,
            "sort[created_at]": sort
        }
        response = self._get(endpoint, params=params)
        
        if response:
            for order in response['orders']:
                try:
                    order = self.get_by_id(order['id'])
                    if order:
                        order_list.append(order)
                    else:
                        print(f"Order with ID {order['id']} not found.")
                except KeyError as e:
                    print(f"Key error: {e} in order {order['id']}")
                    continue
                except TypeError as e:
                    print(f"Type error: {e} in order {order['id']}")
                    continue
                except ValueError as e:
                    print(f"Value error: {e} in order {order['id']}")
                    continue
                except Exception as e:
                    print(f"Error retrieving order {order['id']}: {e}")
                    continue
            return order_list

        