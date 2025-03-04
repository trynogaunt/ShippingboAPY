import requests


class APIWrapper:
    def __init__(self, client):
        self.base_url = "https://app.shippingbo.com"
        self.client = client

    def get(self, url, headers, querystring:dict = None):
        if querystring:
            response = requests.get(url, headers=headers, params=querystring)
        else:
            response = requests.get(url, headers=headers)
        return response
    
 

