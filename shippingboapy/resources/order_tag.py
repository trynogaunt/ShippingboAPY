from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable, Deletable
from shippingboapy.models.order_tag import OrderTag, OrderTagCreate
    
class OrderTagResource(Gettable[OrderTag], Creatable[OrderTagCreate, OrderTag], Deletable):
    _path = "order_tags"
    _model = OrderTag
