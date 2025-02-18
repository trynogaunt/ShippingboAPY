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
        self.order = None

    def build_headers(self):
        """
        Construit les headers pour les requêtes
        """
        return {'Accept': 'application/json', 'X-API-VERSION': f'{self.api_version}', 'X-API-APP-ID': f'{self.app_id}', 'Authorization': f'Bearer {self.access_token}'}
        
    def refreshing_token(self):
        """
        Rafraîchit le token
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

    def run(self, token):
        """
        Lance l'authentification
        """
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
                self.access_token = response.json().get("access_token")
                self.refresh_token = response.json().get("refresh_token")
                self.token_type = response.json().get("token_type")
                self.headers = self.build_headers()
                self.order = Order(self, self.headers)
                self.product = Product(self, self.headers)
                print("Authentification réussie")
                self.running = True
                return self.access_token , self.refresh_token
            case 400:
                print("Requête invalide")
            case 403:
                print("Interdit")
            case 401:
                print("Non autorisé")
            case 500:
                print("Erreur interne du serveur")
            case 404:
                print("Ressource non trouvée")
            case _:
                print("Authentification échouée")
                print(response.json())       

    def authenticated(self):
        """
        Vérifie si le client est authentifié
        """
        return self.running

    def get_app_id(self):
        """
        Retourne l'ID de l'application
        """
        return self.app_id
    
    def get_api_version(self):
        """
        Retourne la version de l'API
        """
        return self.api_version 
    
    def get_client_id(self):
        """
        Retourne l'ID du client
        """
        return self.client_id
    
    def get_client_secret(self):
        """
        Retourne le secret du client
        """
        return self.client_secret
    
    def get_redirect_uri(self):
        """
        Retourne l'URI de redirection
        """
        return self.redirect_uri

    def get_access_token(self):
        """
        Retourne le token d'accès
        """
        return self.access_token
    
    def get_refresh_token(self):
        """
        Retourne le token de rafraîchissement
        """
        return self.refresh_token

    