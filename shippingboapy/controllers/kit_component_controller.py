from .abstract_controller import AbstractController
from ..models.kit_component_model import KitComponent

class KitComponentController(AbstractController):
    def __init__(self, client):
        super().__init__(client)
        self.client = client
        self.endpoint = "kit_components"
    
    def get_by_id(self, kit_component_id):
        """
        Get a KitComponent by its ID.
        
        :param kit_component_id: The ID of the KitComponent to retrieve.
        :return: The KitComponent object.
        """
        endpoint = f"{self.endpoint}/{kit_component_id}"
 
        print(endpoint)
        response = self._get(endpoint)
        return KitComponent(response) if response else None
        
    