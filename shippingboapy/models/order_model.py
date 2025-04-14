from .abstract_model import AbstractModel
from .address_model import Address

class Config:
    def __init__(self, response):
        self.__attributes = []
        data = response.get("config")
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
                

class ExternalComputedCarrierService:
    def __init__(self, response):
        self.__attributes = []
        data = response.get("external_computed_carrier_service")
        if data:
            for key, value in data.items():
                if key == "config":
                    value = Config(value)
                self.__attributes.append(key)
                setattr(self, key, value)

class MappedProducts:
    def __init__(self, response):
        self.__attributes = []
        data = response.get("mapped_product")
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class OrderItems:
    def __init__(self, response):
        self.__attributes = []
        data = response.get("order_item")
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class Order:
    """
    Product class to represent a product in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to products.
    Products are used to manage the products in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the Product dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response.get("order")
        if data:
            for key, value in data.items():
                if key == "billing_address" or key == "shipping_address":
                    value = Address(value)
                if key == "external_computed_carrier_service":
                    value = ExternalComputedCarrierService(value)
                if key == "mapped_products":
                    value = MappedProducts(value)
                if key == "order_items":
                    value = OrderItems(value)
                self.__attributes.append(key)
                setattr(self, key, value)