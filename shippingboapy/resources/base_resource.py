from typing import TypeVar, Generic, ClassVar, cast
from pydantic import BaseModel

TRead = TypeVar("TRead", bound=BaseModel)
TUpdate = TypeVar("TUpdate", bound=BaseModel)
TCreate = TypeVar("TCreate", bound=BaseModel)
TSummary = TypeVar("TSummary", bound=BaseModel)

class BaseResource:
    _path: ClassVar[str] 
    _model: ClassVar[type[BaseModel]]
    
    def __init__(self, client):
        self.client = client
    
    def _unwrap(self, response: object) -> object:
        if isinstance(response, dict) and self._path in response:
            return response[self._path]
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

class Creatable(BaseResource, Generic[TCreate, TRead]):
    async def create(self, data: TCreate) -> TRead:
        """
        Create a new resource.

        Args:
            data (TCreate): The data for the new resource.

        Returns:
            TRead: The created resource.
        """
        response = await self.client._request("POST", self._path, json=data.model_dump(by_alias=True, exclude_none=True))
        
        if response is None:
            raise ValueError("Failed to create resource.")

        response = self._unwrap(response)

        return cast(TRead, self._model.model_validate(response))

class Updatable(BaseResource, Generic[TUpdate, TRead]):
    async def update(self, resource_id: int | str, data: TUpdate) -> TRead:
        """
        Update an existing resource.

        Args:
            resource_id (int | str): The ID of the resource to update.
            data (TUpdate): The updated data for the resource.

        Returns:
            TRead: The updated resource.
        """
        raise NotImplementedError("The 'update' method must be implemented in the subclass.")

class Deletable(BaseResource):
    async def delete(self, resource_id: int | str) -> None:
        """
        Delete a resource by its ID.

        Args:
            resource_id (int | str): The ID of the resource to delete.
        """
        await self.client._request("DELETE", f"{self._path}/{resource_id}")


