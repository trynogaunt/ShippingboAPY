from .api_wrapper import APIWrapper

class Product(APIWrapper):
    def __init__(self,client, headers):
        super().__init__(client, headers)
        self.endpoint = 'orders'
        self.client = client
    
    def get_products(self, limit=10):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            return self.get(endpoint=f"{self.endpoint}", querystring={"limit": limit, "sort[id]": "desc"})
    
    def get_product_by_id(self, product_id):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            product_id = str(product_id)
            product = self.get(f"{self.endpoint}/{product_id}", querystring=None)['product']
            product_object = ProductObject(product)
            return product_object
        
class ProductObject():
    def __init__(self, response):
        self.__dict__.update(response)
    
    def __setattr__(self, name, value):
        if name == "id":
            print("You can't change the id of an order")
        else:
            self.__dict__[name] = value       