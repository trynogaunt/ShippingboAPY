from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Literal, Any

class Orderitems(BaseModel):
    item_quantity: int = Field(..., description="The quantity of the item in the order.")
    order_item_id: int = Field(..., description="The ID of the order item.")

class SerialNumbers(BaseModel):
    order_item_id: int = Field(..., description="The ID of the order item associated with the serial number.")
    number: str = Field(..., description="The serial number of the item.")

class Shipment(BaseModel):
    carrier_id: int = Field(..., description="The ID of the carrier for the shipment.")
    order_id: int = Field(..., description="The ID of the order associated with the shipment.")
    order_items: List[Orderitems] = Field(..., description="A list of order items included in the shipment.")
    shipping_method_id: int = Field(..., description="The ID of the shipping method for the shipment.")
    shipping_ref: str = Field(..., description="The shipping reference for the shipment.")
    tracking_url: str = Field(..., description="The tracking URL for the shipment.")
    ship_order: Optional[bool] = Field(None, description="Indicates whether the order should be shipped.")
    total_weight: Optional[float] = Field(None, description="The total weight of the shipment.")
    serial_numbers: Optional[List[SerialNumbers]] = Field(None, description="A list of serial numbers associated with the shipment.")