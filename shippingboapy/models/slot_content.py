from pydantic import BaseModel, Field
from typing import List, Optional, Any

class UnitVariation(BaseModel):
    product_logistic_unit_id: int = Field(..., description="The ID of the product's logistic unit.")
    quantity: float = Field(..., description="The quantity of the product in the logistic unit.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class SlotContentCreate(BaseModel):
    product_ref: str = Field(..., description="The reference of the product to be added to the slot.")
    product_id: str = Field(..., description="The ID of the product to be added to the slot.")
    warehouse_slot_name: str = Field(..., description="The name of the warehouse slot where the product will be added.")
    warehouse_slot_id: str = Field(..., description="The ID of the warehouse slot where the product will be added.")
    stock: float = Field(..., description="The stock quantity of the product to be added to the slot.")
    batch_number: str = Field(..., description="The batch number of the product to be added to the slot.")
    slot_tag: str = Field(..., description="The tag associated with the slot content.")
    unit_variations: Optional[List[UnitVariation]] = Field(None, description="A list of unit variations for the product in the slot.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class SlotContent(BaseModel):
    batch_number: str = Field(..., description="The batch number of the product in the slot.")
    created_at: str = Field(..., description="The timestamp when the slot content was created.")
    id: int = Field(..., description="The unique identifier for the slot content.")
    product_id: str = Field(..., description="The ID of the product in the slot.")
    product_ref: str = Field(..., description="The reference of the product in the slot")
    product_title: str = Field(..., description="The title of the product in the slot.")
    product_user_ref: str = Field(..., description="The user reference of the product in the slot.")
    stock: int = Field(..., description="The stock quantity of the product in the slot.")
    stored_serial_numbers: List[Any] = Field(..., description="A list of stored serial numbers for the product in the slot.")
    updated_at: str = Field(..., description="The timestamp when the slot content was last updated.")
    warehouse_slot_id: int = Field(..., description="The ID of the warehouse slot where the product is stored.")
    warehouse_slot_name: str = Field(..., description="The name of the warehouse slot where the product is stored.")
    total_reserved_stock: int = Field(..., description="The total reserved stock quantity of the product in the slot.")