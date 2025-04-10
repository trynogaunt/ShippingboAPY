class OrderItemProductMapping:
    """
    OrderItemProductMapping class to represent a product in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to products.
    Products are used to manage the products in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the Product dynamically generated with JSON.
    """
    def __init__(self, response):
       self.__attributes = []
       for key, value in response.items():
           self.__attributes.append(key)
           setattr(self, key, value)

    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __str__(self):
        return f"OrderItemProductMapping({self.id}, {self.product_field}, {self.product_value})"