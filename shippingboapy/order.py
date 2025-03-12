from .api_wrapper import APIWrapper
from datetime import datetime
from .product import Product


class OrderObject():
    def __init__(self, response, token , client):
       var_test = 1
        

#region order object property         
    @property
    def id(self):
        return self.__id

    @property
    def initial_order_id(self):
        return self.__initial_order_id
    
    @property
    def external_computed_carrier_service(self):
        return self.__external_computed_carrier_service

    @property
    def lastest_choosen_delivery_at(self):
        return self.__lastest_choosen_delivery_at
    
    @property
    def lastest_delivery_at(self):
        return self.__lastest_delivery_at
    
    @property
    def lastest_shipped_at(self):
        return self.__lastest_shipped_at
    
    @property
    def order_tag(self):
        return self.__order_tag
    
    @property
    def origin(self):
        return self.__origin
    
    @property
    def origin_created_at(self):
        return self.__origin_created_at
    
    @property
    def origin_ref(self):
        return self.__origin_ref
    
    @property
    def payment_medium(self):
        return self.__payment_medium
    
    @property
    def relay_ref(self):
        return self.__relay_ref
    
    @property
    def shipments(self):
        return self.__shipments
    
    @property
    def shipped_at(self):
        return self.__shipped_at
    
    @property
    def shipping_address(self):
        return self.__shipping_address
    
    @property
    def shipping_address_id(self):
        return self.__shipping_address_id
    
    @property
    def source(self):
        return self.__source
    
    @property
    def source_ref(self):
        return self.__source_ref
    
    @property
    def state(self):
        return self.__state
    
    @property
    def state_changed_at(self):
        return self.__state_changed_at
    
    @property
    def total_discount_tax_included_cents(self):
        return self.__total_discount_tax_included_cents
    
    @property
    def total_discount_tax_included_currency(self):
        return self.__total_discount_tax_included_currency
    
    @property
    def total_price_cents(self):
        return self.__total_price_cents
    
    @property
    def total_price_currency(self):
        return self.__total_price_currency
    
    @property
    def total_shipping_cents(self):
        return self.__total_shipping_cents
    
    @property
    def total_shipping_tax_cents(self):
        return self.__total_shipping_tax_cents
    
    @property
    def total_shipping_tax_included_cents(self):
        return self.__total_shipping_tax_included_cents
    
    @property
    def total_shipping_tax_included_currency(self):
        return self.__total_shipping_tax_included_currency
    
    @property
    def total_tax_cents(self):
        return self.__total_tax_cents
    
    @property
    def total_weight(self):
        return self.__total_weight
    
    @property
    def total_without_tax_cents(self):
        return self.__total_without_tax_cents
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @property
    def mapped_carrier(self):
        return self.__mapped_carrier
    
    @property
    def billing_address(self):
        return self.__billing_address
    
    @property
    def chosen_delivery_service(self):
        return self.__chosen_delivery_service
    
    @property
    def created_at(self):
        return self.__created_at
    
    @property
    def closed_at(self):
        return self.__closed_at
    
    @property
    def custom_state(self):
        return self.__custom_state
    
    @property
    def earliest_chosen_delivery_at(self):
        return self.__earliest_chosen_delivery_at
    
    @property
    def earliest_delivery_at(self):
        return self.__earliest_delivery_at
    
    @property
    def earliest_shipped_at(self):
        return self.__earliest_shipped_at

    @property
    def mapped_products(self):
        return self.__mapped_products
#endregion

    def test(self):
        print('ok')
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
                        order_class = OrderObject(order)
                        order_list.append(order_class)
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
                    order_item = OrderObject(response.json()['order'], token=self.access_token, client=self.client)
                    return order_item
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
    

   