from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class ProductStocksInformations(BaseModel):
    available_stock: int = Field(..., description="The available stock for the product.")
    created_at: str = Field(..., description="The date and time when the stock information was created.")
    updated_at: str = Field(..., description="The date and time when the stock information was last updated.")
    id : int = Field(..., description="The unique identifier for the stock information.")
    picked_stock: int = Field(..., description="The stock that has been picked for orders.")
    reserved_stock: int = Field(..., description="The stock that has been reserved for orders.")
    stock_in_refill: int = Field(..., description="The stock that is currently being refilled.")
    stock_in_slots: int = Field(..., description="The stock that is currently in slots.")
    stock_in_transition: int = Field(..., description="The stock that is currently in transition.")
    theorical_physical_stock: int | None = Field(..., description="The theoretical physical stock for the product. Can be null if the product is stored in a WarehouseSlot. This value is computed from the available stock and the non-shipped orders (stock + non-shipped orders product quantities)")

class OrderItemProductMapping(BaseModel):
    id: int = Field(..., description="The unique identifier for the order item product mapping.")
    matched_quantity: str = Field(..., description="The quantity of the product that has been matched to the order item.")
    order_item_field: str = Field(..., description="The field of the order item that is mapped to the product, always product ref.")
    order_item_value: str = Field(..., description="The value of the order item field that is mapped to the product, the additional reference you want to map.")
    product_field: str = Field(..., description="The field of the product that is mapped to the order item, always id.")
    product_value: str = Field(..., description="The value of the product field that is mapped to the order item, the Shippingbo id of the corresponding product.")

class KitComponent(BaseModel):
    id: int = Field(..., description="The unique identifier for the kit component.")
    quantity: int = Field(..., description="The quantity of the component in the kit.")
    kit_product_id: int = Field(..., description="The unique identifier for the kit product.")
    product_id: int = Field(..., description="The unique identifier for the product that is a component of the kit.")
    kit_stock_rule: Optional[str] = Field(..., description="How kit and their components stocks interact with each other. Can be: null: no interaction , 'kit_supply': the kit stock feeds the components stock") 

class PackComponent(BaseModel):
    component_product_id: int = Field(..., description="The unique identifier for the product that is a component of the pack.")
    quantity: int = Field(..., description="The quantity of the component in the pack.")
    id: int = Field(..., description="The unique identifier for the pack component.")
    pack_product_id: int = Field(..., description="The unique identifier for the pack product.")
    
class ProductAdditionalField(BaseModel):
    created_at: str = Field(..., description="The date and time when the additional field was created.")
    id: int = Field(..., description="The unique identifier for the additional field.")
    key: str = Field(..., description="The key of the additional field.")
    product_id: int = Field(..., description="The unique identifier for the product associated with the additional field.")
    updated_at: str = Field(..., description="The date and time when the additional field was last updated.")
    value: str = Field(..., description="The value of the additional field.")

class ProductAdditionalFieldToAdd(BaseModel):
    key: str = Field(..., description="The key of the additional field.")
    value: str = Field(..., description="The value of the additional field.")

class ProductBarcodeToAdd(BaseModel):
    key: str = Field(..., description="The key of the barcode, can be 'ean13', 'upc' or 'isbn'")
    value: str = Field(..., description="The value of the barcode")

class ProductInstructionsFile(BaseModel):
    id: int = Field(..., description="The unique identifier for the product instructions file.")
    product_id: int = Field(..., description="The unique identifier for the product associated with the instructions file.")
    file_url: str = Field(..., description="The URL of the product instructions file.")
    language: str = Field(..., description="The language of the product instructions file.")

