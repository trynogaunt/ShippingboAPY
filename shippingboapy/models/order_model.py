from .abstract_model import AbstractModel

class Order(AbstractModel):
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
        super().__init__(response, wrapper_key="order")