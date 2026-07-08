from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Literal, Any

class ShippingMethod(BaseModel):
    id: int = Field(..., description="The unique identifier for the shipping method.")
    name: str = Field(..., description="The name of the shipping method.")
    carrier_id: int = Field(..., description="The unique identifier for the carrier associated with the shipping method.")