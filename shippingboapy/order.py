from .api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self,client, headers):
        super().__init__(client, headers)
        self.endpoint = 'orders'
        self.client = client
    
    def get_orders(self, limit=10):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            return self.get(endpoint=f"{self.endpoint}", querystring={"limit": limit, "sort[id]": "desc"})
     
        
    def get_order_by_id(self, order_id):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            order_id = str(order_id)
            order = self.get(f"{self.endpoint}/{order_id}", querystring=None)['order']
            order_object = OrderObject(order)
            return order_object


class OrderObject():
    def __init__(self, response):
        self.__dict__.update(response)
    
    def __setattr__(self, name, value):
        if name == "id":
            print("You can't change the id of an order")
        else:
            self.__dict__[name] = value   
   