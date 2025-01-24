from reseller import Reseller
from product import Product
from reseller_product import ResellerProducts
from order_item import OrderItem
from order import Order

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self._reseller = Reseller(api_key)
        self._product = Product(api_key)
        self._reseller_product = ResellerProducts(api_key)
        self._order_item = OrderItem(api_key)
        self._order = Order(api_key)

        
    def get_reseller(self):
        return self._reseller
    
    def get_product(self):
        return self._product
    
    def get_reseller_product(self):
        return self._reseller_product
    
    def get_order_item(self):
        return self._order_item
    
    def get_order(self):
        return self._order
