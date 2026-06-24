from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.update_hook import WebHook
if TYPE_CHECKING:
    from shippingboapy.client import Client

class UpdateHookResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, hook_id: str, **kwargs) -> WebHook:
        """
        Get the details of a specific update hook by its ID.

        Args:
            hook_id (str): The unique identifier of the update hook to retrieve.

        Returns:
            WebHook: A WebHook object representing the details of the specified update hook.
        """
        
        data = await self.client._request("GET", f"/update_hooks/{hook_id}", **kwargs)
        
        if data is None:
            return None
        
        if isinstance(data, dict) and "update_hook" in data:
            data = data.get("update_hook", {})
           
        return WebHook(**data)
    
    async def list(self, **kwargs) -> list[WebHook]:
        """
        List all update hooks associated with the authenticated account.

        Returns:
            list[WebHook]: A list of WebHook objects representing the update hooks in the account.
        """
        
        data = await self.client._request("GET", "update_hooks", **kwargs)
        
        if data is None:
            return []
        
        if isinstance(data, dict) and "update_hooks" in data:
            data = data.get("update_hooks", [])
           
        return [WebHook(**item) for item in data]
    
    async def create(self, update_hook: WebHook, **kwargs) -> WebHook:
        """
        Create a new update hook in the Shippingbo account.

        Args:
            update_hook (WebHook): A WebHook object containing the details of the update hook to create.

        Returns:
            WebHook: A WebHook object representing the details of the newly created update hook.
        """
        data = await self.client._request("POST", "update_hooks", json=update_hook.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        if isinstance(data, dict) and "update_hook" in data:
            data = data.get("update_hook", {})
           
        return WebHook(**data)
    
    async def update(self, hook_id: str, update_hook: WebHook, **kwargs) -> WebHook:
        """
        Update an existing update hook in the Shippingbo account.

        Args:
            hook_id (str): The unique identifier of the update hook to update.
            update_hook (WebHook): A WebHook object containing the updated details of the update hook.

        Returns:
            WebHook: A WebHook object representing the details of the updated update hook.
        """
        data = await self.client._request("PATCH", f"/update_hooks/{hook_id}", json=update_hook.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        if isinstance(data, dict) and "update_hook" in data:
            data = data.get("update_hook", {})
           
        return WebHook(**data)
    
    async def delete(self, hook_id: str, **kwargs) -> bool:
        """
        Delete an existing update hook from the Shippingbo account.

        Args:
            hook_id (str): The unique identifier of the update hook to delete.

        Returns:
            bool: True if the update hook was successfully deleted, False otherwise.
        """
        data = await self.client._request("DELETE", f"/update_hooks/{hook_id}", **kwargs)
        
        if data is None:
            return False
        
        return True