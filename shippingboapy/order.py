from .api_wrapper import APIWrapper
from datetime import datetime
from .product import Product

class MappedProduct():
    def __init__(self, mapped_product, client, token):
        # Initialize attributes of MappedProduct from the API response
        self.__id = mapped_product['id']
        self.__quantity = mapped_product['quantity']
        self.__order_item_id = mapped_product['order_item_id']
        self.__updated_at = mapped_product['updated_at']
        self.__created_at = mapped_product['created_at']
        self.__stock_type_names = mapped_product['stock_type_names']
        self.__product = Product(client=client, token=token).get_product_by_id(mapped_product['product_id'])
    
    # Properties to access private attributes
    @property
    def id(self):
        return self.__id
    
    @property
    def quantity(self):
        return self.__quantity
    
    @property
    def order_item_id(self):
        return self.__order_item_id
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @property
    def created_at(self):
        return self.__created_at
    
    @property
    def stock_type_names(self):
        return self.__stock_type_names
    
    @property
    def product(self):
        return self.__product

class OrderObject():
    def __init__(self, response, token, client):
        # Initialize attributes of OrderObject from the API response
        self.token = token
        self.client = client
        
        self.__id = response['id']
        self.__initial_order_id = response['initial_order_id']
        self.__latest_chosen_delivery_at = response['latest_chosen_delivery_at']
        self.__latest_delivery_at = response['latest_delivery_at']
        self.__latest_shipped_at = response['latest_shipped_at']
        self.__order_tag = response['order_tags']
        self.__origin = response['origin']
        self.__origin_created_at = response['origin_created_at']
        self.__origin_ref = response['origin_ref']
        self.__payment_medium = response['payment_medium']
        self.__relay_ref = response['relay_ref']
        self.__shipments = response['shipments']
        self.__shipped_at = response['shipped_at']
        self.__shipping_address = response['shipping_address']
        self.__shipping_address_id = response['shipping_address_id']
        self.__source = response['source']
        self.__source_ref = response['source_ref']
        self.__state = response['state']
        self.__state_changed_at = response['state_changed_at']
        self.__total_discount_tax_included_cents = response['total_discount_tax_included_cents']
        self.__total_discount_tax_included_currency = response['total_discount_tax_included_currency']
        self.__total_price_cents = response['total_price_cents']
        self.__total_price_currency = response['total_price_currency']
        self.__total_shipping_cents = response['total_shipping_cents']
        self.__total_shipping_tax_cents = response['total_shipping_tax_cents']
        self.__total_shipping_tax_included_cents = response['total_shipping_tax_included_cents']
        self.__total_shipping_tax_included_currency = response['total_shipping_tax_included_currency']
        self.__total_tax_cents = response['total_tax_cents']
        self.__total_weight = response['total_weight']
        self.__total_without_tax_cents = response['total_without_tax_cents']
        self.__updated_at = response['updated_at']
        self.__mapped_carrier = response['mapped_carrier']
        self.__billing_address = response['billing_address']
        self.__chosen_delivery_service = response['chosen_delivery_service']
        self.__created_at = response['created_at']
        self.__closed_at = response['closed_at']
        self.__custom_state = response['custom_state']
        self.__earliest_chosen_delivery_at = response['earliest_chosen_delivery_at']
        self.__earliest_delivery_at = response['earliest_delivery_at']
        self.__earliest_shipped_at = response['earliest_shipped_at']
        self.__external_computed_carrier_service = response['external_computed_carrier_service']
        self.__mapped_products = response['mapped_products']
        
        # Call the method to transform mapped products
        self.__match_mapped_products()
    
    def __match_mapped_products(self):
        # Transform mapped products into instances of MappedProduct
        new_mapped_products = []
        for product in self.__mapped_products:
            new_mapped_products.append(MappedProduct(product, self.client, self.token))
        self.__mapped_products = new_mapped_products

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
    def latest_chosen_delivery_at(self):
        return self.__latest_chosen_delivery_at
    
    @property
    def latest_delivery_at(self):
        return self.__latest_delivery_at
    
    @property
    def latest_shipped_at(self):
        return self.__latest_shipped_at
    
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
    def __init__(self, client, token):
        super().__init__(client)
        self.endpoint = 'orders'
        self.client = client
        self.access_token = token
    
    def get_orders(self, limit:int=100, offset:int=0, tags:str="", shipped_at:str="", source_ref:str="", state:str="", sort:str="asc") -> list[OrderObject]:
        if not self.client.running:
            print("Please run client with valid token before refreshing")
            return
        else:
            querystring = {
                "limit": limit,
                "sort['created_at']": sort
            }
            if offset != 0:
                querystring["offset"] = offset
            if tags:
                querystring["search[joins][order_tags][value__eq]"] = tags
            if shipped_at:
                querystring["search[shipped_at__gt][]"] = shipped_at
            if source_ref:
                querystring["search[source_ref__eq]"] = source_ref
            if state:
                querystring["search[state__eq][]"] = state
            
            headers = self.build_headers()
            url = self.build_url(endpoint=self.endpoint)
            print(f"request: {url}?{querystring}")
            response = self.get(url, headers, querystring)
            match response.status_code:
                case 200:
                    order_list = []
                    for order in response.json()['orders']:
                        order_class = OrderObject(order, token=self.access_token, client=self.client)
                        order_list.append(order_class)
                    return order_list
                case 404:
                    raise Exception("Order not found")
                case 403:
                    raise Exception("Forbidden")
                case 401:
                    raise Exception("Unauthorized")
                case _:
                    raise Exception("An error occurred")
            
    def get_order_by_id(self, order_id):
        if not self.client.running:
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
                    raise Exception("An error occurred")
                
    def build_headers(self):
        self.headers = {
            "Accept": "application/json",
            "X-API-VERSION": "1",
            "X-API-APP-ID": "447",
            "Authorization": f"Bearer {self.access_token}"
        }
        return self.headers
    
    def build_url(self, endpoint, id=None):
        if id:
            return f"{self.base_url}/{endpoint}/{id}"
        return f"{self.base_url}/{endpoint}"


