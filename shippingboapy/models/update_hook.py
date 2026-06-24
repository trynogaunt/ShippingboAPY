from pydantic import BaseModel, Field
from typing import Optional, Literal

class WebHook(BaseModel):
    activated: bool = Field(..., description="Indicates whether the webhook is activated or not.")
    endpoint_url: str = Field(..., description="The endpoint URL where the webhook will send data.")
    field: str = Field(..., description="The specific field that the webhook is monitoring for changes.")
    from_value: Optional[str] = Field(None, description="The previous value of the monitored field before the change occurred.")
    id: str = Field(..., description="The unique identifier of the webhook.")
    object_class: Literal["Order", "OrderEvent", "OrderItemProductMapping", "PreparationRun", "Product", "ProductBarcode", "ProductStockVariation", "ReturnOrder", "Shipment", "SlotContent", "SlotStockVariation", "SupplyCapsule", "WarehouseTransfer"] = Field(..., description="The class of the object that the webhook is associated with.")
    to_value: Optional[str] = Field(None, description="The new value of the monitored field after the change occurred.")
    visible: bool = Field(..., description="Deprecated: Indicates whether the webhook is visible or not.")