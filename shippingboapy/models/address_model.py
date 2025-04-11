class Address:
    def __init__(self, response):
        self.__attributes = []
        if response is None:
            return None
        for key, value in response.items():
            self.__attributes.append(key)
            setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"