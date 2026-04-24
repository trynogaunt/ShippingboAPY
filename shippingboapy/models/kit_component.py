from pydantic import BaseModel, Field
from typing import Optional

class KitComponentCreate(BaseModel):
    kit_product_id: int = Field(..., description="ID of the kit product")
    component_product_id: int = Field(..., description="ID of the component product")
    quantity: int = Field(..., description="Quantity of the component in the kit")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class KitComponent(KitComponentCreate):
    id: int = Field(..., description="ID of the kit component")
    kit_stock_rule: Optional[str] = Field(None, description="Stock rule for the kit component")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }
    
class KitComponentUpdate(BaseModel):
    quantity: int = Field(None, description="Quantity of the component in the kit")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }