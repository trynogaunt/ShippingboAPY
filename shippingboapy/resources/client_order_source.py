from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.client_order_source import ClientOrderSource, ClientOrderSourceCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ClientOrderSourceResource:
    def __init__(self, client: Client):
        self.client = client

    async def create(self, client_order_source_create: ClientOrderSourceCreate) -> ClientOrderSource:
        """
        Create a new client order source.

        Args:
            client_order_source_create (ClientOrderSourceCreate): An object containing the details of the client order source to be created.

        Returns:
            ClientOrderSource: The created client order source object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the ClientOrderSource model.
        """
        data = await self.client._request("POST", "/client_order_sources", json=client_order_source_create.model_dump(by_alias=True))
        
        if data is None:
            return None

        return ClientOrderSource.model_validate(data)
