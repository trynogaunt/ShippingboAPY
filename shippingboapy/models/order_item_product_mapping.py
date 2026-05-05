from pydantic import BaseModel, Field
from typing import Optional

class RequestModel(BaseModel):
    field: str = Field(..., description='description')

class OrderItemProductMappingCreate(BaseModel):
    id: Optional[int] = Field(None, description='ID of the order item product mapping', alias='id')
    matched_quantity: int = Field(..., description='Matched quantity', alias='matched_quantity')
    order_item_field: str = Field(..., description='Order item field', alias='order_item_field')
    order_item_value: str = Field(..., description='Order item value', alias='order_item_value')
    product_field: str = Field(..., description='Product field', alias='product_field')
    product_value: str = Field(..., description='Product value', alias='product_value')
    
    model_config = {
        'allow_population_by_field_name': True,
        'extra': 'forbid',
    }

class OrderItemProductMapping(OrderItemProductMappingCreate):
    pass

    model_config = {
        'allow_population_by_field_name': True,
        'extra': 'forbid',
    }