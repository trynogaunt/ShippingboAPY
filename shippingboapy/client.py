import httpx
from config import ShippingBoConfig

class Client:
    def __init__(self, config: ShippingBoConfig):
        self.config = config
        self.token = None
        self.session = httpx.Client(timeout=self.config.timeout)

    def authenticate(self):
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.config.client_id,
            'client_secret': self.config.client_secret,
        }
        response = self.session.post(self.config.auth_url, data=data)
        response.raise_for_status()
        self.token = response.json().get('access_token')

    def get_headers(self):
        if not self.token:
            self.authenticate()
        return {'Authorization': f'Bearer {self.token}'}

    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.config.api_url}{endpoint}"
        headers = self.get_headers()
        kwargs['headers'] = headers
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()