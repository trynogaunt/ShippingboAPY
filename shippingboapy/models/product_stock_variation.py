from pydantic import BaseModel, Field
from typing import Optional, Any

class ProductStockVariation(BaseModel):
    batch_number: Optional[str] = Field(None, alias="batch_number", description="The batch number associated with the product stock variation item.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the product stock variation item.")
    last_preparation_day: Optional[str] = Field(None, alias="last_preparation_day", description="The last preparation day for the product stock variation item.")
    origin: Optional[str] = Field(None, alias="origin", description="The origin of the product stock variation item.")
    origin_ref: Optional[str] = Field(None, alias="origin_ref", description="The reference for the origin of the product stock variation item.")
    product_id: Optional[int] = Field(None, alias="product_id", description="The unique identifier of the product associated with the product stock variation item.")
    quantity: Optional[int] = Field(None, alias="quantity", description="The quantity of the product stock variation item.")
    reason: Optional[str] = Field(None, alias="reason", description="The reason for the product stock variation item.")
    reason_ref: Optional[str] = Field(None, alias="reason_ref", description="The reference for the reason of the product stock variation item.")
    serial_number: Optional[str] = Field(None, alias="serial_number", description="The serial number associated with the product stock variation item.")
    
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }
