from pydantic import BaseModel, Field
from typing import Optional
from shippingboapy.models.types import ShippingboDateTime

class ProviderConfig(BaseModel):
    id: int = Field(..., alias="id", description="The unique identifier of the provider configuration.")
    name: str = Field(..., alias="name", description="The name of the provider configuration.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class AddressLabelConfig(BaseModel):
    id: int = Field(..., alias="id", description="The unique identifier of the address label configuration.")
    type: str = Field(..., alias="type", description="The type of the address label configuration (e.g., default, custom).")
    name: str = Field(..., alias="name", description="The name of the address label configuration.")
    archived: bool = Field(..., alias="archived", description="Indicates whether the address label configuration is archived.")
    ready: bool = Field(..., alias="ready", description="Indicates whether the address label configuration is ready for use.")
    retired: Optional[bool] = Field(None, alias="retired", description="Indicates whether the address label configuration is retired and no longer in use.")
    allow_included_version: Optional[bool] = Field(None, alias="allow_included_version", description="Indicates whether the address label configuration allows included versions, if applicable.")
    sender_country: str = Field(..., alias="sender_country", description="The country of the sender associated with the address label configuration.")
    label_credential_id: int = Field(..., alias="label_credential_id", description="The unique identifier of the label credential associated with the address label configuration, if applicable.")
    label_credential_name: str = Field(..., alias="label_credential_name", description="The name of the label credential associated with the address label configuration, if applicable.")
    custom_logo_url: Optional[str] = Field(None, alias="custom_logo_url", description="The URL of the custom logo associated with the address label configuration, if applicable.")
    config: dict = Field(None, alias="config", description="The configuration details of the address label configuration, if applicable.")
    sender_address_id: Optional[int] = Field(None, alias="sender_address_id", description="The unique identifier of the sender address associated with the address label configuration, if applicable.")
    contract_address_id: Optional[int] = Field(None, alias="contract_address_id", description="The unique identifier of the contract address associated with the address label configuration, if applicable.")
    depositor_address_id: Optional[int] = Field(None, alias="depositor_address_id", description="The unique identifier of the depositor address associated with the address label configuration, if applicable.")
    return_address_id: Optional[int] = Field(None, alias="return_address_id", description="The unique identifier of the return address associated with the address label configuration, if applicable.")
    address_label_config_customization_ids: Optional[list[int]] = Field(None, alias="address_label_config_customization_ids", description="A list of unique identifiers for the address label configuration customizations associated with the address label configuration, if applicable.")
    insurance_provider_config_id: Optional[int] = Field(None, alias="insurance_provider_config_id", description="The unique identifier of the insurance provider configuration associated with the address label configuration, if applicable.")
    insurance_provider_configs: Optional[list[ProviderConfig]] = Field(None, alias="insurance_provider_configs", description="A list of provider configurations for insurance associated with the address label configuration, if applicable.")
    logo_source_url: Optional[str] = Field(None, alias="logo_source_url", description="The URL of the logo source associated with the address label configuration, if applicable.")
    public_boolean_fields: Optional[list[str]] = Field(None, alias="public_boolean_fields", description="A list of public boolean fields associated with the address label configuration, if applicable.")
    public_list_fields: Optional[list[str]] = Field(None, alias="public_list_fields", description="A list of public list fields associated with the address label configuration, if applicable.")
    credential_public_info: Optional[dict] = Field(None, alias="credential_public_info", description="A dictionary containing public information about the credentials associated with the address label configuration, if applicable.")
    connectable: Optional[bool] = Field(None, alias="connectable", description="Indicates whether the address label configuration is connectable to other configurations or services, if applicable.")
    created_at: str = Field(..., alias="created_at", description="The date and time when the address label configuration was created.")
    updated_at: str = Field(..., alias="updated_at", description="The date and time when the address label configuration was last updated.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }