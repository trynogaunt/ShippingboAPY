from __future__ import annotations
from typing import TYPE_CHECKING, List
from shippingboapy.models.address_label_config import AddressLabelConfig, AddressLabelConfigDetails
from shippingboapy.models.filter import Filter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class AddressLabelConfigResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, id: int) -> AddressLabelConfig:
        """
        Retrieve a specific address label configuration by its unique identifier.

        Args:
            id (int): The unique identifier of the address label configuration to retrieve.

        Returns:
            AddressLabelConfigDetails: The address label configuration details object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the AddressLabelConfig model.
        """
        data = await self.client._request("GET", f"/address_label_configs/{id}")
        if data is None:
            return None

        return AddressLabelConfigDetails.model_validate(**data.get("address_label_config", {}))
    
    async def list(self, 
                   limit: int=50, 
                   offset: int=0, 
                   search: List[tuple[str, str, str]] = None) -> list[AddressLabelConfig]:
        """
        Retrieve a list of address label configurations.

        Returns:
            list[AddressLabelConfig]: A list of address label configuration objects.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the AddressLabelConfig model.
        """
        params = {"limit": limit, 
                  "offset": offset}
        
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
                key = f"search{filter_obj.to_params()}"
                
                if isinstance(item[2], list):
                    for value in item[2]:
                        params.append((key, str(value)))
                    else:
                        params.append((key, str(item[2])))
        
        data = await self.client._request("GET", "/address_label_configs", params=params)
        if data is None:
            return []
        
        return [AddressLabelConfig.model_validate(**item) for item in data.get("addressLabelConfigs", [])]