from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: str = Field(..., description="The unique identifier of the user.")
    api_client_id: int = Field(..., description="The unique identifier of the API client associated with the user.")
    email: str = Field(..., description="The email address of the user.")
    company_id: Optional[int] = Field(None, description="The unique identifier of the company associated with the user, if applicable.")
    first_name: Optional[str] = Field(None, description="The first name of the user, if provided.")
    last_name: Optional[str] = Field(None, description="The last name of the user, if provided.")
    roles: List[str] = Field(..., description="A list of roles assigned to the user.")