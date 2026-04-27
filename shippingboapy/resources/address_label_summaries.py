from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.address_label_summaries import AddressLabelSummaries
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class AddressLabelSummariesResource:
    def __init__(self, client: Client):
        self.client = client

    async def list(self) -> AddressLabelSummaries:
        """
        Retrieve the address label summaries by its unique identifier.

        Args:
            address_label_summaries_id (int): The unique identifier of the address label summaries to retrieve.

        Returns:
            AddressLabelSummaries: The address label summaries object corresponding to the provided identifier.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the AddressLabelSummaries model.
        """
        data = await self.client._request("GET", "/address_label_summaries")
        if data is None:
            return None
        
        return [AddressLabelSummaries.model_validate(item) for item in data.get("address_label_summaries", [])]