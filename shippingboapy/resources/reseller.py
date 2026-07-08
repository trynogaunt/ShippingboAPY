from __future__ import annotations
from shippingbo.resources.base_resource import Gettable, Listable
from shippingboapy.models.reseller import Reseller


class ResellerResource(Gettable[Reseller], Listable[Reseller]):
    _path = "resellers"
    _model = Reseller