from .api_wrapper import APIWrapper
from datetime import datetime

class Order(APIWrapper):
    def __init__(self,client, token):
        super().__init__(client)
        self.endpoint = 'orders'
        self.client = client
        self.access_token = token
    
    def get_orders(self, limit:int=100, offset:int=0, tags:str="", shipped_at:str="", source_ref:str="", state:str="", sort:str="asc"):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            querystring = {
                "limit": limit,
                "sort['created_at']": sort
                }
            if offset != 0:
                querystring["offset"] = offset
            if tags != "":
                querystring["search[joins][order_tags][value__eq]"] = tags
            if shipped_at != "":
                querystring["search[shipped_at__gt][]"] = shipped_at
            if source_ref != "":
                querystring["search[source_ref__eq]"] = source_ref
            if state != "":
                querystring["search[state__eq][]"] = state
            
            headers = self.build_headers()
            url = self.build_url(endpoint=self.endpoint)
            print(f"request: {url}?{querystring}")
            response = self.get(url, headers, querystring)
            order_list = []
            for order in response.json()['orders']:
                order_list.append(OrderObject(order))
            return order_list 
            
     
        
    def get_order_by_id(self, order_id):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            headers = self.build_headers()
            url = self.build_url(endpoint=self.endpoint, id=order_id)
            response = self.get(url, headers)
            match response.status_code:
                case 200:
                    return OrderObject(response.json()['order'])
                case 404:
                    raise Exception("Order not found")
                case 403:
                    raise Exception("Forbidden")
                case 401:
                    raise Exception("Unauthorized")
                case _:
                    raise Exception("An error occured")
                

    def build_headers(self):
        self.headers = {
            "Accept": "application/json",
            "X-API-VERSION": f"1",
            "X-API-APP-ID": f"447",
            "Authorization": f"Bearer {self.access_token}"
        }
        return self.headers
    
    def build_url(self, endpoint, id=None):
        if id:
            return f"{self.base_url}/{endpoint}/{id}"
        return f"{self.base_url}/{endpoint}"
    

class OrderObject():
    def __init__(self, response):
        self.__dict__.update(response)
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value  
    
    @property
    def get_id(self):
        return self.id
   