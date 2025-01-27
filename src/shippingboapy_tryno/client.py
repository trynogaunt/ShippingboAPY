import requests
import sys
import os



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/shippingboapy_tryno')))
from product import Product
from reseller import Reseller
from address import Address
from product import Product
from order import Order
from order_item import OrderItem
from reseller_product import ResellerProducts

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
        self.token_type = None
    
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
            "redirect_uri": self.redirect_uri
        }
        
        response = requests.post(url=url, json=payload, headers=headers)

        if response.status_code == 200:
            self.access_token = response.json().get("access_token")
            self.refresh_token = response.json().get("refresh_token")
            self.token_type = response.json().get("token_type")
            self.headers = {'Accept': 'application/json', 'X-API-VERSION': f'{self.api_version}', 'X-API-APP-ID': f'{self.app_id}', 'Authorization': f'Bearer {self.access_token}'}
           # self.product = Product(self.headers)
           # self.reseller =  Reseller(self.headers)
           # self.address = Address(self.headers)
            self.order = Order(self, self.headers)
           # self.order_item = OrderItem(self.headers)
           # self.reseller_product = ResellerProducts(self.headers)

            print("Client connecté à l'api shippingbo")

        else:
            print("[!] Veuillez lancer le client avec un code d'autorisation valide [!]")
            exit(1)
        
     
