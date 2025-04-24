class ResellerProducts:
    """
    Reseller Products
    """

    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "active":
                        value = bool(value)
                self.__attributes.append(key)
                setattr(self, key, value)