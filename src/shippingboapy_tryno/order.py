from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self):
        super().__init__()
        self.endpoint = 'orders'
    
    def get_orders(self):
        return self.get(f"{self.endpoint}?limit=2")
    
    def get_order(self, order_id):
        return self.get(f"{self.endpoint}/{order_id}")

   