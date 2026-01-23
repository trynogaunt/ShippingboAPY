from .abstract_controller import AbstractController
from ..models.product_stocks_information import ProductStocksInformation

class ProductStocksController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "product_stocks"
        self.wrapper_key = "product_stock_information"
    
    def get_by_product_id(self, product_id, product_logistic_unit_id=None):
        """
        Get a ProductStocksInformation by its ID.
        
        :param product_stock_id: The ID of the ProductStocksInformation to retrieve.
        :return: The ProductStocksInformation object.
        """
        endpoint = f"{self.endpoint}/{product_id}?"
        if product_logistic_unit_id:
            endpoint += f"product_logistic_unit_id={product_logistic_unit_id}"
        
        response = self._get(endpoint)
        return ProductStocksInformation(response) if response else None
