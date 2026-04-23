from __future__ import annotations
from typing import TYPE_CHECKING, List
from shippingboapy.models.address_label_config import AddressLabelConfig
from shippingboapy.models.filter import Filter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class AddressLabelConfigResource:
    def __init__(self, client: Client):
        self.client = client

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
        
        return [AddressLabelConfig(**item) for item in data.get("addressLabelConfigs", [])]