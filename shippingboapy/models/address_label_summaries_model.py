from datetime import datetime as dt

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
                else:
                    if key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "insurance_provided":
                        value = bool(value)
                self.__attributes.append(key)
                setattr(self, key, value)

class LabelCredential:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                self.__attributes.append(key)
                setattr(self, key, value)

class LabelOfferOption:        
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                self.__attributes.append(key)
                setattr(self, key, value)
                
class AddressLabelSummaries:
    """
    Address Label Summaries Model
    """

    def __init__(self, reponse):
        self.__attributes = []
        data = reponse
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "created_at" or key == "updated_at":
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                self.__attributes.append(key)
                setattr(self, key, value)