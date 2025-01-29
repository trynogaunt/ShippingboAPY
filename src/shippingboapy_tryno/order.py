from api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self,client, headers):
        super().__init__(client, headers)
        self.endpoint = 'orders'
    
    def get_orders(self, limit=10):
        try:
            return self.get(endpoint=f"{self.endpoint}", querystring={"limit": limit})
        except Exception as e:
            if e.response.status_code == 401:
                self.client.refreshing_token()
                return self.get_orders(limit)
            print(e)
            return None
    def get_order(self, order_id):
        return self.get(f"{self.endpoint}/{order_id}")

   