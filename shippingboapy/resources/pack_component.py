from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Updatable, Creatable, Deletable
from shippingboapy.models.pack_component import PackComponent, PackComponentCreate
    

class PackComponentResource(Gettable[PackComponent], Updatable[PackComponent, PackComponent], Creatable[PackComponentCreate, PackComponent], Deletable):
    _path = "pack-components"
    _model = PackComponent