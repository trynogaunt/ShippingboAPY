from pydantic import BaseModel, Field
from typing import Optional

class AddressLabel(BaseModel):
    address_label_config_id: int = Field(..., alias="address_label_config_id", description="The unique identifier of the address label configuration associated with the address label.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the address label.")
    label_url: Optional[str] = Field(None, alias="label_url", description="The URL of the address label, if applicable.")
    package_id: Optional[int] = Field(None, alias="package_id", description="The unique identifier of the package associated with the address label, if applicable.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }