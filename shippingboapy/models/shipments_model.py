class OrderItemShipmentPickingHistory:
    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            self.__attributes.append(key)
            setattr(self, key, value)
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

class OrderItemsShipments:
    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            if key == "order_item_shipment_picking_histories":
                value = [OrderItemShipmentPickingHistory(item) for item in value]
            self.__attributes.append(key)
            setattr(self, key, value)

class ItemsShipmentSerialNumbers:
    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            self.__attributes.append(key)
            setattr(self, key, value)

class Shipments:
    def __init__(self, response):
        self.__attributes = []
        for key, value in response.items():
            if key == "items_shipment_serial_numbers":
                value = [ItemsShipmentSerialNumbers(item) for item in value]
            if key == "order_items_shipments":
                value = [OrderItemsShipments(item) for item in value]
            self.__attributes.append(key)
            setattr(self, key, value)

    def __repr__(self):
        return f"<{self.__class__.__name__}>"