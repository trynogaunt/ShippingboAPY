class User:
    """
    User model for the Shippingbo API.
    
    :param data: The data returned from the API.
    """
    
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "roles":
                        if isinstance(value, list) and all(isinstance(item, str) for item in value):
                            value = value
                        else:
                            value = [value] if isinstance(value, str) else []
                self.__attributes.append(key)
                setattr(self, key, value)