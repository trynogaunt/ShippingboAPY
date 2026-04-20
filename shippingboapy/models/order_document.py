from pydantic import BaseModel, Field
from typing import Optional

class OrderDocument(BaseModel):
    error_message: Optional[str] = Field(None, alias="error_message", description="The error message associated with the order document, if applicable.")
    id: Optional[str] = Field(..., alias="id", description="The unique identifier of the order document.")
    email: Optional[str] = Field(None, alias="email", description="The email address associated with the order document, if applicable.")
    level: Optional[str] = Field(None, alias="level", description="The level of the order document (e.g., info, warning, error).")
    message: Optional[str] = Field(None, alias="message", description="The message content of the order document.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the order document.")
    title: Optional[str] = Field(None, alias="title", description="The title of the order document.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the order document was last updated.")