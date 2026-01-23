from .abstract_controller import AbstractController
from ..models.logistician_service_config_model import LogisticianServiceConfig

class LogisticianServiceConfigController(AbstractController):
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "logistician_service_configs/matching_service/PredefinedLogistician::GenericLogistician/of"
        self.wrapper_key = "logistician_service_config"

    def get_by_id(self, logistician_service_config_id):
        """
        Get a Logistician Service Config by its ID.
        
        :param logistician_service_config_id: The ID of the Logistician Service Config to retrieve.
        :return: The LogisticianServiceConfig object.
        """
        endpoint = f"{self.endpoint}/{logistician_service_config_id}"
        
        response = self._get(endpoint)
        return LogisticianServiceConfig(response) if response else None