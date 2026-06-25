from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING
from shippingboapy.models.reseller import Reseller
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ResellerResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list(self) -> list[Reseller]:
        """
        Get the list of resellers in the Shippingbo account.

        Returns:
            list[Reseller]: A list of Reseller objects representing the resellers in the Shippingbo account.
        """
        data = await self.client._request("GET", "resellers")

        if data is None:
            return []

        if isinstance(data, dict) and "resellers" in data:
            data = data["resellers"]

        return [Reseller.model_validate(reseller) for reseller in data]

    async def get(self, reseller_id: int) -> Reseller:
        """
        Get the details of a specific reseller by its ID.

        Args:
            reseller_id (int): The unique identifier of the reseller.

        Returns:
            Reseller: A Reseller object representing the details of the specified reseller.
        """
        data = await self.client._request("GET", f"resellers/{reseller_id}")

        if data is None:
            raise ValueError(f"Reseller with ID {reseller_id} not found.")

        if isinstance(data, dict) and "reseller" in data:
            data = data["reseller"]
        
        return Reseller.model_validate(data)