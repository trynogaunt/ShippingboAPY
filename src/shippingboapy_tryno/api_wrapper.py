import requests
import logging

class APIWrapper:
    def __init__(self, token : str):
        self.base_url = "https://app.shippingbo.com"
        self.refresh_token = None
        self.access_token = None
        self.id = 447
        self.client_id = "Q8TGUF0QDZVPlDZzck9kIjCs6aj7efqWoNAcnyiljKc"
        self.client_secret = "TalkAlPu47s331DxTo-z1btOiww_2luCQ-6w5oc4lX0"
        self.token = token
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
            "X-API-APP-ID ": f"{self.id}",
            "X-API-VERSION": f"{1.0}"
        }
        self.session.headers.update(self.headers)

        logging.basicConfig(level=logging.INFO)

    def _handle_response(self, response) -> dict | None:
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error {response.status_code}: {response.text}")
            response.raise_for_status()
    
    def get_access_token(self) -> bool:
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
            "code": self.token,
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
        }
        
        response = requests.post(url=url, json=payload, headers=headers)
        
        match response.status_code:
            case 200:
                self.access_token = response.json().get("access_token")
                self.headers["Authorization"] = f"Bearer {self.access_token}"
                self.session.headers.update(self.headers)
                return 1
            
            case 404:
                print(f"Error {response.status_code}: Ressource not found")
                return 0
            case 403:
                print(f"Error {response.status_code}: Access denied")
                return 0
            case _:
                print("Unknow error") 
                return 0
        
    def refresh_access_token(self) -> bool:
        '''Refresh the access token'''
        url = f"https://oauth.shippingbo.com/oauth/token"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token
        }
        
        response = requests.post(url=url, json=payload, headers=headers)

        match response.status_code:
            case 200:
                self.access_token = response.json().get("access_token")
                self.headers["Authorization"] = f"Bearer {self.access_token}"
                self.session.headers.update(self.headers)
                return 1
            
            case 404:
                print(f"Error {response.status_code}: Ressource not found")
                return 0
            case 403:
                print(f"Error {response.status_code}: Access denied")
                return 0
            case _:
                print("Unknow error") 
                return 0
    
    def authenticate(self) -> bool:
        access_token_check = self.get_access_token()
        if access_token_check:
            return 1
        else:
            refresh_token_check = self.refresh_access_token()
            if refresh_token_check:
                return 1
            else:
                return 0
            

    def get(self, endpoint) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        
        if self.authenticate():
            try:
                response = self.session.get(url=url, headers=self.headers)
                return self._handle_response(response)
            except requests.RequestException as e:
                logging.error(f"GET request failed: {e}")
                return None
        else:
            print("Can't authenticate")
            return None

    def post(self, endpoint, payload) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        self.authenticate()
        try:
            response = self.session.post(url=url, json=payload, headers=self.headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"POST request failed: {e}")
            return None

    def patch(self, endpoint, payload) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        self.authenticate()
        try:
            response = self.session.patch(url=url, json=payload, headers=self.headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"PATCH request failed: {e}")
            return None
    
    def delete(self , endpoint) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        self.authenticate()
        try: 
            response = self.session.delete(url=url, headers=self.headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"DELETE request failed: {e}")
            return None
