import httpx
from shippingboapy.config import ShippingBoConfig
from shippingboapy.auth import TokenData, get_token, refresh_token
import asyncio
from shippingboapy.exceptions import BadRequestError, AuthenticationError, TokenRefreshError, UnexpectedError, ForbiddenError, NotFoundError, ServerError
from shippingboapy.resources.product import ProductResource
from shippingboapy.resources.order import OrderResource
from shippingboapy.resources.order_tag import OrderTagResource
from shippingboapy.resources.pack_component import PackComponentResource
from shippingboapy.resources.package import PackageResource
from shippingboapy.resources.order_document import OrderDocumentResource
from shippingboapy.resources.address_label import AddressLabelResource
from shippingboapy.resources.order_dispatch import OrderDispatchResource
from shippingboapy.resources.order_event import OrderEventResource
from shippingboapy.resources.address_label_summaries import AddressLabelSummariesResource
from shippingboapy.resources.address_label_config import AddressLabelConfigResource
from shippingboapy.resources.address import AddressResource
from shippingboapy.resources.background_job import BackgroundJobResource
from shippingboapy.resources.carrier import CarrierResource
from shippingboapy.resources.client_order_origin import ClientOrderOriginResource
from shippingboapy.resources.client_order_source import ClientOrderSourceResource
from shippingboapy.resources.dangerous_good_product_informations import DangerousGoodProductInformationResource
from shippingboapy.resources.kit_component import KitComponentResource
from shippingboapy.resources.logistician_service_config import LogisticianServiceConfigResource

from typing import Callable, Awaitable, Any, Protocol

class OnTokenRefreshCallback(Protocol):
    async def __call__(self, token_data: TokenData) -> None: ...
    
class RetryableRequest(Protocol):
    async def __call__(self, _retry: int = 0, **kwargs: Any) -> httpx.Response: ...

