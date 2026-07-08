from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Any
from datetime import datetime, date

class Orderitems(BaseModel):
    item_quantity: int = Field(..., description="The quantity of the item in the order.")
    order_item_id: int = Field(..., description="The ID of the order item.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class SerialNumbers(BaseModel):
    order_item_id: int = Field(..., description="The ID of the order item associated with the serial number.")
    number: str = Field(..., description="The serial number of the item.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class ShipmentCreate(BaseModel):
    carrier_id: int = Field(..., description="The ID of the carrier for the shipment.")
    order_id: int = Field(..., description="The ID of the order associated with the shipment.")
    order_items: List[Orderitems] = Field(..., description="A list of order items included in the shipment.")
    shipping_method_id: int = Field(..., description="The ID of the shipping method for the shipment.")
    shipping_ref: str = Field(..., description="The shipping reference for the shipment.")
    tracking_url: str = Field(..., description="The tracking URL for the shipment.")
    ship_order: Optional[bool] = Field(None, description="Indicates whether the order should be shipped.")
    total_weight: Optional[float] = Field(None, description="The total weight of the shipment.")
    serial_numbers: Optional[List[SerialNumbers]] = Field(None, description="A list of serial numbers associated with the shipment.")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class ItemsShipmentSerialNumber(BaseModel):
    order_item_id: int
    serial_number: str

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class OrderItemShipmentPickingHistory(BaseModel):
    batch_number: str
    id: int
    last_preparation_day: date
    quantity: int = Field(ge=1)

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class OrderItemsShipment(BaseModel):
    item_quantity: int
    order_item_id: int
    order_item_shipment_picking_histories: list[OrderItemShipmentPickingHistory]

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class Shipment(BaseModel):
    carrier_barcode: str 
    carrier_id: int
    carrier_name: str = Field(min_length=1)
    created_at: datetime
    delivery_at: datetime
    height: int
    id: float
    items_shipment_serial_numbers: list[ItemsShipmentSerialNumber]
    label_price_cents: Optional[Any] = None
    label_price_currency: Optional[Any] = None
    length: int
    order_id: int
    order_items_shipments: list[OrderItemsShipment]
    comments: list[str]
    package_id: int
    package_shipped: bool
    shipping_method_id: int
    shipping_method_name: str = Field(min_length=1)
    shipping_ref: str = Field(min_length=1)
    total_weight: int
    tracking_url: str = Field(min_length=1)
    updated_at: datetime
    supplier_name: str
    user_id: int  #
    width: int
    sscc_barcode: str

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }