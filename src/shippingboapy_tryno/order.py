from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self,client, headers):
        super().__init__(client, headers)
        self.endpoint = 'orders'
    
    def get_orders(self):
        try:
            return self.get(endpoint=f"{self.endpoint}", querystring={"limit": 1})
        except Exception as e:
            print(e)
            return None
    def get_order(self, order_id):
        return self.get(f"{self.endpoint}/{order_id}")

   