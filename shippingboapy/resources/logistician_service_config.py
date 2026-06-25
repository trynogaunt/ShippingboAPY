from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable
from shippingboapy.models.logistician_service_config import LogisticianServiceConfig
    
class LogisticianServiceConfigResource(Gettable[LogisticianServiceConfig]):
    _path = "logistician_service_configs/matching_service/PredefinedLogistician::GenericLogistician/of"
    _model = LogisticianServiceConfig