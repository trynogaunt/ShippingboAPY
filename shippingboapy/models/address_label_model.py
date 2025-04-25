class AddressLabel:
    """
    Address Label Model
    """

    def __init__(self, reponse):
        self.__attributes = []
        data = reponse
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                self.__attributes.append(key)
                setattr(self, key, value)

            
class AddressLabelFile:
    """
    Address Label File Model
    """

    def __init__(self, reponse):
        self.__attributes = []
        data = reponse
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                self.__attributes.append(key)
                setattr(self, key, value)