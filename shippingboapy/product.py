from .api_wrapper import APIWrapper
from .exceptions import *

class ProductObject():
    """
    A class to represent a product object.
    It's the object representation of Shippingbo API product data.
    """
    def __init__(self, response):
        self.__dict__.update(response)
    
    def __setattr__(self, name, value):
        """
        Set an attribute of the ProductObject instance.
        Args:
            name (str): The name of the attribute to set.
            value (str): The value to set the attribute to.
        """
        if name == "id":
            print("You can't change the id of an order")
        else:
            self.__dict__[name] = value      
class Product(APIWrapper):
    """
    A class to represent the product endpoint of the Shippingboapy API.
    Inherits from APIWrapper.
    """
    def __init__(self,client, token):
        """
        Construct a new instance of the Product class.
        Args:
            client (Client): The client instance to use for the product endpoint.
            token (str): The access token to use for the product endpoint.
        """
        super().__init__(client)
        self.endpoint = 'products'
        self.client = client
        self.access_token = token
        
#region Product methods        
    def get_products(self, limit:str="10", is_pack:bool=False, ean13:str=None, offset:str=None, updated_at:str=None, user_ref:str=None, sort_id:int=None, sort_updated_at:int="asc") -> list[ProductObject]:
        """
        Retrieve the list of products.
        Args:
            limit (str): The maximum number of products to retrieve. Default is "10".
            is_pack (bool): Filter to retrieve only pack products. Default is False.
            ean13 (str, optional): Filter by EAN-13 barcode.
            offset (str, optional): The offset for pagination.
            updated_at (str, optional): Filter products updated after this date.
            user_ref (str, optional): Filter by user reference.
            sort_id (int, optional): Sort by product ID.
            sort_updated_at (str): Sort by updated_at field, either "asc" or "desc". Default is "asc".
        Returns:
            list: A list of ProductObject instances representing the retrieved products.
        Raises:
            ValueError: If sort_updated_at is not "asc" or "desc".
        Notes:
            Ensure the client is running with a valid token before calling this method.
        """
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
        """
        Retrieve a product by ID.
        Args:
            product_id (str): The ID of the product to retrieve.
        Raise:
            RequestError: If the request fails.
        Returns:
            ProductObject: A ProductObject instance representing the retrieved product.
        Notes:
            Ensure the client is running with a valid token before calling this method.
        """
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
                    raise RequestError(response.status_code,"Product not found")
                case 403:
                    raise RequestError(response.status_code, "Forbidden")
                case 401:
                    raise RequestError(response.status_code,"Unauthorized")
                case _:
                    raise RequestError(response.status_code, "An error occured")
#rendregion

#region  Building the request   
    def build_headers(self) -> dict:
        """
        Build the headers for the request.
        Returns:
            dict: The headers for the request.
        """
        self.headers = {
            "Accept": "application/json",
            "X-API-VERSION": f"1",
            "X-API-APP-ID": f"447",
            "Authorization": f"Bearer {self.access_token}"
        }
        return self.headers
    
    def build_url(self, endpoint, id=None) -> str:
        """
        Build the URL for the request.
        Args:
            endpoint (str): The endpoint to build the URL for.
            id (str, optional): The ID of the entity to build the URL for.
        Returns:
            str: The URL for the request.
        """
        if id:
            return f"{self.base_url}/{endpoint}/{id}"
        return f"{self.base_url}/{endpoint}"
#endregion