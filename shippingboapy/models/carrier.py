from pydantic import BaseModel, Field
from typing import Optional

class Carrier(BaseModel):
    generic_name: Optional[str] = Field(None, alias="generic_name", description="The generic name of the carrier.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the carrier.")
    name: Optional[str] = Field(None, alias="name", description="The name of the carrier.")
    tracking_url: Optional[str] = Field(None, alias="tracking_url", description="The tracking URL template for the carrier, where {tracking_number} can be replaced with the actual tracking number.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }