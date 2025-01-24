import requests

class Client:
    def __init__(self, app_id : int , api_version : int , client_id : str , client_secret : str):
        self.token = None
        self.app_id = app_id
        self.api_version = api_version
        self.client_id = client_id
        self.client_secret = client_secret
    
    def run(self, token):
        '''Get the access token from the API'''
        url = f"https://oauth.shippingbo.com/oauth/token"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": token,
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
        }
        
        response = requests.post(url=url, json=payload, headers=headers)

        if response.status_code == 200:
            print(response.json())
        else:
            print("failed to get access token")
        
     
