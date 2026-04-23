from __future__ import annotations
from typing import TYPE_CHECKING, List
from shippingboapy.models.address import Address, AddressCreate, AddressUpdate
from shippingboapy.models.filter import Filter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class AddressResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, id: int) -> Address:
        """
        Retrieve a specific address by its unique identifier.

        Args:
            id (int): The unique identifier of the address to retrieve.

        Returns:
            Address: The address object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the Address model.
        """
        data = await self.client._request("GET", f"/addresses/{id}")
        
        if data is None:
            return None

        return Address(**data)
    
    async def list(self, 
                   limit: int=50, 
                   offset: int=0,
                   search: List[tuple[str, str, str]] = None ) -> list[Address]:
        """
        Retrieve a list of addresses.
        
        Args:
            limit (int, optional): The maximum number of addresses to return. Defaults to 50.
            offset (int, optional): The number of addresses to skip before starting to collect the result set. Defaults to 0.
            search (List[tuple[str, str, str]], optional): A list of search criteria tuples, where each tuple contains a field name, an operator, and a value for filtering the addresses. Defaults to None.
        
        Returns:
            list[Address]: A list of address objects.
        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the Address model.
        """
        
        params = {"limit": limit, 
                  "offset": offset}
        
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
                key = f"search{filter_obj.to_params()}"
                
                if isinstance(item[2], list):
                    for value in item[2]:
                        params.append((key, str(value)))
                    else:
                        params.append((key, str(item[2])))
        
        data = await self.client._request("GET", "/addresses", params=params)
        
        if data is None:
            return None
        return [Address(**item) for item in data.get("addresses", [])]

    async def create(self, address_create: AddressCreate) -> Address:
        """
        Create a new address.

        Args:
            address_create (AddressCreate): The address creation object containing the details of the address to be created.

        Returns:
            Address: The newly created address object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the Address model.
        """
        
        data = await self.client._request("POST", "/addresses", json=address_create.model_dump(by_alias=True))
        
        if data is None:
            return None

        return Address(**data)
    
    async def update(self, id: int, address_update: AddressUpdate) -> Address:
        """
        Update an existing address.

        Args:
            id (int): The unique identifier of the address to update.
            address_update (AddressUpdate): The address update object containing the updated details of the address.

        Returns:
            Address: The updated address object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the Address model.
        """
        
        data = await self.client._request("PATCH", f"/addresses/{id}", json=address_update.model_dump(by_alias=True))
        
        if data is None:
            return None

        return Address(**data)