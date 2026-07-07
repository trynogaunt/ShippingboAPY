from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Listable
from shippingboapy.models.user import User


class UserResource(Gettable[User], Listable[User]):
    """
    Resource class for interacting with the User API endpoints.
    Provides methods to retrieve user information and list users.
    Unusable without Config role, this role isn't documented in the API.
    """
    _path = "users"
    _model = User