from pydantic import BaseModel, Field
from typing import Optional, Any

class PackagePictureConfig(BaseModel):
    id: str = Field(..., alias="id", description="The unique identifier of the package picture configuration.")
    auto_mode_enabled: bool = Field(False, alias="auto_mode_enabled", description="Indicates whether the auto mode is enabled for the package picture configuration.")
    auto_mode_timer_milliseconds: float = Field(0, alias="auto_mode_timer_milliseconds", description="The timer duration in milliseconds for the auto mode of the package picture configuration.")
    tag_needed: bool = Field(False, alias="tag_needed", description="Indicates whether a tag is needed for the package picture configuration.")