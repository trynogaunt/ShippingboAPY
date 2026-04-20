from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING
from shippingboapy.models.pack_component import PackComponent, PackComponentCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client
    

class PackComponentResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def create(self, pack_component_create: PackComponentCreate, **kwargs) -> PackComponent:
        """
        Create a new pack component in the Shippingbo account.

        Args:
            pack_component_create (PackComponentCreate): An instance of PackComponentCreate containing the details of the pack component to be created.
        Returns:
            PackComponent: The created pack component.
        """
        data = await self.client._request("POST", "pack_components", json=pack_component_create.model_dump(by_alias=True, exclude_none=True), **kwargs)
        
        if data is None:
            return None
        
        return PackComponent(**data)
    
    async def get(self, pack_component_id: int, **kwargs) -> PackComponent:
        """
        Retrieve a specific pack component by its unique identifier.

        Args:
            pack_component_id (int): The unique identifier of the pack component to retrieve.

        Returns:
            PackComponent: The retrieved pack component.
        """
        data = await self.client._request("GET", f"/pack_components/{pack_component_id}", **kwargs)
        
        if data is None:
            return None
        
        return PackComponent(**data)

    async def update(self, pack_component_id: int, pack_component_update: PackComponent, **kwargs) -> PackComponent:
        """
        Update an existing pack component in the Shippingbo account.

        Args:
            pack_component_id (int): The unique identifier of the pack component to update.
            pack_component_update (PackComponentCreate): An instance of PackComponentCreate containing the updated details of the pack component.
        
        Returns:
            PackComponent: The updated pack component.
        """
        data = await self.client._request("PATCH", f"/pack_components/{pack_component_id}", json=pack_component_update.model_dump(by_alias=True, exclude_none=True), **kwargs)
        
        if data is None:
            return None
        
        return PackComponent(**data)
    
    async def delete(self, pack_component_id: int, **kwargs) -> bool:
        """
        Delete a specific pack component by its unique identifier.

        Args:
            pack_component_id (int): The unique identifier of the pack component to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        
        data = await self.client._request("DELETE", f"/pack_components/{pack_component_id}", **kwargs)
        
        if data is None:
            return False
        
        return True