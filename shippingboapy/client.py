import requests

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


    def build_headers(self):
        """
        Construit les headers pour les requêtes
        """
        return {'Accept': 'application/json', 'X-API-VERSION': f'{self.api_version}', 'X-API-APP-ID': f'{self.app_id}', 'Authorization': f'Bearer {self.access_token}'}
        
    def refreshing_token(self):
        """
        Rafraîchit le token
        """
        url = f"https://stoplight.io/mocks/shippingbo/api/256683485/oauth/token"
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

    def run(self, token):
        """
        Lance l'authentification
        """
        url = f"https://stoplight.io/mocks/shippingbo/api/256683485/oauth/token"
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
                print("Authentification réussie")
            case 401:
                print("Non autorisé")
            case 500:
                print("Erreur interne du serveur")
            case 404:
                print("Ressource non trouvée")
            case _:
                print("Authentification échouée")
                print(response.json())
        print(response.json())                    
        return response.json()            
