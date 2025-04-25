from .abstract_controller import AbstractController
from ..models.user_model import User

class UserController(AbstractController):
    """
    UserController for the Shippingbo API.
    :param api_client: The API client to use for making requests.
    """
    def __init__(self, api_client):
        super().__init__(api_client)
        self.client = api_client
        self.endpoint = "users"
        self.wrapper_key = "user"

    def get_by_id(self, user_id):
        """
        Get a User by its ID.
        
        :param user_id: The ID of the User to retrieve.
        :return: The User object.
        """
        endpoint = f"{self.endpoint}/{user_id}"
        
        response = self._get(endpoint)
        return User(response) if response else None
    
    def get_many(self):
        """
        Get many users.
        :return: A list of User objects.
        """

        user_list = []
        endpoint = self.endpoint
        params = {}
        
        response = self._get(endpoint, params=params)
        
        if response:
            for user in response['users']:
                try:
                    user = self.get_by_id(user['id'])
                    if user:
                        user_list.append(User(user))
                except Exception as e:
                    print(f"Error creating User object: {e}")
        
        return user_list