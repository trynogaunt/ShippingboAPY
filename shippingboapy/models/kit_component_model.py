class KitComponent:
    '''
    KitComponent class to represent a component of a kit in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to kit components.
    Kit component is a part of Products and is used to manage the components of a kit.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the KitComponent dynamically generated with JSON.
    '''
    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            self.__attributes.append(key)
            setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"