from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable
from shippingboapy.models.package_picture_config import PackagePictureConfig

class PackagePictureConfigResource(Gettable[PackagePictureConfig]):
    _path = "package_picture_configs"
    _model = PackagePictureConfig
