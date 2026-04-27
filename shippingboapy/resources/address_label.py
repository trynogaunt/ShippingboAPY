from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.address_label import AddressLabel
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class AddressLabelResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, address_label_id: int, **kwargs) -> AddressLabel:
        """
        Get the details of a specific address label by its ID.

        Args:
            address_label_id (int): The unique identifier of the address label to retrieve.

        Returns:
            AddressLabel: An AddressLabel object representing the details of the specified address label.
        """
        
        data = await self.client._request("GET", f"/address_labels/{address_label_id}", **kwargs)
        
        if data is None:
            return None
        
        return AddressLabel.model_validate(**data)
    
    async def get_file(self, address_label_id: int, **kwargs) -> bytes:
        """
        Get the file content of a specific address label by its ID.

        Args:
            address_label_id (int): The unique identifier of the address label to retrieve.

        Returns:
            bytes: The binary content of the address label file.
        """
        
        data = await self.client._download("GET", f"/address_labels/{address_label_id}/file", **kwargs)
        
        if data is None:
            return None
        
        return data