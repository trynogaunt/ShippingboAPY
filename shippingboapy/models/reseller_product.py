from pydantic import BaseModel, Field

class ResellerProduct(BaseModel):
    id: int = Field(..., description="The unique identifier of the reseller product.")
    reseller_id: int = Field(..., description="The unique identifier of the reseller.")
    product_id: int = Field(..., description="The unique identifier of the product.")
    reseller_ref: str = Field(..., description="The reference of the reseller product.")
    active: bool = Field(..., description="Indicates whether the reseller product is active.")
    available_stock: int = Field(..., description="The available stock of the reseller product.")
    physical_stock: int = Field(..., description="The physical stock of the reseller product.")