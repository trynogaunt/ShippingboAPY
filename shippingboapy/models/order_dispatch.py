from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class OrderDispatch(BaseModel):
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the order dispatch.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the dispatch.")
    state: Literal["waiting_for_dispatch", "need_redispatch", "dispatched", "in_trouble", "partially_shipped", "shipped", "canceled"] = Field(None, alias="state", description="The current state of the order dispatch (e.g., waiting_for_dispatch, need_redispatch, dispatched).")
    error_message: Optional[str] = Field(None, alias="error_message", description="The error message associated with the order dispatch, if applicable.")
    origin_ref: Optional[str] = Field(None, alias="origin_ref", description="The reference of the origin of the order dispatch, if applicable.")
    origin_created_at: Optional[str] = Field(None, alias="origin_created_at", description="The timestamp of when the order dispatch was created at the origin, if applicable.")
    supplier_orders: Optional[List[dict]] = Field(None, alias="supplier_orders", description="The list of supplier order IDs associated with the order dispatch, if applicable.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }