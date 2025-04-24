from .address_model import Address
import datetime
from datetime import datetime as dt
class Config:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
                

class ExternalComputedCarrierService:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if key == "config":
                    value = Config(value)
                self.__attributes.append(key)
                setattr(self, key, value)

class MappedProducts:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class OrderItems:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class OrderTags:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class OrderDocuments:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.__dict__}>"

class ItemsShipmentSerialNumber:
    def __init__(self, response):
        self.__attributes = []
        data = response
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
                if value is None:
                    value = None
                else:
                    if key == "billing_address" or key == "shipping_address":
                        value = Address(value)
                    if key == "external_computed_carrier_service" and value:
                        value = ExternalComputedCarrierService(value)
                    if key == "mapped_products":
                        value = [MappedProducts(item) for item in value]
                    if key == "order_items":
                        value = [OrderItems(item) for item in value]
                    if key == "order_tags":
                        value = [OrderTags(item) for item in value]
                    if key == "shipped_at" or key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "order_documents":
                        value = [OrderDocuments(item) for item in value]
                    if key == "items_shipment_serial_numbers":
                        value = [ItemsShipmentSerialNumber(item) for item in value]
                self.__attributes.append(key)    
                setattr(self, key, value)