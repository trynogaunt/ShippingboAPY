import requests
class AbstractController:
    """
    Abstract base class for controllers in the ShippingBo API.
    """

    def __init__(self, api_client):
        """
        Initialize the controller with the given API client.

        :param api_client: An instance of the API client to be used by the controller.
        """
        self.api_client = api_client
        self.base_url = api_client.base_url
    
    def _build_headers(self):
        if not self.client.authenticated:
            raise Exception("Client is not authenticated. Please authenticate first.")
        headers = {
            "Accept":"application/json",
            "X-API-VERSION": self.client.api_version,
            "X-API-APP-ID": self.client.app_id,
            "Authorization": f"Bearer {self.client.access_token}"
        }
        
        return headers

    def _process_reponse(self, response):
        """
        Process the API response.

        :param response: The response from the API.
        :return: The processed response.
        """
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 201:
            return response.json()
        elif response.status_code == 204:
            return None
        elif response.status_code == 401:
            raise Exception("Unauthorized: Invalid access token.")
        elif response.status_code == 403:
            raise Exception("Forbidden: Access denied.")
        elif response.status_code == 404:
            raise Exception("Not Found: The requested resource was not found.")
        elif response.status_code == 500:
            raise Exception("Internal Server Error: An error occurred on the server.")
        else:
            raise Exception(f"Unexpected error: {response.status_code} - {response.text}")
        
    
    def _get(self, endpoint, params=None):
        """
        Send a GET request to the specified endpoint.

        :param endpoint: The API endpoint to send the request to.
        :param params: Optional parameters to include in the request.
        :return: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers()
        if params:
            response = requests.get(url, headers=headers, params=params)
        else:
            response = requests.get(url, headers=headers)
        return self._process_reponse(response)
    
    def _patch(self, endpoint, data):
        """
        Send a PATCH request to the specified endpoint.

        :param endpoint: The API endpoint to send the request to.
        :param data: The data to include in the request body.
        :return: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = self._build_headers()
        response = requests.patch(url, headers=headers, json=data)
        return self._process_reponse(response)