from __future__ import annotations
from shippingboapy.models.shipment_pallet import Pallet
from shippingboapy.resources.base_resource import Gettable, Listable

class ShipmentPalletResource(Gettable[Pallet], Listable[Pallet]):
    _path = "shipment_pallets"
    _model = Pallet