from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Updatable
from shippingboapy.models.package import Package

class PackageResource(Gettable[Package], Updatable[Package, Package]):
    _path = "packages"
    _model = Package
