from pydantic import BaseModel, Field
from typing import Optional, List, Any, Literal
from shippingboapy.models.types import ShippingboDateTime

class AddressLabelObject(BaseModel):
    api_client_id: Optional[int] = Field(None, alias="api_client_id", description="The unique identifier of the API client associated with the address label object, if applicable.")
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the address label object was created.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the address label object.")
    label_url: Optional[str] = Field(None, alias="label_url", description="The URL of the address label object, if applicable.")
    shipped_at: Optional[str] = Field(None, alias="shipped_at", description="The date and time when the address label object was shipped, if applicable.")
    shipping_method_name: Optional[str] = Field(None, alias="shipping_method_name", description="The name of the shipping method associated with the address label object, if applicable.")
    shipping_ref: Optional[str] = Field(None, alias="shipping_ref", description="The reference of the shipping associated with the address label object, if applicable.")
    tracking_url: Optional[str] = Field(None, alias="tracking_url", description="The URL of the tracking information for the address label object, if applicable.")
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the address label object was last updated.")
    insurance_provided: Optional[bool] = Field(None, alias="insurance_provided", description="Indicates whether insurance is provided for the address label object, if applicable.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class LabelCredential(BaseModel):
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the label credential was created.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the label credential.")
    type: Optional[str] = Field(None, alias="type", description="The type of the label credential (e.g., api_key, oauth_token).")
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the label credential was last updated.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class LabelOfferOption(BaseModel):
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the label offer option was created.")
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the label offer option.")
    receiver_country: Optional[str] = Field(None, alias="receiver_country", description="The country of the receiver associated with the label offer option, if applicable.")
    service: Optional[str] = Field(None, alias="service", description="The service associated with the label offer option, if applicable.")
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the label offer option was last updated.")
    zip_prefix: Optional[str] = Field(None, alias="zip_prefix", description="The ZIP code prefix associated with the label offer option, if applicable.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class AddressLabelSummaries(BaseModel):
    address_label: Optional[AddressLabelObject] = Field(None, alias="address_label", description="The address label object associated with the address label summaries, if applicable.")
    country: Optional[str] = Field(None, alias="country", description="The country associated with the address label summaries, if applicable.")
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the address label summaries were created.")
    height: Optional[int] = Field(None, alias="height", description="The height of the package associated with the address label summaries, if applicable.")
    id : Optional[int] = Field(None, alias="id", description="The unique identifier of the address label summaries.")
    insurance_value_cents: Optional[int] = Field(None, alias="insurance_value_cents", description="The insurance value in cents associated with the address label summaries, if applicable.")
    insurance_value_currency: Optional[str] = Field(None, alias="insurance_value_currency", description="The currency of the insurance value associated with the address label summaries, if applicable.")
    label_credential: Optional[LabelCredential] = Field(None, alias="label_credential", description="The label credential associated with the address label summaries, if applicable.")
    label_offer_option: Optional[LabelOfferOption] = Field(None, alias="label_offer_option", description="The label offer option associated with the address label summaries, if applicable.")
    length: Optional[int] = Field(None, alias="length", description="The length of the package associated with the address label summaries, if applicable.")
    merchant_country: Optional[str] = Field(None, alias="merchant_country", description="The country of the merchant associated with the address label summaries, if applicable.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the address label summaries, if applicable.")
    origin: Optional[str] = Field(None, alias="origin", description="The origin of the package associated with the address label summaries, if applicable.")
    origin_ref: Optional[str] = Field(None, alias="origin_ref", description="The reference of the origin associated with the address label summaries, if applicable.")
    reseller_label_provider_id: Optional[int] = Field(None, alias="reseller_label_provider_id", description="The unique identifier of the reseller label provider associated with the address label summaries.")
    reseller_label_provider_name: Optional[str] = Field(None, alias="reseller_label_provider_name", description="The name of the reseller label provider associated with the address label summaries.")
    source: Optional[str] = Field(None, alias="source", description="The source of the address label summaries, if applicable.")
    source_ref: Optional[str] = Field(None, alias="source_ref", description="The reference of the source associated with the address label summaries, if applicable.")
    total_weight: Optional[int] = Field(None, alias="total_weight", description="The total weight of the package associated with the address label summaries, if applicable.")
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the address label summaries were last updated.")
    width: Optional[int] = Field(None, alias="width", description="The width of the package associated with the address label summaries, if applicable.")
    zip: Optional[str] = Field(None, alias="zip", description="The ZIP code associated with the address label summaries, if applicable.")