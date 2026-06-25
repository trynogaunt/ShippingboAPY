from pydantic import BaseModel, Field

class Reseller(BaseModel):
    id: int = Field(..., description="The unique identifier of the reseller.")
    name: str = Field(..., description="The name of the reseller.")