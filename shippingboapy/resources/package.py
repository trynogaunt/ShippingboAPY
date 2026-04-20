from __future__ import annotations
from shippingboapy.exceptions import ValueError
from typing import TYPE_CHECKING
from shippingboapy.models.package import Package
if TYPE_CHECKING:
    from shippingboapy.client import Client

class PackageResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, package_id: int, **kwargs) -> Package:
        """
        Retrieve a specific package by its unique identifier.

        Args:
            package_id (int): The unique identifier of the package to retrieve.

        Returns:
            Package: The retrieved package.
        """
        data = await self.client._request("GET", f"/packages/{package_id}", **kwargs)
        
        if data is None:
            return None
        
        return Package(**data)
    