from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Any


class ReturnOrderitem(BaseModel):
    batch_number: str = Field(..., description="The batch number of the returned product that is not restockable.")
    id: int = Field(..., description="The unique identifier of the returned product that is not restockable.")
    last_preparation_day: str = Field(..., description="The last preparation day of the returned product that is not restockable.")
    lu_quantity: float = Field(..., description="The quantity of the returned product that is not restockable.")
    product_id: int = Field(..., description="The unique identifier of the product associated with the returned product that is not restockable.")
    product_logistic_unit_id: int = Field(..., description="The unique identifier of the logistic unit associated with the returned product that is not restockable.")
    reason: str = Field(..., description="The reason why the returned product is not restockable.")
    reason_ref: str = Field(..., description="The reference for the reason why the returned product is not restockable.")
    return_order_expected_item_id: int = Field(..., description="The unique identifier of the expected return order item associated with the returned product that is not restockable.")
    serial_number: str = Field(..., description="The serial number of the returned product that is not restockable.")

class ReturnedProductNotRestockable(ReturnOrderitem):
    pass

class ReturnOrderExpectedItem(BaseModel):
    id: int = Field(..., description="The unique identifier of the expected return order item.")
    product_id: int = Field(..., description="The unique identifier of the product associated with the expected return order item.")
    product_user_ref: str = Field(..., description="The user reference for the product associated with the expected return order item.")
    quantity: int = Field(..., description="The quantity of the product expected to be returned.")
    return_order_id: int = Field(..., description="The unique identifier of the associated return order.")
    user_ref: str = Field(..., description="An optional user reference for the expected return order item.")

class ReturnOrder(BaseModel):
    barcode: str = Field(..., description="The barcode of the return order.")
    id: int = Field(..., description="The unique identifier of the return order.")
    order_id: int = Field(..., description="The unique identifier of the associated order.")
    reason: str = Field(..., description="The reason for the return.")
    reason_ref: str = Field(..., description="The reference for the reason of the return.")
    return_label_config_id: int = Field(..., description="The unique identifier of the return label configuration.")
    return_order_expected_items: List[ReturnOrderExpectedItem] = Field(..., description="A list of expected items associated with the return order.")
    return_order_items: List[ReturnOrderitem] = Field(..., description="A list of items associated with the return order.")
    return_order_type: Literal["return_order_label", "return_order_carrier", "return_order_customer"] = Field(..., description="The type of the return order.")
    returned_at: Optional[str] = Field(None, description="The date and time when the return order was returned.")
    returned_product_not_restockable: List[ReturnedProductNotRestockable] = Field(..., description="A list of products that are not restockable after being returned.")
    shipping_method_id: int = Field(..., description="The unique identifier of the shipping method associated with the return order.")
    shipping_ref: str = Field(..., description="The reference for the shipping associated with the return order.")
    state: Literal["new", "canceled", "returned", "closed", "dispatched", "in_trouble"] = Field("new", description="The current state of the return order.")
    user_mail : str = Field(..., description="The email address of the user associated with the return order.")
    order_document_id: Optional[int] = Field(None, description="The unique identifier of the document associated with the order.")
