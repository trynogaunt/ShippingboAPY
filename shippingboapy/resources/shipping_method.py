from __future__ import annotations
from shippingboapy.resources.base_resource import Listable
from shippingboapy.models.shipping_method import ShippingMethod


class ShippingMethodResource(Listable[ShippingMethod]):
    _path = "shipping_methods"
    _model = ShippingMethod