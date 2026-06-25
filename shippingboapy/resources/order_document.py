from __future__ import annotations
from shippingboapy.resources.base_resource import Creatable, Gettable, Downloadable
from shippingboapy.models.order_document import OrderDocument, OrderDocumentCreate
    
class OrderDocumentResource(Gettable[OrderDocument], Creatable[OrderDocumentCreate, OrderDocument], Downloadable):
    _path = "order_documents"
    _model = OrderDocument
