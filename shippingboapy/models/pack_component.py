from pydantic import BaseModel, Field
from typing import Optional

class PackComponentCreate(BaseModel):
    component_product_id: int = Field(..., alias="component_product_id", description="The unique identifier of the product that is a component of the pack.")
    pack_product_id: int = Field(..., alias="pack_product_id", description="The unique identifier of the pack product that contains the component.")
    quantity: int = Field(..., alias="quantity", description="The quantity of the component product in the pack.")
    
    model_config = {
         "extra": "forbid",
         "validate_by_name": True,
         "validate_assignment": True
     }

class PackComponent(PackComponentCreate):
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the pack component.")

    model_config = {
         "extra": "forbid",
         "validate_by_name": True,
         "validate_assignment": True
     }