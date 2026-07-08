from __future__ import annotations
from shippingboapy.resources.base_resource import Creatable
from shippingboapy.models.shipment import Shipment, ShipmentCreate

class ShipmentResource(Creatable[ShipmentCreate, Shipment]):
    _path = "shipments"
    _model = Shipment