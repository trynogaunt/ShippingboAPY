from datetime import datetime as dt

class ReturnOrderExpectedItems:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                self.__attributes.append(key)
                setattr(self, key, value)

class ReturnOrderItems:
    def __init__(self,response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                self.__attributes.append(key)
                setattr(self, key, value)
    
class ReturnedProductNotResotckable:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                self.__attributes.append(key)
                setattr(self, key, value)

class ReturnOrder:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "created_at" or key == "updated_at":
                        value = value.split("T")[0]
                    if key == "return_order_expected_items":
                        value = [ReturnOrderExpectedItems(item) for item in value]
                    if key == "return_order_items":
                        value = [ReturnOrderItems(item) for item in value]
                    if key == "returned_product_not_resotckable":
                        value = [ReturnedProductNotResotckable(item) for item in value]
                    if key == "returned_at":
                       value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "state":
                        if value not in ["new", "canceled", "returned", "closed", "dispatched", "in_trouble"]:
                            value = "new"
                self.__attributes.append(key)
                setattr(self, key, value)