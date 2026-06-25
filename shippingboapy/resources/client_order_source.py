from __future__ import annotations
from shippingboapy.resources.base_resource import Creatable
from shippingboapy.models.client_order_source import ClientOrderSource, ClientOrderSourceCreate

class ClientOrderSourceResource(Creatable[ClientOrderSourceCreate, ClientOrderSource]):
    _path = "client_order_sources"
    _model = ClientOrderSource