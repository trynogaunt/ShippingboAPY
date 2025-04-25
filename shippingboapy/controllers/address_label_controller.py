from abstract_controller import AbstractController
from ..models.address_label_model import AddressLabel, AddressLabelFile

class AddressLabelController(AbstractController):
    """
    Address Label Summaries Model
    """

    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "address_labels"
        self.wrapper_key = "address_label"
        self.wrapper_key_file = "address_label_file"
    
    def get_by_id(self, address_label_id):
        """
        Get an AddressLabel by its ID.
        
        :param address_label_id: The ID of the AddressLabel to retrieve.
        :return: The AddressLabel object.
        """
        endpoint = f"{self.endpoint}/{address_label_id}"     
        response = self._get(endpoint)
        return AddressLabel(response) if response else None

    def get_file(self, address_label_id):
        """
        Get an AddressLabelFile by its ID.
        
        :param address_label_id: The ID of the AddressLabel to retrieve.
        :return: The AddressLabelFile object.
        """
        endpoint = f"{self.endpoint}/{address_label_id}/file"
        
        response = self._get(endpoint)
        return AddressLabelFile(response) if response else None