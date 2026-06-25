from __future__ import annotations
from shippingboapy.resources.base_resource import Listable
from shippingboapy.models.address_label_summaries import AddressLabelSummaries
    
class AddressLabelSummariesResource(Listable[AddressLabelSummaries]):
    _path = "address_label_summaries"
    _model = AddressLabelSummaries
    _list_model = AddressLabelSummaries
