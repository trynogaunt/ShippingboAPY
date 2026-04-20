from pydantic import BaseModel, Field
from typing import Optional, List

class OrderDocument(BaseModel):
    error_message: Optional[str] = Field(None, alias="error_message", description="The error message associated with the order document, if applicable.")
    id: Optional[str] = Field(..., alias="id", description="The unique identifier of the order document.")
    package_ids: Optional[List[int]] = Field(None, alias="package_ids", description="The list of package IDs associated with the order document.")
    type: Optional[str] = Field(None, alias="type", description="The type of the order document (e.g., invoice, packing slip).")