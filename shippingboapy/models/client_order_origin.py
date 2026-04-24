from pydantic import BaseModel, Field
from typing import Optional

class ClientOrderOriginCreate(BaseModel):
    display_name: str = Field(..., alias="display_name", description="The display name of the client order origin.")
    origin: str = Field("API", alias="from", description="The unique identifier of the client order origin.")
    name: str = Field(..., alias="name", description="The name of the client order origin.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }

class ClientOrderOrigin(ClientOrderOriginCreate):
    id: int = Field(..., alias="id", description="The unique identifier of the client order origin.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the client order origin was created.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the client order origin was last updated.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }