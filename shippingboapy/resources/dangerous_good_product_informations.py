from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, FilterableListable, Creatable, Deletable, Updatable
from shippingboapy.models.dangerous_good_product_information import DangerousGoodProductInformation, DangerousGoodProductInformationCreate, DangerousGoodProductInformationUpdate

    
class DangerousGoodProductInformationResource(Gettable[DangerousGoodProductInformation], FilterableListable[DangerousGoodProductInformation], Creatable[DangerousGoodProductInformationCreate, DangerousGoodProductInformation], Deletable, Updatable[DangerousGoodProductInformationUpdate, DangerousGoodProductInformation]):
    _path = "dangerous_goods_product_informations"
    _model = DangerousGoodProductInformation
    _list_model = DangerousGoodProductInformation
