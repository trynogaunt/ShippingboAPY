from __future__ import annotations
from typing import TYPE_CHECKING
from shippingboapy.models.order_document import OrderDocument
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
        
        data = await self.client._request("GET", f"/order_documents/{document_id}/file", **kwargs)
        
        if data is None:
            return None
        
        return data