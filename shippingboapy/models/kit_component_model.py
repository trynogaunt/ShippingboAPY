
from .abstract_model import AbstractModel

class KitComponent(AbstractModel):
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
        super().__init__(response, wrapper_key="kit_component")