from reseller import Reseller
from product import Product
from reseller_product import ResellerProducts
from order_item import OrderItem

class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self._reseller = Reseller(api_key)
        self._product = Product(api_key)
        self._reseller_product = ResellerProducts(api_key)
        self._order_item = OrderItem(api_key)

        
        pass