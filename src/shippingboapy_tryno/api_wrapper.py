import requests
import logging

class APIWrapper:
    def __init__(self, client, headers):
        self.base_url = "https://app.shippingbo.com"

        self.session = requests.Session()
        self.headers = headers
        self.session.headers.update(headers)

        logging.basicConfig(level=logging.INFO)

    def _handle_response(self, response) -> dict | None:
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error {response.status_code}: {response.text}")
            response.raise_for_status()
    
    def get(self, endpoint, querystring) -> dict | None:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = self.session.get(url=url, headers=self.headers , params=querystring)
            return self._handle_response(response)
        except requests.RequestException as e:
            logging.error(f"GET request failed: {e}")
            return None
        

    def post(self, endpoint, payload) -> dict | None:
        url = f"{self.base_url}/{endpoint}"


        if self.authenticate():
            try:
                response = self.session.post(url=url, json=payload, headers=self.headers)
                return self._handle_response(response)
            except requests.RequestException as e:
                logging.error(f"POST request failed: {e}")
                return None
        else:
            print("Can't authenticate")
            return None
        
    def patch(self, endpoint, payload) -> dict | None:
        url = f"{self.base_url}/{endpoint}"

        if self.authenticate():
            try:
                response = self.session.patch(url=url, json=payload, headers=self.headers)
                return self._handle_response(response)
            except requests.RequestException as e:
                logging.error(f"PATCH request failed: {e}")
                return None
        else:
            print("Can't authenticate")
            return None
    
    def delete(self , endpoint) -> dict | None:
        url = f"{self.base_url}/{endpoint}"

        if self.authenticate():
            try: 
                response = self.session.delete(url=url, headers=self.headers)
                return self._handle_response(response)
            except requests.RequestException as e:
                logging.error(f"DELETE request failed: {e}")
                return None
        else:
            print("Can't authenticate")
            return None
