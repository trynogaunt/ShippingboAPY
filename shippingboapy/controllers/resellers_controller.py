from .abstract_controller import AbstractController
from ..models.resellers_model import Resellers

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
        return Resellers(response) if response else None

    def get_many(self):
        """
        Get many resellers.
        
        :param params: Optional parameters to filter the resellers.
        :return: A list of Reseller objects.
        """
        reseller_list = []

        
        endpoint = self.endpoint
        params = {}
        
        response = self._get(endpoint, params=params)
        
        if response and self.wrapper_key in response:
            for item in response[self.wrapper_key]:
                reseller_list.append(Resellers(item))
        
        return reseller_list