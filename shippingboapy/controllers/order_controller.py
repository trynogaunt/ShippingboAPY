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
            return [Order(order) for order in response['orders']]
        return []