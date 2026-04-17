from pydantic import BaseModel, Field
from typing import Optional

class OrderTag(BaseModel):
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the order tag.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the tag.")
    value: Optional[str] = Field(None, alias="value", description="The value of the order tag.")

    model_config = {
         "extra": "forbid",
         "validate_by_name": True,
         "validate_assignment": True
     }

class OrderTagCreate(BaseModel):
    order_id: int = Field(..., alias="order_id", description="The unique identifier of the order associated with the tag.")
    value: str = Field(..., alias="value", description="The value of the order tag to create.")

    model_config = {
         "extra": "forbid",
         "validate_by_name": True,
         "validate_assignment": True
     }