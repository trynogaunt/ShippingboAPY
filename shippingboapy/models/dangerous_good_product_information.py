from pydantic import BaseModel, Field
from typing import Optional, Literal, List

class DangerousGoodProductInformationCreate(BaseModel):
    category: str = Field(..., alias="category", description="The category of the dangerous good product.")
    class_code: str = Field(..., alias="class_code", description="The class code of the dangerous good product.")
    coefficient: float = Field(..., alias="coefficient", description="The coefficient of the dangerous good product.")
    dhl_description: Optional[str] = Field(None, alias="dhl_description", description="The DHL description of the dangerous good product.")
    dhl_economy_select_ref: Optional[str] = Field(None, alias="dhl_economy_select_ref", description="The DHL Economy Select reference of the dangerous good product.")
    dhl_ref: Optional[str] = Field(None, alias="dhl_ref", description="The DHL reference of the dangerous good product.")
    environmentally_hazardous: Optional[bool] = Field(None, alias="environmentally_hazardous", description="Indicates whether the dangerous good product is environmentally hazardous.")
    gross_weight: Optional[float] = Field(None, alias="gross_weight", description="The gross weight of the dangerous good product.")
    label_code: str = Field(..., alias="label_code", description="The label code of the dangerous good product.")
    limited_quantity: Optional[bool] = Field(None, alias="limited_quantity", description="Indicates whether the dangerous good product is a limited quantity.")
    onu_code: str = Field(..., alias="onu_code", description="The ONU code of the dangerous good product.")
    onu_description: str = Field(None, alias="onu_description", description="The ONU description of the dangerous good product.")
    package_code_identification: str = Field(None, alias="package_code_identification", description="The package code identification of the dangerous good product.")
    packaging_group: str = Field(..., alias="packaging_group", description="The packaging group of the dangerous good product.")
    packaging_type: str = Field(..., alias="packaging_type", description="The packaging type of the dangerous good product.")
    product_description: str = Field(..., alias="product_description", description="The description of the dangerous good product.")
    product_id: float = Field(..., alias="product_id", description="The unique identifier of the dangerous good product.")
    quantity: Optional[float] = Field(None, alias="quantity", description="The quantity of the dangerous good product.")
    tunnel_code: str = Field(..., alias="tunnel_code", description="The tunnel code of the dangerous good product.")
    unit: Literal['KG', 'L'] | str = Field(..., alias="unit", description="The unit of measurement for the quantity of the dangerous good product.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class DangerousGoodProductInformation(DangerousGoodProductInformationCreate):
    id: int = Field(..., alias="id", description="The unique identifier of the dangerous good product information.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }
    
class DangerousGoodProductInformationUpdate(DangerousGoodProductInformationCreate):
    pass

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }