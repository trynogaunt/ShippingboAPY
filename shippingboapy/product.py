from .api_wrapper import APIWrapper

class Product(APIWrapper):
    def __init__(self,client, token):
        super().__init__(client)
        self.endpoint = 'products'
        self.client = client
        self.access_token = token
        
    def get_products(self, limit:str="10", is_pack:bool=False, ean13:str=None, offset:str=None, updated_at:str=None, user_ref:str=None, sort_id:int=None, sort_updated_at:int="asc"):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        elif sort_updated_at not in ["asc", "desc"]:
            raise ValueError(f"asc or desc expected, got {sort_updated_at}")
        else:
            query_key = ['is_pack', 'limit', 'offset', 'search[ean13__eq]', 'search[updated_at__gt][]', 'search[user_ref_eq]', 'sort[id]', 'sort[updated_at]']
            query_value = [is_pack, limit, offset, ean13, updated_at, user_ref, sort_id, sort_updated_at]
            querystring = {}
            for key, value in zip(query_key, query_value):
                if value != None:
                    querystring[key] = value
            headers = self.build_headers()
            url = self.build_url(endpoint=self.endpoint)
            response = self.get(url, headers, querystring=querystring)
        match response.status_code:
            case 200:
                product_list = []
                for product in response.json()['products']:
                    product_list.append(ProductObject(product))
                return product_list
    def get_product_by_id(self, product_id):
        if self.client.running == False:
            print("Please run client with valid token before refreshing")
            return
        else:
            headers = self.build_headers()
            url = self.build_url(endpoint=self.endpoint, id=product_id)
            response = self.get(url, headers)
            match response.status_code:
                case 200:
                    return ProductObject(response.json()['product'])
                case 404:
                    raise Exception(f"{response.status_code} Product not found")
                case 403:
                    raise Exception(f"{response.status_code} Forbidden")
                case 401:
                    raise Exception(f"{response.status_code} Unauthorized")
                case _:
                    raise Exception(f"{response.status_code} An error occured")
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
     
class ProductObject():
    def __init__(self, response):
        self.__dict__.update(response)
    
    def __setattr__(self, name, value):
        if name == "id":
            print("You can't change the id of an order")
        else:
            self.__dict__[name] = value       