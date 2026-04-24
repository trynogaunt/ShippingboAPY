from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.client_order_origin import ClientOrderOrigin, ClientOrderOriginCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client

class ClientOrderOriginResource:
    def __init__(self, client: Client):
        self.client = client

    async def create(self, client_order_origin_create: ClientOrderOriginCreate) -> ClientOrderOrigin:
        """
        Create a new client order origin.

        Args:
            client_order_origin_create (ClientOrderOriginCreate): An object containing the details of the client order origin to be created.

        Returns:
            ClientOrderOrigin: The created client order origin object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the ClientOrderOrigin model.
        """
        data = await self.client._request("POST", "/client_order_origins", json=client_order_origin_create.model_dump(by_alias=True))
        
        if data is None:
            return None

        return ClientOrderOrigin(**data)