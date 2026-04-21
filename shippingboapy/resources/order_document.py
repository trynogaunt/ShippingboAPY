from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.order_document import OrderDocument, OrderDocumentCreate
if TYPE_CHECKING:
    from shippingboapy.client import Client
    
class OrderDocumentResource:
    def __init__(self, client: Client):
        self.client = client
    
    async def get(self, document_id: str, **kwargs) -> OrderDocument:
        """
        Get the details of a specific order document by its ID.

        Args:
            document_id (str): The unique identifier of the order document to retrieve.

        Returns:
            OrderDocument: An OrderDocument object representing the details of the specified order document.
        """
        
        data = await self.client._request("GET", f"/order_documents/{document_id}", **kwargs)
        
        if data is None:
            return None
        
        return OrderDocument(**data)
    
    async def get_file(self, document_id: str, **kwargs) -> bytes:
        """
        Get the file content of a specific order document by its ID.

        Args:
            document_id (str): The unique identifier of the order document to retrieve.

        Returns:
            bytes: The binary content of the order document file.
        """
        
        data = await self.client._download("GET", f"/order_documents/{document_id}/file", **kwargs)
        
        if data is None:
            return None
        
        return data
    
    async def create(self, order_document_create: OrderDocumentCreate, **kwargs) -> OrderDocument:
        """
        Create a new order document for a specific order.

        Args:
            order_document_create (OrderDocumentCreate): An OrderDocumentCreate object containing the details of the order document to create.
            
        Returns:
            OrderDocument: An OrderDocument object representing the details of the created order document.
        """
        data = await self.client._request("POST", "/order_documents", json=order_document_create.model_dump(exclude_none=True, by_alias=True), **kwargs)
        
        if data is None:
            return None
        
        return OrderDocument(**data)