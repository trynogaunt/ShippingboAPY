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