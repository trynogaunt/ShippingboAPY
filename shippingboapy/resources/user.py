from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.user import User
if TYPE_CHECKING:
    from shippingboapy.client import Client

class UserResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self,user_id: str, **kwargs) -> User:
        """
        Get the details of a specific user by their user ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User: A User object representing the details of the specified user.
        """
        
        data = await self.client._request("GET", f"user/{user_id}", **kwargs)
        
        if data is None:
            return None
        
        if isinstance(data, dict) and "user" in data:
            data = data.get("user", {})
           
        return User(**data)
    
    async def list(self, **kwargs) -> list[User]:
        """
        List all users associated with the authenticated account.

        Returns:
            list[User]: A list of User objects representing the users in the account.
        """
        
        data = await self.client._request("GET", "users", **kwargs)
        
        if data is None:
            return []
        
        if isinstance(data, dict) and "users" in data:
            data = data.get("users", [])
           
        return [User(**item) for item in data]