class Client:
    def __init__(self, access_token: str  = "", 
                 refresh_token: str = "",
                 app_id: str = "",
                 api_version: str  = "",
                 client_id: str = "",
                 client_secret: str  = "",
                 on_token_refresh: OnTokenRefreshCallback | None = None):
        
        if not app_id:
            raise AuthenticationError("app_id is required")
        if not api_version:
            raise AuthenticationError("api_version is required")
        if not client_id:
            raise AuthenticationError("client_id is required")
        if not client_secret:
            raise AuthenticationError("client_secret is required")
        
        self.on_token_refresh: Callable[[TokenData], Awaitable[None]] | None = on_token_refresh
        
        self.config = ShippingBoConfig(
            app_id=app_id,
            api_version=api_version,
            client_id=client_id,
            client_secret=client_secret
        )
        
        self.token: TokenData | None = TokenData(
            access_token=str(access_token),
            refresh_token=str(refresh_token),
            token_type= "Bearer",
            expires_in=3600,
            scope="",
            created_at = None
        )
        self.session = httpx.AsyncClient(timeout=self.config.timeout)
        
        
        self.products = ProductResource(self)
        self.orders = OrderResource(self)
        self.order_tags = OrderTagResource(self)
        self.pack_components = PackComponentResource(self)
        self.packages = PackageResource(self)
        self.order_documents = OrderDocumentResource(self)
        self.address_labels = AddressLabelResource(self)
        self.order_dispatches = OrderDispatchResource(self)
        self.order_events = OrderEventResource(self)
        self.address_label_summaries = AddressLabelSummariesResource(self)
        self.address_label_configs = AddressLabelConfigResource(self)
        self.address = AddressResource(self)
        self.background_jobs = BackgroundJobResource(self)
        self.carrier = CarrierResource(self)
        self.client_order_origin = ClientOrderOriginResource(self)
        self.client_order_source = ClientOrderSourceResource(self)
        self.dangerous_good_product_informations = DangerousGoodProductInformationResource(self)
        self.kit_components = KitComponentResource(self)
        self.logistician_service_configs = LogisticianServiceConfigResource(self)
        
    def _set_token(self, token_data: TokenData):
        self.token = token_data
    
    def set_config(self, timeout: int | None = None, max_retries: int | None = None, retry_backoff_factor: float | None = None, redirect_uri: str | None = None, auth_url: str | None = None, api_url: str | None = None):
        if timeout is not None:
            self.config.timeout = timeout
            self.session.timeout = timeout
        if max_retries is not None:
            self.config.max_retries = max_retries
        if retry_backoff_factor is not None:
            self.config.retry_backoff_factor = retry_backoff_factor
        if redirect_uri is not None:
            self.config.redirect_uri = redirect_uri
        if auth_url is not None:
            self.config.auth_url = auth_url
        if api_url is not None:
            self.config.api_url = api_url
    
    async def _process_response(self, response: httpx.Response) -> httpx.Response:
        match response.status_code:
            case s if 200 <= s < 300:
                return response
            case 400:
                raise BadRequestError(response.status_code, f"Bad request: {response.text}")
            case 401:
                raise AuthenticationError(response.status_code, f"Authentication failed: {response.text}")
            case 403:
                raise ForbiddenError(response.status_code, f"Forbidden access: {response.text}")
            case 404:
                raise NotFoundError(response.status_code, f"Resource not found: {response.text}")
            case 422:
                raise BadRequestError(response.status_code, f"Unprocessable entity: {response.text}")
            case s if s >= 500:
                raise ServerError(response.status_code, f"Server error after {self.config.max_retries} retries: {response.text}")
            case _:
                raise UnexpectedError(response.status_code, f"Unexpected error: {response.text}")
            
    
    async def _raw_request(self, method: str, endpoint: str, params: dict[str, Any] | None = None, **kwargs: Any) -> httpx.Response:
        
        if self.token is None:
            raise AuthenticationError("Access token is missing. Please authenticate first.")
        
        url = f"{self.config.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        extra_headers = kwargs.pop("headers", {})
        
        auth_attempts : int = 0
        server_attempts : int = 0
        
        while True:
            
            headers = {
                "Authorization": f"Bearer {self.token.access_token}",
                "X-API-VERSION": self.config.api_version,
                "X-API-APP-ID": self.config.app_id,
                "Accept": "application/json",  
                **extra_headers
            }
        
            response = await self.session.request(method, url, headers=headers, params=params, **kwargs)

            if response.status_code == 401 and auth_attempts == 0:
                auth_attempts += 1
                try:
                    new_token : TokenData | None = await refresh_token(self.token.refresh_token, self.session, self.config, on_refresh=self.on_token_refresh)
                    self._set_token(new_token)
                    continue 
                except Exception as e:
                    raise TokenRefreshError(f"Failed to refresh token: {str(e)}") from e
                
            if response.status_code >= 500 and server_attempts < self.config.max_retries:
                server_attempts += 1
                await asyncio.sleep(self.config.retry_backoff_factor * (2 ** (server_attempts - 1)))
                continue
            
            return await self._process_response(response)

    async def _request(self, method: str, endpoint: str, params: dict[str, Any] | None = None, **kwargs: Any) -> Any:
        response = await self._raw_request(method, endpoint, params, **kwargs)
        if not response.content:
            return {}
        return response.json()


    async def _download(self, method: str, endpoint: str, params: dict[str, Any] | None = None, **kwargs: Any) -> bytes:
        kwargs.setdefault("headers", {})["Accept"] = "application/pdf, application/octet-stream, */*"
        response = await self._raw_request(method, endpoint, params, **kwargs)
        return response.content 
       
    
    @classmethod
    async def from_auth_code(cls, auth_code: str, app_id: str, api_version: str, client_id: str, client_secret: str, redirect_uri: str | None = None, headers: dict[str, Any] | None = None):
        config_dict : dict[str, Any] = {
            "app_id": app_id,
            "api_version": api_version,
            "client_id": client_id,
            "client_secret": client_secret
        }
        
        if redirect_uri is not None:
            config_dict["redirect_uri"] = redirect_uri
            
        config = ShippingBoConfig(**config_dict)
        async with httpx.AsyncClient(timeout=config.timeout) as session:
            token = await get_token(auth_code, session, config, headers)
            
        if token is None:
            raise AuthenticationError("Failed to obtain access token with the provided authorization code.")
            
        cls = cls(
            access_token=token.access_token,
            refresh_token=token.refresh_token,
            app_id=config.app_id,
            api_version=config.api_version,
            client_id=config.client_id,
            client_secret=config.client_secret
        )
        cls._set_token(token)
        return cls
    
    async def close(self):
        await self.session.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self):
        await self.close()

