from __future__ import annotations
from shippingboapy.resources.base_resource import FilterableGettable
from shippingboapy.models.carrier import Carrier  

class CarrierResource(FilterableGettable[Carrier]):
    _path = "carriers"
    _model = Carrier