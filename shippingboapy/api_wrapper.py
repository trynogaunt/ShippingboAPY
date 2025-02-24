import requests


class APIWrapper:
    def __init__(self, client):
        self.base_url = "https://app.shippingbo.com"
        self.client = client

    def get(self, url, headers, querystring:dict = None):
        if querystring:
            print("Using querystring")
            response = requests.get(url, headers=headers, params=querystring)
        else:
            print("Not using querystring")
            response = requests.get(url, headers=headers)
        return response
    
 

