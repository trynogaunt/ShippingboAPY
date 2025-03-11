from .api_wrapper import APIWrapper
from datetime import datetime


class OrderObject():
    def __init__(self, response):
        self.__dict__.update(response)
        __id : int = response['id']
        __initial_order_id : int  = response['initial_order_id']
        __lastest_choosen_delivery_at : datetime = response['lastest_choosen_delivery_at']
        __lastest_delivery_at : datetime = response['lastest_delivery_at']
        __lastest_shipped_at : datetime = response['lastest_shipped_at']
        __order_tag : list = response['order_tags']
        __origin : str = response['origin']
        __origin_created_at : datetime = response['origin_created_at']
        __origin_ref : str = response['origin_ref']
        __payment_medium : str = response['payment_medium']
        __relay_ref : str = response['relay_ref']
        __shipments : list = response['shipments']
        __shipped_at : datetime = response['shipped_at']
        __shipping_address : dict = response['shipping_address']
        __shipping_address_id : int = response['shipping_address_id']
        __source : str = response['source']
        __source_ref : str = response['source_ref']
        __state : str = response['state']
        __state_changed_at : datetime = response['state_changed_at']
        __total_discount_tax_included_cents : float = response['total_discount_tax_included_cents']
        __total_discount_tax_included_currency : str = response['total_discount_tax_included_currency']
        __total_price_cents : float = response['total_price_cents']
        __total_price_currency : str = response['total_price_currency']
        __total_shipping_cents : float = response['total_shipping_cents']
        __total_shipping_tax_cents : float = response['total_shipping_tax_cents']
        __total_shipping_tax_included_cents : float = response['total_shipping_tax_included_cents']
        __total_shipping_tax_included_currency : str = response['total_shipping_tax_included_currency']
        __total_tax_cents : float = response['total_tax_cents']
        __total_weight : str = response['total_weight']
        __total_without_tax_cents : float = response['total_without_tax_cents']
        __updated_at : datetime = response['updated_at']
        __mapped_carrier : str = response['mapped_carrier']
        __billing_address = response['billing_address']
        __chosen_delivery_service : str = response['chosen_delivery_service']
        __created_at : datetime = response['created_at']
        __closed_at : datetime = response['closed_at']
        __custom_state : str = response['custom_state']
        __earliest_chosen_delivery_at : datetime = response['earliest_chosen_delivery_at']
        __earliest_delivery_at : datetime = response['earliest_delivery_at']
        __earliest_shipped_at : datetime = response['earliest_shipped_at']
        __external_computed_carrier_service = response['external_computed_carrier_service']

    
    @property
    def id(self):
        return self.__id

    @property
    def initial_order_id(self):
        return self.__initial_order_id
    
    @property
    def external_computed_carrier_service(self):
        return self.__external_computed_carrier_service
    
class Order(APIWrapper):
    def __init__(self,client, token):
        super().__init__(client)
        self.endpoint = 'orders'
        self.client = client
        self.access_token = token
    
    def get_orders(self, limit:int=100, offset:int=0, tags:str="", shipped_at:str="", source_ref:str="", state:str="", sort:str="asc") -> list[OrderObject]:
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
            match response.status_code:
                case 200:
                    order_list = []
                    for order in response.json()['orders']:
                        order_list.append(OrderObject(order))
                    return order_list
                case 404:
                    raise Exception("Order not found")
                case 403:
                    raise Exception("Forbidden")
                case 401:
                    raise Exception("Unauthorized")
                case _:
                    raise Exception("An error occured")
            
     
        
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
    

   