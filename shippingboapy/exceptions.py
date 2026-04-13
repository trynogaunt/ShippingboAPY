class ShippingboAPYException(Exception):
    """Base exception for ShippingboAPY."""
    pass

class ValueError(ShippingboAPYException):
    """Raised when an invalid value is provided."""
    pass

class AuthenticationError(ShippingboAPYException):
    """Raised when authentication fails."""
    pass

class TokenExpiredError(AuthenticationError):
    """Raised when the authentication token has expired."""
    pass

class TokenRefreshError(AuthenticationError):
    """Raised when there is an error refreshing the authentication token."""
    pass

class APIRequestError(ShippingboAPYException):
    """Raised when an API request fails."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Request failed with status {status_code}: {message}")
        
class BadRequestError(APIRequestError):
    """Raised when the API request is malformed or contains invalid parameters."""
    pass

class UnauthorizedError(APIRequestError):
    """Raised when the API request is unauthorized."""
    pass

class ForbiddenError(APIRequestError):
    """Raised when the API request is forbidden."""
    pass

class NotFoundError(APIRequestError):
    """Raised when the requested resource is not found."""
    pass

class RateLimitError(APIRequestError):
    """Raised when the API rate limit is exceeded."""
    pass

class ServerError(APIRequestError):
    """Raised when the server encounters an error."""
    pass

class UnexpectedError(APIRequestError):
    """Raised when an unexpected error occurs."""
    pass