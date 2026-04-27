from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.logistician_service_config import LogisticianServiceConfig
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class LogisticianServiceConfigResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, id: int) -> LogisticianServiceConfig:
        """
        Retrieve a specific logistician service configuration by its unique identifier.

        Args:
            id (int): The unique identifier of the logistician service configuration to retrieve.

        Returns:
            LogisticianServiceConfig: The logistician service configuration object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the LogisticianServiceConfig model.
        """
        data = await self.client._request("GET", f"/logistician_service_configs/matching_service/PredefinedLogistician::GenericLogistician/of/{id}")
        
        if data is None:
            return None

        return LogisticianServiceConfig.model_validate(data)