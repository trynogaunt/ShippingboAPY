from .abstract_controller import AbstractController
from ..models.address_label_summaries_model import AddressLabelSummaries

class AddressLabelSummariesController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "address_label_summaries"
        self.wrapper_key = "address_label_summaries"

    def get_by_id(self, address_label_summary_id):
        """
        Get an AddressLabelSummary by its ID.
        
        :param address_label_summary_id: The ID of the AddressLabelSummary to retrieve.
        :return: The AddressLabelSummary object.
        """
        raise NotImplementedError("This method is not implemented yet.")
        # The API does not support getting a single address label summary by ID.
    
    def get_many(self):
        """
        Get many address label summaries.
        
        :param params: Optional parameters to filter the address label summaries.
        :return: A list of AddressLabelSummaries objects.
        """
        address_label_summary_list = []
        endpoint = self.endpoint
        params = {}

        response = self._get(endpoint, params=params)

        if response:
            for item in response[self.wrapper_key]:
                address_label_summary_list.append(AddressLabelSummaries(item))

        return address_label_summary_list