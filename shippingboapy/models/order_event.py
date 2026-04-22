from pydantic import BaseModel, Field
from typing import Optional, Literal

class OrderEvent(BaseModel):
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the order event was created.")
    email: Optional[str] = Field(None, alias="email", description="The email address associated with the order event, if applicable.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the order event.")
    level: Optional[str] = Field(None, alias="level", description="The level of the order event (e.g., info, warning, error).")
    message: Optional[str] = Field(None, alias="message", description="The message content of the order event.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the order event.")
    title: Optional[str] = Field(None, alias="title", description="The title of the order event.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the order event was last updated.")

class OrderEventCreate(BaseModel):
    display_ps_enabled: bool = Field(False, alias="display_ps_enabled", description="Whether to enable display of the order event on the public storefront, if applicable.")
    level: Literal["info", "error"] = Field(..., alias="level", description="The level of the order event (e.g., info, warning, error).")
    message: str = Field(..., alias="message", description="The message content of the order event.")
    order_id: int = Field(..., alias="order_id", description="The unique identifier of the order associated with the order event.")
    title: str = Field(..., alias="title", description="The title of the order event.")