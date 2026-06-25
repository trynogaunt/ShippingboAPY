from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable
from shippingboapy.models.order_event import OrderEvent, OrderEventCreate
    
class OrderEventResource(Gettable[OrderEvent], Creatable[OrderEventCreate, OrderEvent]):
    _path = "order_events"
    _model = OrderEvent
