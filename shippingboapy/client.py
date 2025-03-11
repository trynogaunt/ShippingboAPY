import requests
from .order import Order
from .product import Product

class Client:
    def __init__(self, app_id : int , api_version : int , client_id : str , client_secret : str , redirect_uri : str):
        """
        Initialise la classe Client avec les informations nécessaires pour l'authentification.
        
        :param app_id: ID de l'application
        :param api_version: Version de l'API
        :param client_id: ID du client
        :param client_secret: Secret du client
        """
        self.app_id = app_id
        self.api_version = api_version
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None
        self.refresh_token = None
        self.running = False

    @property
    def order(self) -> Order:
        """
        Return the Order object as a property
        """
        return Order(self, self.access_token)   

    @property
    def product(self):
        """
        Return the Product object as a property
        """
        return Product(self, self.access_token)
        
    def refreshing_token(self):
        """
        Refresh the access token and the refresh token if they are not None
        """
        
        if self.refresh_token is None or self.access_token is None:
            print("Please run client with valid token before refreshing")
            return

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
                self.refresh_token = response.json().get("refresh_token")
                return self.access_token , self.refresh_token

    def run(self, token, refresh_token=None, access_token=None):
        """
        Connect the script to the API
        Args:
            token (str): The unique token given from admin dev dashboard
            refresh_token (str): The token used to refreshing access token
            access_token (str): The token used to access the API (limited in time)
        Notes:
            If the access_token and refresh_token are not given, the script will connect to the API with the token given from the admin dev dashboard
        """
        self.access_token = access_token
        self.refresh_token = refresh_token
        if self.access_token is None  or self.refresh_token is None :
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
                "redirect_uri": self.redirect_uri
            }

            response = requests.post(url=url, json=payload, headers=headers)
            match response.status_code:
                case 200:
                    print("Connected to the API")
                    self.access_token = response.json().get("access_token")
                    self.refresh_token = response.json().get("refresh_token")
                    self.running = True
                case 401:
                    print("Invalid token")
                    exit()
                case 500:
                    print("Internal server error")
                    exit()
                case 403:
                    print("Forbidden")
                    exit()
                case _:
                    print(response.s)
                    exit()
        else:
            self.access_token = access_token
            self.refresh_token = refresh_token
            self.running = True
              

    def authenticated(self):
        """
        Return True if the client is authenticated
        """
        return self.running


    def get_app_id(self):
        """
        Return the app ID
        """
        return self.app_id
    
    def get_api_version(self):
        """
        Return the API version
        """
        return self.api_version 
    
    def get_client_id(self):
        """
        Return the client ID
        """
        return self.client_id
    
    def get_client_secret(self):
        """
        Return the client secret
        """
        return self.client_secret
    
    def get_redirect_uri(self):
        """
        Return the redirect URI
        """
        return self.redirect_uri

    def get_access_token(self):
        """
        Return the access token
        """
        return self.access_token
    
    def get_refresh_token(self):
        """
        Return the refresh token
        """
        return self.refresh_token

    