from shippingboapy.controllers.kit_component_controller import KitComponentController
from shippingboapy.controllers.product_controller import ProductController
import requests

class Client:
    """
    Main class to interact with the ShippingBo API.
    This class handle authentication, API requests and responses.
    It is used to manage the connection to the API and handle errors.
    """
    
    def __init__(self, app_id, api_version, client_id, client_secret, redirect_uri):
        """
        Initialize the client with the given parameters.
        
        :param app_id: The application ID.
        :param api_version: The API version to use.
        :param client_id: The client ID for authentication.
        :param client_secret: The client secret for authentication.
        :param redirect_uri: The redirect URI for authentication.
        """
        # Initialize the client with the given parameters
        # and set the base URL for the API.
        self.app_id = app_id
        self.api_version = api_version
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.base_url = f"https://app.shippingbo.com"
        self.auth_url = f"https://oauth.shippingbo.com/oauth/token"
        
        # Initialize the access token and refresh token
        self.access_token = None
        self.refresh_token = None
        self.token_expiry = None
        self.token_creation_time = None
        self.authenticated = False
        
        # Initialize controllers for different API resources
        self.kit_component = None
        self.product = None
        
    def authenticate(self, auth_code=None, refresh_token=None, access_token=None):
            """
            Authenticate the client using the provided authorization code.
            
            :param auth_code: The authorization code received from the OAuth flow.
            """
            # If an authorization code is provided and no access token, use it to get an access token
            if auth_code and not access_token and not refresh_token:
                print(self._get_access_token(auth_code))
            else:
                # If no authorization code is provided, check if we have a refresh token
                if refresh_token:
                    self.refresh_token = refresh_token
                    self.refresh_authentication()
                # If no refresh token is available, raise an exception
                else:
                    raise Exception("No authorization code or refresh token provided.")
            if self.access_token and self.refresh_token:
                print("Access token and refresh token are already set.")
                self._initialize_controllers()
        
    def _get_access_token(self, auth_code):
            '''
            Get an access token using the provided authorization code.
            If access token is successfully retrieved, set the access token and refresh token.
            If the request fails, raise an exception with the error message.
            '''
            payload = {
                'grant_type': 'authorization_code',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'redirect_uri': self.redirect_uri,
                'code': auth_code
            }
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            try:
                # Make a POST request to the authentication URL to get the access token
                response = requests.post(self.auth_url, json=payload, headers=headers)
                response.raise_for_status()
                self.access_token = response.json().get('access_token')
                self.refresh_token = response.json().get('refresh_token')
                self.token_expiry = response.json().get('expires_in')
                self.authenticated = True
                return self.access_token , self.refresh_token
            except requests.exceptions.HTTPError as err:
                if err.response.status_code == 400:
                    raise Exception("Invalid authorization code or redirect URI.")
                elif err.response.status_code == 401:
                    raise Exception("Invalid client ID or client secret.")
                elif err.response.status_code == 403:
                    raise Exception("Access denied. Check your permissions.")
                else:
                    raise Exception(f"Failed to get access token: {err.response.text}")
            
    def refresh_authentication(self):
            """
            Refresh the access token using the refresh token.
            
            :param refresh_token: The refresh token used to get a new access token.
            """
            # If we have a refresh token, use it to get a new access token
            if self.refresh_token:
                payload = {
                    'grant_type': 'refresh_token',
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'refresh_token': self.refresh_token
                }
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
                try:
                    response = requests.post(self.auth_url, json=payload, headers=headers)
                    response.raise_for_status()
                    self.access_token = response.json().get('access_token')
                    self.refresh_token = response.json().get('refresh_token')
                    self.token_expiry = response.json().get('expires_in')
                    self.token_creation_time = response.json().get('created_at')
                    self.authenticated = True
                except Exception.HTTPError as err:
                    if err.response.status_code == 400:
                        raise Exception("Invalid refresh token.")
                    elif err.response.status_code == 401:
                        raise Exception("Invalid client ID or client secret.")
                    elif err.response.status_code == 403:
                        raise Exception("Access denied. Check your permissions.")
                    else:
                        raise Exception(f"Failed to refresh access token: {err.response.text}")
                    
            else:
                raise Exception("No refresh token available.")
            
    def is_authenticated(self):
            """
            Check if the client is authenticated.
            
            :return: True if authenticated, False otherwise.
            """
            return self.authenticated

    def _initialize_controllers(self):
            """
            Initialize the controllers for different API resources.
            """
            self.kit_component = KitComponentController(self)
            self.product = ProductController(self)
