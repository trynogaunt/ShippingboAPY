from datetime import datetime as dt

class AdditionnalReferences:
    """
    AdditionnalReferences class to represent additional references in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to additional references.
    Additional references are used to manage the additional references in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the AdditionnalReferences dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class KitComponents:
    """
    KitComponents class to represent kit components in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to kit components.
    Kit components are used to manage the kit components in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the KitComponents dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class PackComponents:
    """
    PackComponents class to represent pack components in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to pack components.
    Pack components are used to manage the pack components in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the PackComponents dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class ProductAdditionalFields:
    """
    ProductAdditionalFields class to represent additional fields in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to additional fields.
    Additional fields are used to manage the additional fields in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the ProductAdditionalFields dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class ProductInstructionsFiles:
    """
    ProductInstructionsFiles class to represent instructions files in the ShippingBo API.
    
    This class is used to manage the attributes and methods related to instructions files.
    Instructions files are used to manage the instructions files in the ShippingBo API.
    
    Attributes:
        __token (str): The token used for authentication.
        __client (Client): The client instance to use for the API wrapper.
        __attributs (list): List of attributes of the ProductInstructionsFiles dynamically generated with JSON.
    """
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)
class Product:
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
        data = response.get("product")
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "created_at" or key == "updated_at":
                        value = value.split("T")[0]
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "product_additional_fields":
                        value = [ProductAdditionalFields(item) for item in value]
                    if key == "product_instructions_files":
                        value = [ProductInstructionsFiles(item) for item in value]
                    if key == "kit_components":
                        value = [KitComponents(item) for item in value]
                    if key == "pack_components":
                        value = [PackComponents(item) for item in value]
                    if key == "additionnal_references":
                        value = [AdditionnalReferences(item) for item in value]
                self.__attributes.append(key)
                setattr(self, key, value)