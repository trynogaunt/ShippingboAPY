class ProductAdditionalFields:
    """
    Model for product additional fields.
    """

    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            setattr(self, key, value)
            self.__attributes.append(key)
        
    def __repr__(self):
        return f"<{self.__class__.__name__}>"