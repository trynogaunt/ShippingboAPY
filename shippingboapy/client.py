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
from typing import Callable

class Client:
    def __init__(self, access_token: str | None = None, 
                 refresh_token: str | None = None,
                 app_id: str = "",
                 api_version: str  = "",
                 client_id: str = "",
                 client_secret: str  = "",
                 on_token_refresh: Callable[[str, str], None] | None = None):
        
        if not app_id:
            raise AuthenticationError("app_id is required")
        if not api_version:
            raise AuthenticationError("api_version is required")
        if not client_id:
            raise AuthenticationError("client_id is required")
        if not client_secret:
            raise AuthenticationError("client_secret is required")
        
        self.config = ShippingBoConfig(
            app_id=app_id,
            api_version=api_version,
            client_id=client_id,
            client_secret=client_secret
        )
        self.token: TokenData | None = TokenData(
            access_token=access_token,
            refresh_token=refresh_token,
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
        
    def _set_token(self, token_data: TokenData):
        self.token = token_data
    
    def set_config(self, timeout: int = None, max_retries: int = None, retry_backoff_factor: float = None, redirect_uri: str = None, auth_url: str = None, api_url: str = None):
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
    
    async def _process_response(self, response: httpx.Response, _retry: int = 0, request_func: Callable = None, **kwargs) -> httpx.Response:
        match response.status_code:
            case 200:
                return response
            case 400:
                raise BadRequestError(response.status_code, f"Bad request: {response.text}")
            case 401:
                if _retry == 0 and self.token and self.token.refresh_token and request_func is not None:
                    try:
                        new_token = await refresh_token(self.token.refresh_token, self.session, self.config, on_refresh=self.config.on_token_refresh)
                        self._set_token(new_token)
                        return await request_func(_retry=_retry + 1, **kwargs)
                    except Exception as e:
                        raise TokenRefreshError(response.status_code, f"Token refresh failed: {str(e)}")
                else:
                    raise AuthenticationError(response.status_code, f"Authentication failed: {response.text}")
            case 403:
                raise ForbiddenError(response.status_code, f"Forbidden access: {response.text}")
            case 404:
                raise NotFoundError(response.status_code, f"Resource not found: {response.text}")
            case 422:
                raise BadRequestError(response.status_code, f"Unprocessable entity: {response.text}")
            case _ if response.status_code >= 500:
                if _retry < self.config.max_retries and request_func is not None:
                    backoff_time = self.config.retry_backoff_factor * (2 ** _retry)
                    await asyncio.sleep(backoff_time)
                    return await request_func(_retry=_retry + 1, **kwargs)
                else:
                    raise ServerError(response.status_code, f"Server error after {self.config.max_retries} retries: {response.text}")
            case _:
                raise UnexpectedError(response.status_code, f"Unexpected error: {response.text}")
            
    
    async def _raw_request(self, method: str, endpoint: str, params: dict | None = None,_retry: int = 0,**kwargs,) -> httpx.Response:
        if self.token is None or self.token.access_token is None:
            raise AuthenticationError("Access token is missing. Please authenticate first.")
        
        url = f"{self.config.api_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.token.access_token}",
            "X-API-VERSION": self.config.api_version,
            "X-API-APP-ID": self.config.app_id,
            "Accept": "application/json",  
        }
        headers.update(kwargs.pop("headers", {}))
        
        response = await self.session.request(method, url, headers=headers, params=params, **kwargs)
        
        return await self._process_response(
            response,
            _retry=_retry,
            request_func=lambda **kw: self._raw_request(method, endpoint, params, **kw),
        )


    async def _request(self, method: str, endpoint: str, **kwargs) -> dict | list:
        response = await self._raw_request(method, endpoint, **kwargs)
        if not response.content:
            return {}
        return response.json()


    async def _download(self, method: str, endpoint: str, **kwargs) -> bytes:
        kwargs.setdefault("headers", {})["Accept"] = "application/pdf, application/octet-stream, */*"
        response = await self._raw_request(method, endpoint, **kwargs)
        return response.content 
       
    
    @classmethod
    async def from_auth_code(cls, auth_code: str, app_id: str, api_version: str, client_id: str, client_secret: str, redirect_uri: str | None = None, headers: dict | None = None):
        config = ShippingBoConfig(app_id=app_id, api_version=api_version, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        async with httpx.AsyncClient(timeout=config.timeout) as session:
            token = await get_token(auth_code, session, config, headers)
        
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
    
    async def __aexit__(self,  *args):
        await self.close()

