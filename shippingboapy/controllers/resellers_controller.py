from .abstract_controller import AbstractController
from ..models.resellers_model import Reseller

class ResellerController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "resellers"
        self.wrapper_key = "reseller"
    
    def get_by_id(self, reseller_id):
        """
        Get a Reseller by its ID.
        
        :param reseller_id: The ID of the Reseller to retrieve.
        :return: The Reseller object.
        """
        endpoint = f"{self.endpoint}/{reseller_id}"
        
        response = self._get(endpoint)
        return Reseller(response) if response else None