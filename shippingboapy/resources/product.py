from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Updatable, Creatable, Deletable
from shippingboapy.models.product import Product, ProductCreate

class ProductResource(Gettable[Product], Updatable[Product, Product], Creatable[ProductCreate, Product], Deletable):
    _path = "products"
    _dict_header = "product"
    _model = Product
 