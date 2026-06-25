from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable, Deletable, FilterableListable
from shippingboapy.models.order_item_product_mapping import OrderItemProductMapping, OrderItemProductMappingCreate

class OrderItemProductMappingResource(Gettable[OrderItemProductMapping], Creatable[OrderItemProductMappingCreate, OrderItemProductMapping], Deletable, FilterableListable):
    _path = "order_item_product_mappings"
    _model = OrderItemProductMapping
