from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable
from shippingboapy.models.carrier import Carrier  

class CarrierResource(Gettable[Carrier]):
    _path = "carriers"
    _model = Carrier