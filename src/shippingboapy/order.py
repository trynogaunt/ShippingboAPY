from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self,client, headers):
        super().__init__(client, headers)
        self.endpoint = 'orders'
    
    def get_orders(self, limit=10):
        try:
            return self.get(endpoint=f"{self.endpoint}", querystring={"limit": limit, "sort[id]": "desc"})
        except Exception as e:
            return None
        
    def get_order_by_id(self, order_id):
        order_id = str(order_id)
        return self.get(f"{self.endpoint}/{order_id}", querystring=None)

   