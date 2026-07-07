from __future__ import annotations
from shippingboapy.resources.base_resource import Gettable, Listable
from shippingboapy.models.user import User


class UserResource(Gettable[User], Listable[User]):
    _path = "users"
    _model = User