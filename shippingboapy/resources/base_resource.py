from typing import TypeVar, Generic, ClassVar, cast, TYPE_CHECKING, Optional
from pydantic import BaseModel

if TYPE_CHECKING:
    from shippingboapy.client import Client

from shippingboapy.models.filter import Filter


TRead = TypeVar("TRead", bound=BaseModel)
TUpdate = TypeVar("TUpdate", bound=BaseModel)
TCreate = TypeVar("TCreate", bound=BaseModel)
TSummary = TypeVar("TSummary", bound=BaseModel)

class BaseResource:
    _path: ClassVar[str] 
    _dict_header: ClassVar[str] = []
    _model: ClassVar[type[BaseModel]]
    
    def __init__(self, client: "Client"):
        self.client = client
    
    def _unwrap(self, response: object) -> object:
        
        probable_headers = []
        probable_headers.append(self._dict_header) if self._dict_header else None
        probable_headers.append(self._path)
        single_item_headers = [header[:-1] for header in probable_headers if header.endswith('s')]
        probable_headers.extend(single_item_headers)

        for header in probable_headers:
            if isinstance(response, dict) and header in response:
                return response[header]
            else:
                continue
        return response

class Gettable(BaseResource, Generic[TRead]):
    async def get(self, resource_id: int | str) -> TRead:
        """
        Get a resource by its ID.

        Args:
            resource_id (int | str): The ID of the resource to retrieve.

        Returns:
            TRead: The resource with the specified ID.
        """
        response = await self.client._request("GET", f"{self._path}/{resource_id}")

        if response is None:
            raise ValueError(f"Resource with ID {resource_id} not found.")
        
        response = self._unwrap(response)

        return cast(TRead, self._model.model_validate(response))

class FilterableGettable(Gettable[TRead], Generic[TRead]):
    async def get(self, search: Optional[list[Filter]] = None) -> TRead:
        """
        Get a resource by its ID with optional filtering.

        Args:
            resource_id (int | str): The ID of the resource to retrieve.
            search (list[Filter], optional): A list of Filter objects representing the search criteria.

        Returns:
            TRead: The resource with the specified ID that matches the search criteria.
        """
        params = {}
        
        if search is not None:
            for filter_obj in search:
                key = f"search{filter_obj.to_params()}"
                params[key] = str(filter_obj.value)
        
        response = await self.client._request("GET", f"{self._path}", params=params)

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [cast(TRead, self._model.model_validate(item)) for item in response]

class Listable(BaseResource, Generic[TSummary]):
    _list_model: ClassVar[type[BaseModel]]

    async def list(self) -> list[TSummary]:
        """
        List all resources.

        Returns:
            list[TSummary]: A list of all lightweight resources.
        """
        response = await self.client._request("GET", self._path)

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [cast(TSummary, self._list_model.model_validate(item)) for item in response]

class FilterableListable(Listable[TSummary], Generic[TSummary]):
    async def list(self, search: Optional[list[Filter]] = None) -> list[TSummary]:
        """
        List all resources with optional filtering.

        Args:
            search (list[Filter], optional): A list of Filter objects representing the search criteria.

        Returns:
            list[TSummary]: A list of all lightweight resources that match the search criteria.
        """
        params = {}
        
        if search is not None:
            for filter_obj in search:
                key = f"search{filter_obj.to_params()}"
                params[key] = str(filter_obj.value)
        
        response = await self.client._request("GET", self._path, params=params)

        if response is None:
            return []
        
        response = self._unwrap(response)

        return [cast(TSummary, self._list_model.model_validate(item)) for item in response]

class MandatoryFilterableListable(FilterableListable[TSummary], Generic[TSummary]):
    _mandatory_filter : ClassVar[list[str]] = []

    async def list(self, search: Optional[list[Filter]] = None) -> list[TSummary]:
        """
        List all resources with mandatory filtering.

        Args:
            search (list[Filter]): A list of Filter objects representing the mandatory search criteria, optional to clarify missing mandatory filters.

        Returns:
            list[TSummary]: A list of all lightweight resources that match the mandatory search criteria.
        """
        provided_filters = {filter_obj.field for filter_obj in search} if search is not None else set()
        missing_filters = [f for f in self._mandatory_filter if f not in provided_filters]
        if missing_filters:
            raise ValueError(f"Filters for '{missing_filters}' must be provided for mandatory filtering.")

        return await super().list(search=search)

class Creatable(BaseResource, Generic[TCreate, TRead]):
    async def create(self, data: dict | TCreate) -> TRead:
        """
        Create a new resource.

        Args:
            data (TCreate): The data for the new resource.

        Returns:
            TRead: The created resource.
        """
        if isinstance(data, dict):
            data = cast(TCreate, self._model.model_validate(data))
       
        response = await self.client._request("POST", self._path, json=data.model_dump(by_alias=True, exclude_none=True))

        if response is None:
            raise ValueError("Failed to create resource.")

        response = self._unwrap(response)

        return cast(TRead, self._model.model_validate(response))

class Updatable(BaseResource, Generic[TUpdate, TRead]):
    async def update(self, resource_id: int | str, data: dict | TUpdate) -> TRead:
        """
        Update an existing resource.

        Args:
            resource_id (int | str): The ID of the resource to update.
            data (TUpdate): The updated data for the resource.

        Returns:
            TRead: The updated resource.
        """

        if isinstance(data, dict):
            data = cast(TUpdate, self._model.model_validate(data))
       
        response = await self.client._request("PATCH", f"{self._path}/{resource_id}", json=data.model_dump(by_alias=True, exclude_none=True))     

        if response is None:
            raise ValueError(f"Resource with ID {resource_id} not found or could not be updated.")
        
        response = self._unwrap(response)

        return cast(TRead, self._model.model_validate(response))
        
class Deletable(BaseResource):
    async def delete(self, resource_id: int | str) -> None:
        """
        Delete a resource by its ID.

        Args:
            resource_id (int | str): The ID of the resource to delete.
        """
        await self.client._request("DELETE", f"{self._path}/{resource_id}")

class Downloadable(BaseResource):
    async def get_file(self, resource_id: int | str) -> bytes:
        """
        Download a resource by its ID.

        Args:
            resource_id (int | str): The ID of the resource to download.

        Returns:
            bytes: The binary content of the downloaded resource.
        """
        response = await self.client._download("GET", f"{self._path}/{resource_id}/file")

        if response is None:
            raise ValueError(f"Resource with ID {resource_id} not found or could not be downloaded.")

        return response

