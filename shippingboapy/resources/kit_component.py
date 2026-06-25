from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Creatable, Deletable, Updatable
from shippingboapy.models.kit_component import KitComponent, KitComponentCreate, KitComponentUpdate

class KitComponentResource(Gettable[KitComponent], Creatable[KitComponentCreate, KitComponent], Deletable, Updatable[KitComponentUpdate, KitComponent]):
    _path = "kit_components"
    _model = KitComponent
    _list_model = KitComponent

    async def get_for_kit(self, kit_id: int | str) -> list[KitComponent]:
        """
        Get all components for a specific kit.

        Args:
            kit_id (int | str): The ID of the kit.
        
        Returns:
            list[KitComponent]: A list of kit components for the specified kit.
        """
        response = await self.client._request("GET", f"{self._path}", params={"kit_product_id": str(kit_id)})

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [KitComponent.model_validate(item) for item in response]
