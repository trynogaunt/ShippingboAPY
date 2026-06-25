from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Downloadable
from shippingboapy.models.address_label import AddressLabel
    
class AddressLabelResource(Gettable[AddressLabel], Downloadable):
    _path = "address_labels"
    _model = AddressLabel
    
