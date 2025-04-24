from datetime import datetime as dt


class ItemLines:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class PackageProductHistories:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class OrderItemPackage:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                self.__attributes.append(key)
                setattr(self, key, value)

class Package:
    def __init__(self, response):
        self.__attributes = []
        data = response
        if data:
            for key, value in data.items():
                if value is None:
                    value = None
                else:
                    if key == "updated_at" or key == "created_at" or key=="requested_shipping_date":
                        value = value.split("T")[0]
                        value = dt.fromisoformat(value).strftime("%Y-%m-%d %H:%M:%S")
                    if key == "item_lines":
                        value = [ItemLines(item) for item in value]
                    
                    if key == "package_product_histories":
                        value = [PackageProductHistories(item) for item in value]
                    
                    if key == "order_item_package":
                        value = [OrderItemPackage(item) for item in value]
                self.__attributes.append(key)
                setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"