from pydantic import BaseModel, Field
from typing import Optional

class ProviderConfig(BaseModel):
    id: int = Field(..., alias="id", description="The unique identifier of the provider configuration.")
    name: str = Field(..., alias="name", description="The name of the provider configuration.")
    
    model_config = {
        "extra": "allow",
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
    implements_advanced_insurance: Optional[bool] = Field(None, alias="implements_advanced_insurance", description="Indicates whether the address label configuration implements advanced insurance features, if applicable.")
    implements_cn23: Optional[bool] = Field(None, alias="implements_cn23", description="Indicates whether the address label configuration implements CN23 customs declaration features, if applicable.")
    implements_cn23_doc_fetching: Optional[bool] = Field(None, alias="implements_cn23_doc_fetching", description="Indicates whether the address label configuration implements CN23 document fetching features, if applicable.")
    implements_consignments: Optional[bool] = Field(None, alias="implements_consignments", description="Indicates whether the address label configuration implements consignments features, if applicable.")
    implements_consignment_additional_reference: Optional[bool] = Field(None, alias="implements_consignment_additional_reference", description="Indicates whether the address label configuration implements consignment additional reference features, if applicable.")
    implements_contract_address: Optional[bool] = Field(None, alias="implements_contract_address", description="Indicates whether the address label configuration implements contract address features, if applicable.")
    implements_currency_conversion: Optional[bool] = Field(None, alias="implements_currency_conversion", description="Indicates whether the address label configuration implements currency conversion features, if applicable.")
    implements_dangerous_goods: Optional[bool] = Field(None, alias="implements_dangerous_goods", description="Indicates whether the address label configuration implements dangerous goods features, if applicable.")
    implements_dangerous_goods_docs: Optional[bool] = Field(None, alias="implements_dangerous_goods_docs", description="Indicates whether the address label configuration implements dangerous goods document features, if applicable.")
    implements_delivery_at_pick_up_location: Optional[bool] = Field(None, alias="implements_delivery_at_pick_up_location", description="Indicates whether the address label configuration implements delivery at pick-up location features, if applicable.")
    implements_delivery_slots: Optional[bool] = Field(None, alias="implements_delivery_slots", description="Indicates whether the address label configuration implements delivery slots features, if applicable.")
    implements_depositor_address: Optional[bool] = Field(None, alias="implements_depositor_address", description="Indicates whether the address label configuration implements depositor address features, if applicable.")
    implements_dimensions: Optional[bool] = Field(None, alias="implements_dimensions", description="Indicates whether the address label configuration implements dimensions features, if applicable.")
    implements_disable_auto_printing: Optional[bool] = Field(None, alias="implements_disable_auto_printing", description="Indicates whether the address label configuration implements disable auto printing features, if applicable.")
    implements_disable_cn23_information: Optional[bool] = Field(None, alias="implements_disable_cn23_information", description="Indicates whether the address label configuration implements disable CN23 information features, if applicable.")
    implements_exclude_surtaxed_zip_codes: Optional[bool] = Field(None, alias="implements_exclude_surtaxed_zip_codes", description="Indicates whether the address label configuration implements exclude surtaxed zip codes features, if applicable.")
    implements_export_reference: Optional[bool] = Field(None, alias="implements_export_reference", description="Indicates whether the address label configuration implements export reference features, if applicable.")
    implements_forced_consignments: Optional[bool] = Field(None, alias="implements_forced_consignments", description="Indicates whether the address label configuration implements forced consignments features, if applicable.")
    implements_forced_package_products: Optional[bool] = Field(None, alias="implements_forced_package_products", description="Indicates whether the address label configuration implements forced package products features, if applicable.")
    implements_insurance: Optional[bool] = Field(None, alias="implements_insurance", description="Indicates whether the address label configuration implements insurance features, if applicable.")
    implements_insurance_level: Optional[bool] = Field(None, alias="implements_insurance_level", description="Indicates whether the address label configuration implements insurance level features, if applicable.")
    implements_mono_parcel_shipping: Optional[bool] = Field(None, alias="implements_mono_parcel_shipping", description="Indicates whether the address label configuration implements mono parcel shipping features, if applicable.")
    implements_offer_on_zip_codes: Optional[bool] = Field(None, alias="implements_offer_on_zip_codes", description="Indicates whether the address label configuration implements offer on zip codes features, if applicable.")
    implements_optional_weight: Optional[bool] = Field(None, alias="implements_optional_weight", description="Indicates whether the address label configuration implements optional weight features, if applicable.")
    implements_package_description: Optional[bool] = Field(None, alias="implements_package_description", description="Indicates whether the address label configuration implements package description features, if applicable.")
    implements_parts_count: Optional[bool] = Field(None, alias="implements_parts_count", description="Indicates whether the address label configuration implements parts count features, if applicable.")
    implements_pickup_request: Optional[bool] = Field(None, alias="implements_pickup_request", description="Indicates whether the address label configuration implements pickup request features, if applicable.")
    implements_products_price: Optional[bool] = Field(None, alias="implements_products_price", description="Indicates whether the address label configuration implements products price features, if applicable.")
    implements_provide_barcode: Optional[bool] = Field(None, alias="implements_provide_barcode", description="Indicates whether the address label configuration implements provide barcode features, if applicable.")
    implements_provide_shipping_method_name: Optional[bool] = Field(None, alias="implements_provide_shipping_method_name", description="Indicates whether the address label configuration implements provide shipping method name features, if applicable.")
    implements_provide_carrier_name: Optional[bool] = Field(None, alias="implements_provide_carrier_name", description="Indicates whether the address label configuration implements provide carrier name features, if applicable.")
    implements_requested_shipping_date: Optional[bool] = Field(None, alias="implements_requested_shipping_date", description="Indicates whether the address label configuration implements requested shipping date features, if applicable.")
    implements_return_address: Optional[bool] = Field(None, alias="implements_return_address", description="Indicates whether the address label configuration implements return address features, if applicable.")
    implements_return_config_creation: Optional[bool] = Field(None, alias="implements_return_config_creation", description="Indicates whether the address label configuration implements return config creation features, if applicable.")
    implements_sender_address: Optional[bool] = Field(None, alias="implements_sender_address", description="Indicates whether the address label configuration implements sender address features, if applicable.")
    implements_verifiable_connection: Optional[bool] = Field(None, alias="implements_verifiable_connection", description="Indicates whether the address label configuration implements verifiable connection features, if applicable.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }