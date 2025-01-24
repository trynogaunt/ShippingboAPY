from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self, token : str , app_id : int , api_version : int , client_id : str , client_secret : str):
        super().__init__(token, app_id, api_version, client_id, client_secret)
        self.endpoint = 'orders'
    
    def get_orders(self):
        return self.get(f"{self.endpoint}?limit=2")
    
    def get_order(self, order_id):
        return self.get(f"{self.endpoint}/{order_id}")

   