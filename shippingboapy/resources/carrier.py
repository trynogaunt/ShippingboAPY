from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
from shippingboapy.models.carrier import Carrier
from shippingboapy.models.filter import Filter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client

class CarrierResource:
    def __init__(self, client: Client):
        self.client = client

    async def list(self, search: Optional[List[tuple[str, str, str]]] = None) -> Carrier:
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
        params = []
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
        
        data = await self.client._request("GET", "/carriers", params=params if params else None)
        
        if data is None:
            return None

        if isinstance(data, dict) and "carriers" in data:
            data = data.get("carriers", [])

        return [Carrier.model_validate(item) for item in data]