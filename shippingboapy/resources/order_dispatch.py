from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable
from shippingboapy.models.order_dispatch import OrderDispatch
    
class OrderDispatchResource(Gettable[OrderDispatch]):
    _path = "order_dispatches"
    _model = OrderDispatch
