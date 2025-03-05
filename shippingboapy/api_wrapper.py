import requests


class APIWrapper:
    def __init__(self, client):
        """
        Construct a new instance of the APIWrapper class.
        Args:
            client (Client): The client instance to use for the API wrapper.
        """
        self.base_url = "https://app.shippingbo.com"
        self.client = client

    def get(self, url, headers, querystring:dict = None):
        if querystring:
            response = requests.get(url, headers=headers, params=querystring)
        else:
            response = requests.get(url, headers=headers)
        return response
    
 

