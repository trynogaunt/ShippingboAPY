from pydantic import BaseModel, Field
from typing import Optional, Any

class ReservationItem(BaseModel):
    consumed_quantity: int = Field(0, alias="consumed_quantity", description="The quantity of the item that has been consumed.")
    created_at: str = Field(..., alias="created_at", description="The date and time when the reservation item was created.")
    id: int = Field(..., alias="id", description="The unique identifier of the reservation item.")
    pre_order_reservation_id: str = Field(..., alias="pre_order_reservation_id", description="The unique identifier of the preorder reservation associated with the reservation item.")
    product_id: str = Field(..., alias="product_id", description="The unique identifier of the product associated with the reservation item.")
    quantity: int = Field(..., alias="quantity", description="The quantity of the item reserved.")
    unassigned_quantity: int = Field(..., alias="unassigned_quantity", description="The quantity of the item that has not been assigned.")
    updated_at: str = Field(..., alias="updated_at", description="The date and time when the reservation item was last updated.")

class PreorderReservation(BaseModel):
    created_at: str = Field(..., alias="created_at", description="The date and time when the preorder reservation was created.")
    end_reservation_date: str = Field(..., alias="end_reservation_date", description="The end date of the preorder reservation.")
    id: int = Field(..., alias="id", description="The unique identifier of the preorder reservation.")
    pre_order_reservation_items: list[ReservationItem] = Field(..., alias="pre_order_reservation_items", description="A list of preorder reservation items associated with the preorder reservation.")
    source: str = Field(..., alias="source", description="The source of the preorder reservation.")
    source_ref: str = Field(..., alias="source_ref", description="The reference of the source of the preorder reservation.")
    state: str = Field(..., alias="state", description="The state of the preorder reservation.")
    updated_at: str = Field(..., alias="updated_at", description="The date and time when the preorder reservation was last updated.")