class Product(BaseModel):
    additonal_reference: Optional[List[OrderItemProductMapping]] = Field(..., description="The additional reference for the product.")
    ean13: Optional[str] = Field(..., description="The EAN13 code for the product.")
    eco_tax_cents : Optional[int] = Field(..., description="The eco tax in cents for the product.")
    eco_tax_currency: Optional[str] = Field(..., description="The currency for the eco tax.")
    height: Optional[int] = Field(..., description="The height of the product in millimeters.")
    hs_code: Optional[str] = Field(..., description="The HS code for the product, mandatory for CN23 generation.")
    id: Optional[int] = Field(..., description="The unique identifier for the product.")
    kit_product_ids: Optional[List[int]] = Field(..., description="The list of ids of linked product kits")
    is_pack: Optional[bool] = Field(..., description="Whether the product is a pack or not.")
    kit_components: Optional[List[KitComponent]] = Field(..., description="Describe a kit component. Only available if kitting is enabled on your account")
    length: Optional[int] = Field(..., description="The length of the product in millimeters.")
    location: Optional[str] = Field(..., description="Can be the location of the product in your warehouse")
    other_ref1: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref2: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref3: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref4: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref5: Optional[str] = Field(..., description="An additional reference for the product")
    other_ref6: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref7: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref8: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref9: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref10: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref11: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref12: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref13: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref14: Optional[str] = Field(..., description="An additional reference for the product.")
    other_ref15: Optional[str] = Field(..., description="An additional reference for the product.")
    picture_url: Optional[str] = Field(..., description="The URL of the product picture.")
    pack_components: Optional[List[PackComponent]] = Field(..., description="The list of components in the pack.")
    pack_product_ids: Optional[List[int]] = Field(..., description="The list of ids of linked product packs")
    product_additional_fields: Optional[List[ProductAdditionalField]] = Field(..., description="The list of additional fields for the product.")
    product_instructions_files: Optional[List[ProductInstructionsFile]] = Field(..., description="The list of instructions files for the product.")
    reseller_product_ids: Optional[List[int]] = Field(..., description="This a reference to the reseller products, you can request each of them and look at the physical stock and available stock if you need the information")
    source: Optional[str]  = Field(..., description="The source of the product, this is where the product comes from")
    source_ref: Optional[str] = Field(..., description="The reference on the source")
    stock: Optional[int] = Field(..., description="The stock of the product, this is the total stock of the product in all your warehouses, it is the sum of the available stock and the non-shipped orders product quantities")
    stock_volume_in_m3: Optional[float] = Field(..., description="unit_volume * stock / 10^9")
    supplier: Optional[str] = Field(..., description="The supplier of the product")
    supplier_product_ids: Optional[List[int]] = Field(..., description="This a reference to the supplier products, you can request each of them and look at the physical stock and available stock if you need the information")
    tax_rate: Optional[float] = Field(..., description="The tax rate for the product, in percentage", gt=-1000000000000000)
    title: Optional[str] = Field(..., description="The title of the product.")
    total_physical_stock: Optional[int] = Field(..., description="Only for OMS: total physical stock computed from suppliers")
    unit_volume: Optional[int] = Field(..., description="The unit volume of the product in cubic millimeters, height * length * width")
    user_ref: str = Field(..., description="The main reference of the product, usually useful to match product reference if orders")
    weight: Optional[int] = Field(..., description="The weight of the product in grams.")
    width: Optional[int] = Field(..., description="The width of the product in millimeters.")
    
    @field_validator("stock_volume_in_m3", mode="before")
    @classmethod
    def round_to_2_decimal(cls, v, values):
        if v is not None:
            return round(v, 2)
        return v
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True,
    }
    
