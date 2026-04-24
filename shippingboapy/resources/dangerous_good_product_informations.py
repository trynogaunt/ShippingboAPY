from __future__ import annotations
from typing import TYPE_CHECKING, List
from shippingboapy.models.dangerous_good_product_information import DangerousGoodProductInformation, DangerousGoodProductInformationCreate, DangerousGoodProductInformationUpdate
from shippingboapy.models.filter import Filter, Operator
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class DangerousGoodProductInformationResource:
    def __init__(self, client: Client):
        self.client = client

    async def get(self, dangerous_good_product_information_id: int) -> DangerousGoodProductInformation:
        """
        Retrieve a specific dangerous good product information by its unique identifier.

        Args:
            dangerous_good_product_information_id (int): The unique identifier of the dangerous good product information to retrieve.

        Returns:
            DangerousGoodProductInformation: The dangerous good product information object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the DangerousGoodProductInformation model.
        """
        data = await self.client._request("GET", f"/dangerous_goods_product_informations/{dangerous_good_product_information_id}")
        
        if data is None:
            return None

        return DangerousGoodProductInformation(**data)  
    
    async def list(self, search: List[tuple[str, str, str]] = None) -> list[DangerousGoodProductInformation]:
        """
        Retrieve a list of dangerous good product informations based on search criteria.

        Args:
            search (List[tuple[str, str, str]]): A list of search criteria tuples, where each tuple contains a field name, an operator, and a value for filtering the dangerous good product informations.

        Returns:
            list[DangerousGoodProductInformation]: A list of dangerous good product information objects matching the search criteria.
        """
        
        params = {}
        
        if search is not None:
            for item in search:
                if len(item) != 3:
                    raise ValueError(f"Invalid search item: {item}. Each search item must be a tuple of (field, operator, value).")
                
                filter_obj = Filter(field=item[0], operator=Operator(item[1]), value=item[2])
                params.setdefault("search", []).append(filter_obj.json(by_alias=True))
        
        data = await self.client._request("GET", "/dangerous_goods_product_informations", params=params)
        
        if data is None:
            return None

        return [DangerousGoodProductInformation(**item) for item in data]
    
    async def create(self, dangerous_good_product_information_create: DangerousGoodProductInformationCreate) -> DangerousGoodProductInformation:
        """
        Create a new dangerous good product information.

        Args:
            dangerous_good_product_information_create (DangerousGoodProductInformationCreate): An object containing the details of the dangerous good product information to be created.

        Returns:
            DangerousGoodProductInformation: The created dangerous good product information object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the DangerousGoodProductInformation model.
        """
        data = await self.client._request("POST", "/dangerous_goods_product_informations", json=dangerous_good_product_information_create.model_dump(by_alias=True))
        
        if data is None:
            return None

        return DangerousGoodProductInformation(**data)
    
    async def update(self, dangerous_good_product_information_id: int, dangerous_good_product_information_update: DangerousGoodProductInformationUpdate) -> DangerousGoodProductInformation:
        """
        Update an existing dangerous good product information.

        Args:
            dangerous_good_product_information_id (int): The unique identifier of the dangerous good product information to update.
            dangerous_good_product_information_update (DangerousGoodProductInformationUpdate): An object containing the updated details of the dangerous good product information.

        Returns:
            DangerousGoodProductInformation: The updated dangerous good product information object.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
            ValidationError: If the response data cannot be validated against the DangerousGoodProductInformation model.
        """
        data = await self.client._request("PATCH", f"/dangerous_goods_product_informations/{dangerous_good_product_information_id}", json=dangerous_good_product_information_update.model_dump(by_alias=True))
        
        if data is None:
            return None

        return DangerousGoodProductInformation(**data)
    
    async def delete(self, dangerous_good_product_information_id: int) -> bool:
        """
        Delete a specific dangerous good product information by its unique identifier.

        Args:
            dangerous_good_product_information_id (int): The unique identifier of the dangerous good product information to delete.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
        """
        data = await self.client._request("DELETE", f"/dangerous_goods_product_informations/{dangerous_good_product_information_id}")
        
        if data is None:
            return False
        return True