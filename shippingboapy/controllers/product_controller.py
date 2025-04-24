from .abstract_controller import AbstractController
from ..models.product_model import Product

class ProductController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "products"
        self.wrapper_key = "product"
    
    def get_by_id(self, product_id):
        """
        Get a Product by its ID.
        
        :param product_id: The ID of the Product to retrieve.
        :return: The Product object.
        """
        endpoint = f"{self.endpoint}/{product_id}"
        
        response = self._get(endpoint)
        return Product(response) if response else None
    
    def get_many(self, limit=50, offset=0, sort="desc", **kwargs):
        """
        Get many products.
        
        :param params: Optional parameters to filter the products.
        :return: A list of Product objects.
        """
        product_list = []
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
            if key not in ["status", "created_at", "updated_at", "user_ref_eq", "is_packed"]:
                raise ValueError(f"Invalid filter parameter: {key}.")
        endpoint = self.endpoint
        print(f"User ref_eq: {kwargs.get('user_ref_eq')}")
        params = {
            "limit": limit if limit < 50 else 50,
            "offset": offset,
            "sort[created_at]": sort,
            "is_packed": str(kwargs.get('is_packed')).lower() if kwargs.get('is_packed') else 'false',
        }
        if kwargs.get('user_ref_eq'):
            params["user_ref__eq"] = kwargs.get('user_ref_eq')
        response = self._get(endpoint, params=params)
        
        if response:
            for product in response['products']:
                try:
                    product = self.get_by_id(product['id'])
                    if product:
                        product_list.append(product)
                except Exception as e:
                    print(f"Error processing product: {e}")
        
        return product_list