class ProductSummary(BaseModel):
    additonal_references: Optional[List[OrderItemProductMapping]] = Field(None, description="The additional reference for the product.")
    ean13: Optional[str] = Field(None, description="The EAN13 code for the product.")
    eco_tax_cents : Optional[int] = Field(None, description="The eco tax in cents for the product.")
    eco_tax_currency: Optional[str] = Field(None, description="The currency for the eco tax.")
    height: Optional[int] = Field(None, description="The height of the product in millimeters.")
    hs_code: Optional[str] = Field(None, description="The HS code for the product, mandatory for CN23 generation.")
    id: Optional[int] = Field(None, description="The unique identifier for the product.")
    kit_product_ids: Optional[List[int]] = Field(None, description="The list of ids of linked product kits")
    is_pack: Optional[bool] = Field(None, description="Whether the product is a pack or not.")
    kit_components: Optional[List[KitComponent]] = Field(None, description="Describe a kit component. Only available if kitting is enabled on your account")
    length: Optional[int] = Field(None, description="The length of the product in millimeters.")
    location: Optional[str] = Field(None, description="Can be the location of the product in your warehouse")
    other_ref1: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref2: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref3: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref4: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref5: Optional[str] = Field(None, description="An additional reference for the product")
    other_ref6: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref7: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref8: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref9: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref10: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref11: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref12: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref13: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref14: Optional[str] = Field(None, description="An additional reference for the product.")
    other_ref15: Optional[str] = Field(None, description="An additional reference for the product.")
    picture_url: Optional[str] = Field(None, description="The URL of the product picture.")
    pack_components: Optional[List[PackComponent]] = Field(None, description="The list of components in the pack.")
    pack_product_ids: Optional[List[int]] = Field(None, description="The list of ids of linked product packs")
    product_additional_fields: Optional[List[ProductAdditionalField]] = Field(None, description="The list of additional fields for the product.")
    product_instructions_files: Optional[List[ProductInstructionsFile]] = Field(None, description="The list of instructions files for the product.")
    reseller_product_ids: Optional[List[int]] = Field(None, description="This a reference to the reseller products, you can request each of them and look at the physical stock and available stock if you need the information")
    source: Optional[str]  = Field(None, description="The source of the product, this is where the product comes from")
    source_ref: Optional[str] = Field(None, description="The reference on the source")
    stock: Optional[int] = Field(None, description="The stock of the product, this is the total stock of the product in all your warehouses, it is the sum of the available stock and the non-shipped orders product quantities")
    stock_volume_in_m3: Optional[float] = Field(None, description="unit_volume * stock / 10^9")
    supplier: Optional[str] = Field(None, description="The supplier of the product")
    supplier_product_ids: Optional[List[int]] = Field(None, description="This a reference to the supplier products, you can request each of them and look at the physical stock and available stock if you need the information")
    tax_rate: Optional[float] = Field(None, description="The tax rate for the product, in percentage", gt=-1000000000000000000)
    title: Optional[str] = Field(None, description="The title of the product.")
    unit_volume: Optional[int] = Field(None, description="The unit volume of the product in cubic millimeters, height * length * width")
    user_ref: str = Field(..., description="The main reference of the product, usually useful to match product reference if orders")
    weight: Optional[int] = Field(None, description="The weight of the product in grams.")
    width: Optional[int] = Field(None, description="The width of the product in millimeters.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True,
    }
    
    @field_validator("stock_volume_in_m3", mode="before")
    @classmethod
    def round_to_2_decimal(cls, v, values):
        if v is not None:
            return round(v, 2)
        return v
    
class ProductCreate(BaseModel):
    ean13: Optional[str] = Field(None, description="The EAN13 code for the product.")
    height: Optional[int] = Field(None, description="The height of the product in millimeters.")
    hs_code: Optional[str] = Field(None, description="The HS code for the product, mandatory for CN23 generation.")
    is_pack: Optional[bool] = Field(None, description="Whether the product is a pack or not.")
    length: Optional[int] = Field(None, description="The length of the product in millimeters.")
    location: Optional[str] = Field(None, description="Can be the location of the product in your warehouse")
    picture_url: Optional[str] = Field(None, description="The URL of the product picture.")
    stock: Optional[int] = Field(None, description="The stock of the product, this is the total stock of the product in all your warehouses, it is the sum of the available stock and the non-shipped orders product quantities")
    supplier: Optional[str] = Field(None, description="The supplier of the product")
    title: Optional[str] = Field(None, description="The title of the product.")
    total_physical_stock: Optional[int] = Field(None, description="Only for OMS: total physical stock computed from suppliers")
    user_ref: str = Field(..., description="The main reference of the product, usually useful to match product reference if orders")
    weight: Optional[int] = Field(None, description="The weight of the product in grams.")
    width: Optional[int] = Field(None, description="The width of the product in millimeters.")
    product_additional_fields_to_add: Optional[List[ProductAdditionalFieldToAdd]] = Field(None, description="The list of additional fields for the product.")
    product_barcodes_attributes: Optional[List[ProductBarcodeToAdd]] = Field(None, description="The list of barcodes for the product.")