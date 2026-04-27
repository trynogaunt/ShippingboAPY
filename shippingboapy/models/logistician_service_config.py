from pydantic import BaseModel, Field
from typing import Optional

class LogisticianServiceConfigObject(BaseModel):
    service_code: Optional[str] = Field(None, alias="service_code", description="The code of the logistician service associated with this configuration.")
    shipping_options: Optional[str] = Field(None, alias="shipping_options", description="The shipping options associated with this logistician service configuration.")
    tags_to_send: Optional[str] = Field(None, alias="tags_to_send", description="The tags to send associated with this logistician service configuration.")

class LogisticianServiceConfig(BaseModel):
    archived: Optional[bool] = Field(None, alias="archived", description="Indicates whether the logistician service configuration is archived.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the logistician service configuration was created.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the logistician service configuration.")
    predefined_logistician_id: Optional[int] = Field(None, alias="predefined_logistician_id", description="The unique identifier of the predefined logistician associated with this configuration.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the logistician service configuration was last updated.")
    config: Optional[LogisticianServiceConfigObject] = Field(None, alias="config", description="The configuration details of the logistician service.")