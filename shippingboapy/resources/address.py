from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Listable, Creatable, Deletable, Updatable
from shippingboapy.models.address import Address, AddressCreate, AddressUpdate
    
class AddressResource(Gettable[Address], Listable[Address], Creatable[AddressCreate, Address], Deletable, Updatable[AddressUpdate, Address]):
    _path = "addresses"
    _model = Address
    _list_model = Address