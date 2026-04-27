from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.kit_component import KitComponent, KitComponentCreate, KitComponentUpdate
if TYPE_CHECKING:
    from shippingboapy.client import Client
    

class KitComponentResource:
    def __init__(self, client: Client):
        self.client = client
        
    async def create(self, kit_component_create: KitComponentCreate) -> KitComponent:
        data = await self.client._request(
            "POST",
            "kit_components",
            json=kit_component_create.model_dump(by_alias=True)
        )
        
        if data is None:
            return None
        
        return KitComponent.model_validate(data.get("kit_component", {}))
    
    async def get(self, kit_component_id: int) -> KitComponent:
        data = await self.client._request("GET", f"kit_components/{kit_component_id}")
        
        if data is None:
            return None
        
        return KitComponent.model_validate(data.get("kit_component", {}))
    
    async def list(self, kit_product_id: int) -> list[KitComponent]:
        data = await self.client._request("GET", "kit_components", params={"kit_product_id": kit_product_id})      

        if data is None:
            return None
        
        return [KitComponent.model_validate(item) for item in data.get("kit_components", [])]
    
    async def update(self, kit_component_id: int, kit_component_update: KitComponentUpdate) -> KitComponent:
        data = await self.client._request(
            "PATCH",
            f"kit_components/{kit_component_id}",
            json=kit_component_update.model_dump(by_alias=True)
        )
        if data is None:
            return None 
        return KitComponent.model_validate(data.get("kit_component", {}))
    
    async def delete(self, kit_component_id: int) -> None:
        data = await self.client._request(
            "DELETE",
            f"kit_components/{kit_component_id}"
        )
        
        if data is None:
            return False
        
        return True