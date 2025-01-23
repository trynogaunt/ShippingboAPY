import requests
import logging

class APIWrapper:
    def __init__(self, api_key):
        self.base_url = "https://app.shippingbo.com"
        self.api_key = api_key
        self.refresh_token = None
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.session.headers.update(self.headers)

        logging.basicConfig(level=logging.INFO)

    def _handle_response(self, response) -> dict | None:
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error {response.status_code}: {response.text}")
            response.raise_for_status()
    
    def authenticate(self):
        url = "https://oauth.shippingbo.com/oauth/token"
        payload = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": self.token,
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
        }
        try:
            requests.post(url, json=payload, headers=self.headers)
            print(f"Token {self.token} is still valid")
        except requests.RequestException as e:
            logging.error(f"POST request failed: {e}")
            print("Token is invalid, refreshing token")
            payload = {
                "grant_type": "refresh_token",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "refresh_token": self.refresh,
                "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
            }
            try:
                refreshed_token = requests.post(url, json=payload, headers=self.headers)
                print(refreshed_token.json())
            except requests.RequestException as e:
                logging.error(f"POST request failed: {e}")
                print("Can't refresh token")
                exit(1)

    def get(self, endpoint) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        self.authenticate()
        try:
            response = self.session.get(url=url, headers=self.headers)
            return self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"GET request failed: {e}")
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
