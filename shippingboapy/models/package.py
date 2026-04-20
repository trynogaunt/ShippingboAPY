from pydantic import BaseModel, Field
from typing import Optional

class Package(BaseModel):
    address_label_config_id: Optional[int] = Field(None, alias="address_label_config_id", description="The unique identifier of the address label configuration associated with the package.")
    cardboard_id: Optional[int] = Field(None, alias="cardboard_id", description="The unique identifier of the cardboard associated with the package.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the package was created.")
    id : Optional[int] = Field(None, alias="id", description="The unique identifier of the package.")
    insurance_value_cents: Optional[int] = Field(None, alias="insurance_value_cents", description="The insurance value of the package in cents.")
    insurance_value_currency: Optional[str] = Field(None, alias="insurance_value_currency", description="The currency of the insurance value of the package.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the package.")
    order_item_packages: Optional[list] = Field(None, alias="order_item_packages", description="A list of order item packages associated with the package.")
    item_lines: Optional[list] = Field(None, alias="item_lines", description="A list of item lines associated with the package.")
    package_product_histories: Optional[list] = Field(None, alias="package_product_histories", description="A list of package product histories associated with the package.")
    picking_control_validated: Optional[bool] = Field(None, alias="picking_control_validated", description="Indicates whether the picking control has been validated for the package.")
    requested_shipping_date: Optional[str] = Field(None, alias="requested_shipping_date", description="The requested shipping date for the package.")
    return_label_config_id: Optional[int] = Field(None, alias="return_label_config_id", description="The unique identifier of the return label configuration associated with the package.")
    total_weight: Optional[int] = Field(None, alias="total_weight", description="The total weight of the package.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the package was last updated.")
    address_label_id: Optional[str] = Field(None, alias="address_label_id", description="The unique identifier of the address label associated with the package.")