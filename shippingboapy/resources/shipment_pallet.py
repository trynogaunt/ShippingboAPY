from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING, Literal
from shippingboapy.models.shipment_pallet import Pallet
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ShipmentPalletResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, pallet_id: int) -> Pallet:
        """
        Get a shipment pallet by its ID.

        Args:
            pallet_id (int): The unique identifier of the pallet.

        Returns:
            Pallet: The shipment pallet object.
        """
        data = await self.client._request("GET", f"shipment/pallets/{pallet_id}")
        
        if data is None:
            return None

        if isinstance(data, dict) and "pallet" in data:
            data = data["pallet"]

        return Pallet.model_validate(data)
    
    async def list(self) -> list[Pallet]:
        """
        List shipment pallets with optional filtering by state.

        Args:
            state (Literal["created", "handed_to_carrier", "cancelled"], optional): The state to filter the pallets by. Defaults to None.

        Returns:
            list[Pallet]: A list of shipment pallet objects.
        """

        data = await self.client._request("GET", "shipment_pallets")
        
        if data is None:
            return []

        if isinstance(data, dict) and "pallets" in data:
            data = data["pallets"]

        return [Pallet.model_validate(item) for item in data]