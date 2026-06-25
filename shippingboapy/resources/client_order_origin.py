from __future__ import annotations
from shippingboapy.resources.base_resource import Creatable
from shippingboapy.models.client_order_origin import ClientOrderOrigin, ClientOrderOriginCreate

class ClientOrderOriginResource(Creatable[ClientOrderOriginCreate, ClientOrderOrigin]):
    _path = "client_order_origins"
    _model = ClientOrderOrigin