from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.carrier import Carrier
if TYPE_CHECKING:
    from shippingboapy.client import Client

class CarrierResource:
    def __init__(self, client: Client):
        self.client = client

    async def list(self) -> Carrier:
        """
        Retrieve a specific carrier by its unique identifier.

        Args:
            carrier_id (int): The unique identifier of the carrier to retrieve.

        Returns:
            Carrier: The carrier object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the Carrier model.
        """
        data = await self.client._request("GET", "/carriers")
        
        if data is None:
            return None

        return [Carrier.model_validate(item) for item in data]