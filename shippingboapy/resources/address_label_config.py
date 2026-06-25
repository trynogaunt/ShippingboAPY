from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, FilterableListable
from shippingboapy.models.address_label_config import AddressLabelConfig, AddressLabelConfigDetails

class AddressLabelConfigResource(Gettable[AddressLabelConfigDetails], FilterableListable[AddressLabelConfig]):
    _path = "address_label_configs"
    _model = AddressLabelConfigDetails
    _list_model = AddressLabelConfig