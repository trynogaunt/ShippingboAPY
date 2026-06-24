from pydantic import BaseModel, Field
from typing import Optional, List

class PackageObject(BaseModel):
    package_id: int = Field(..., alias="package_id", description="The unique identifier of the package associated with the pallet.")
    order_id: int = Field(..., alias="order_id", description="The unique identifier of the order associated with the package.")
    sscc: Optional[str] = Field(None, alias="sscc", description="The Serial Shipping Container Code (SSCC) of the package associated with the pallet.")
    state: str = Field(..., alias="state", description="The current state of the package associated with the pallet.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class Pallet(BaseModel):
    id: int = Field(..., alias="id", description="The unique identifier of the pallet.")
    label_ref: str = Field(..., alias="label_ref", description="The reference of the label associated with the pallet.")
    state: str = Field(..., alias="state", description="The current state of the pallet.")
    created_at: str = Field(..., alias="created_at", description="The date and time when the pallet was created.")
    updated_at: str = Field(..., alias="updated_at", description="The date and time when the pallet was last updated.")
    handed_to_carrier_at: Optional[str] = Field(None, alias="handed_to_carrier_at", description="The date and time when the pallet was handed to the carrier.")
    label_credential_id: Optional[str] = Field(None, alias="label_credential_id", description="The unique identifier of the label credential associated with the pallet.")
    carrier_name: Optional[str] = Field(None, alias="carrier_name", description="The name of the carrier associated with the pallet.")
    packages: List[PackageObject] = Field(..., alias="packages", description="A list of package objects associated with the pallet.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }