from pydantic import BaseModel, Field
from typing import Optional, List, Any, Literal

class OrderDocument(BaseModel):
    error_message: Optional[str] = Field(None, alias="error_message", description="The error message associated with the order document, if applicable.")
    id: Optional[str] = Field(..., alias="id", description="The unique identifier of the order document.")
    package_ids: Optional[List[int]] = Field(None, alias="package_ids", description="The list of package IDs associated with the order document.")
    type: Optional[str] = Field(None, alias="type", description="The type of the order document (e.g., invoice, packing slip).")

    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }
class OrderDocumentCreate(BaseModel):
    document_type: Optional[str] = Field(..., alias="document_type", description="The type of the order document to create (e.g., invoice, packing slip).")
    language: str = Field(None, alias="language", description="The language to use for the order document, if applicable.")
    order_id: int = Field(None, alias="order_id", description="The unique identifier of the order for which to create the document.")
    print_trigger: Any = Field(None, alias="print_trigger", description="The print trigger to use for the order document, if applicable.")
    duplicate_on_partial_orders: bool = Field(False, alias="duplicate_on_partial_orders", description="Whether to duplicate the order document on partial orders, if applicable.")
    type: Literal["OrderDocument::AdditionalFile", "OrderDocument::ExternalInvoice"] = Field(..., alias="type", description="The type of the order document to create (e.g., invoice, packing slip).")
    uploaded_file_id: int = Field(None, alias="uploaded_file_id", description="The unique identifier of the uploaded file to associate with the order document, if applicable.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }