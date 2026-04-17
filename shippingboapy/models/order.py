from pydantic import BaseModel, Field
from typing import List, Optional
from shippingboapy.models.tag import OrderTag

class Address(BaseModel):
    apartement_number: Optional[str] = Field(None, alias="apartement_number", description="The number of the apartment, if applicable.")
    building: Optional[str] = Field(None, alias="building", description="The building name or number, if applicable.")
    city: str = Field(..., alias="city", description="The city of the address.")
    civility: Optional[str] = Field(None, alias="civilitity", description="The civility of the recipient (e.g., Mr, Ms, Company).")
    company_name: Optional[str] = Field(None, alias="company_name", description="The name of the company, if applicable.")
    country: str = Field(..., alias="country", description="The country of the address.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the address was created.")
    email: Optional[str] = Field(None, alias="email", description="The email address associated with the address.")
    eori_importer: Optional[str] = Field(None, alias="eori_importer", description="The EORI number of the importer, if applicable.")
    firstname: Optional[str] = Field(None, alias="firstname", description="The first name of the recipient.")
    fullname: Optional[str] = Field(None, alias="fullname", description="The full name of the recipient.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the address.")
    instructions: Optional[str] = Field(None, alias="instructions", description="Special instructions for the delivery, if applicable.")
    lastname: Optional[str] = Field(None, alias="lastname", description="The last name of the recipient.")
    phone1: Optional[str] = Field(None, alias="phone", description="The phone number associated with the address.")
    phone2: Optional[str] = Field(None, alias="phone2", description="An additional phone number associated with the address, if applicable.")
    place_name: Optional[str] = Field(None, alias="place_name", description="The name of the place, if applicable.")
    state: Optional[str] = Field(None, alias="state", description="The state or province of the address.")
    street1: Optional[str] = Field(None, alias="street1", description="The first line of the street address.")
    street2: Optional[str] = Field(None, alias="street2", description="The second line of the street address, if applicable.")
    street3: Optional[str] = Field(None, alias="street3", description="The third line of the street address, if applicable.")
    street4: Optional[str] = Field(None, alias="street4", description="The fourth line of the street address, if applicable.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the address was last updated.")
    vat_importer: Optional[str] = Field(None, alias="vat_importer", description="The VAT number of the importer, if applicable.")
    zip: Optional[str] = Field(None, alias="zip", description="The postal code of the address.")
    
class CarrierConfig(BaseModel):
    service_code: Optional[str] = Field(None, alias="service_code", description="The code of the carrier service.")
    shipping_options: Optional[str] = Field(None, alias="shipping_options", description="Additional shipping options for the carrier service.")
    tags_to_send: Optional[str] = Field(None, alias="tags_to_send", description="Tags to send to the carrier for the shipment.")

class MappedProduct(BaseModel):
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the mapped product was created.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the mapped product.")
    product_id: Optional[int] = Field(None, alias="product_id", description="The unique identifier of the product in the external system.")
    order_item_id: Optional[int] = Field(None, alias="order_item_id", description="The unique identifier of the order item associated with the mapped product.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the mapped product was last updated.")
    quantity: Optional[int] = Field(None, alias="quantity", description="The quantity of the product in the order item.")
    product_user_ref: Optional[str] = Field(None, alias="product_user_ref", description="The user reference of the product in the external system, if applicable.")
    
class CarrierService(BaseModel):
    archived: Optional[bool] = Field(None, alias="archived", description="Indicates whether the carrier service is archived.")
    config: Optional[CarrierConfig] = Field(None, alias="config", description="The configuration details of the carrier service.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the carrier service was created.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the carrier service.")
    name: Optional[str] = Field(None, alias="name", description="The name of the carrier service.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the carrier service was last updated.")

class OrderDocument(BaseModel):
    error_message: Optional[str] = Field(None, alias="error_message", description="The error message associated with the order document, if applicable.")
    id: Optional[str] = Field(..., alias="id", description="The unique identifier of the order document.")
    email: Optional[str] = Field(None, alias="email", description="The email address associated with the order document, if applicable.")
    level: Optional[str] = Field(None, alias="level", description="The level of the order document (e.g., info, warning, error).")
    message: Optional[str] = Field(None, alias="message", description="The message content of the order document.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the order document.")
    title: Optional[str] = Field(None, alias="title", description="The title of the order document.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the order document was last updated.")
    
class OrderEvent(BaseModel):
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the order event was created.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the order event.")
    name: Optional[str] = Field(None, alias="name", description="The name of the order event.")
    payload: Optional[dict] = Field(None, alias="payload", description="The payload of the order event, containing additional details about the event.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the order event was last updated.")

class OrderItemUpdate(BaseModel):
    id: int = Field(..., alias="id", description="The unique identifier of the order item to update.")
    product_ean: Optional[str] = Field(None, alias="product_ean", description="The EAN13 code of the product associated with the order item, if applicable.")
    product_ref: Optional[str] = Field(None, alias="product_reference", description="The reference of the product associated with the order item, if applicable.")
    product_source: Optional[str] = Field(None, alias="product_source", description="The source of the product information for the order item (e.g., user_ref, ean13).")
    product_source_ref: Optional[str] = Field(None, alias="product_source_ref", description="The reference value of the product source for the order item (e.g., the user_ref or ean13 value).")
    quantity: Optional[int] = Field(None, alias="quantity", description="The quantity of the product in the order item.")
    title: Optional[str] = Field(None, alias="title", description="The title or name of the order item.")
    stock_type_ref: Optional[str] = Field(None, alias="stock_type_ref", description="The stock type reference for the order item, if applicable.")
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True,
    }

class OrderItem(OrderItemUpdate):
    price_tax_included_cents: Optional[int] = Field(None, alias="price_tax_included_cents", description="The price of the order item including tax, in cents.")
    price_tax_included_currency: Optional[str] = Field(None, alias="price_tax_included_currency", description="The currency of the price including tax for the order item.")
    source: Optional[str] = Field(None, alias="source", description="The source of the order item information (e.g., external system name).")
    source_ref: Optional[str] = Field(None, alias="source_ref", description="The reference value of the source for the order item (e.g., the order item ID in the external system).")
    tax_cents: Optional[int] = Field(None, alias="tax_cents", description="The tax amount for the order item, in cents.")
    tax_currency: Optional[str] = Field(None, alias="tax_currency", description="The currency of the tax amount for the order item.")
    computed_prices: Optional[dict] = Field(None, alias="computed_prices", description="The computed prices for the order item, containing details such as price breakdowns, discounts, etc.")
    additional_content: Optional[dict] = Field(None, alias="additional_content", description="Additional content or information related to the order item, if applicable.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }
    
class OrderItemCreate(BaseModel):
    id: Optional[int] = Field(None, alias="id", description="The unique identifier of the order item.")
    price_tax_included_cents: Optional[int] = Field(None, alias="price_tax_included_cents", description="The price of the order item including tax, in cents.")
    price_tax_included_currency: Optional[str] = Field(None, alias="price_tax_included_currency", description="The currency of the price including tax for the order item.")
    product_ean: Optional[str] = Field(None, alias="product_ean13", description="The EAN13 code of the product associated with the order item, if applicable.")
    product_ref: Optional[str] = Field(None, alias="product_reference", description="The reference of the product associated with the order item, if applicable.")
    product_source: Optional[str] = Field(None, alias="product_source", description="The source of the product information for the order item (e.g., user_ref, ean13).")
    product_source_ref: Optional[str] = Field(None, alias="product_source_ref", description="The reference value of the product source for the order item (e.g., the user_ref or ean13 value).")
    quantity: Optional[int] = Field(None, alias="quantity", description="The quantity of the product in the order item.")
    source: Optional[str] = Field(None, alias="source", description="The source of the order item information (e.g., external system name).")
    source_ref: Optional[str] = Field(None, alias="source_ref", description="The reference value of the source for the order item (e.g., the order item ID in the external system).")
    tax_cents: Optional[int] = Field(None, alias="tax_cents", description="The tax amount for the order item, in cents.")
    tax_currency: Optional[str] = Field(None, alias="tax_currency", description="The currency of the tax amount for the order item.")
    title: Optional[str] = Field(None, alias="title", description="The title or name of the order item.")
    computed_prices: Optional[dict] = Field(None, alias="computed_prices", description="The computed prices for the order item, containing details such as price breakdowns, discounts, etc.")
    additional_content: Optional[dict] = Field(None, alias="additional_content", description="Additional content or information related to the order item, if applicable.")
    
class ItemShipmentSerialNumber(BaseModel):
    order_item_id: Optional[int] = Field(None, alias="order_item_id", description="The unique identifier of the order item associated with the shipment serial number.")
    serial_number: Optional[str] = Field(None, alias="serial_number", description="The serial number of the item in the shipment, if applicable.")

class OrderItemShipmentPickingHistory(BaseModel):
    batch_number: Optional[str] = Field(None, alias="batch_number", description="The batch number associated with the order item shipment picking history, if applicable.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the order item shipment picking history.")
    last_preparation_day: Optional[str] = Field(None, alias="last_preparation_day", description="The date and time of the last preparation for the order item shipment picking history, if applicable.")
    quantity: Optional[int] = Field(None, alias="quantity", description="The quantity associated with the order item shipment picking history.")

class OrderItemShipment(BaseModel):
    item_quantity: Optional[int] = Field(None, alias="item_quantity", description="The quantity of the item in the shipment.")
    order_item_id: Optional[int] = Field(None, alias="order_item_id", description="The unique identifier of the order item associated with the shipment.")
    order_item_shipment_picking_histories: Optional[List[OrderItemShipmentPickingHistory]] = Field(None, alias="order_item_shipment_picking_histories", description="The picking histories of the order item shipment, if applicable.")
    comments: Optional[List[str]] = Field(None, alias="comments", description="Comments related to the order item shipment, if applicable.")
    
    
class Shipment(BaseModel):
    carrier_barcode: Optional[str] = Field(None, alias="carrier_barcode", description="The barcode provided by the carrier for the shipment, if applicable.")
    carrier_id: Optional[int] = Field(None, alias="carrier_id", description="The unique identifier of the carrier associated with the shipment, if applicable.")
    carrier_name: Optional[str] = Field(None, alias="carrier_name", description="The name of the carrier associated with the shipment, if applicable.")
    created_at: Optional[str] = Field(None, alias="created_at", description="The date and time when the shipment was created.")
    delivery_at: Optional[str] = Field(None, alias="delivery_at", description="The date and time when the shipment is expected to be delivered, if applicable.")
    height: Optional[int] = Field(None, alias="height_cm", description="The height of the shipment in centimeters, if applicable.")
    id: Optional[int] = Field(..., alias="id", description="The unique identifier of the shipment.")
    items_shipment_serial_numbers: Optional[List[ItemShipmentSerialNumber]] = Field(None, alias="items_shipment_serial_numbers", description="The list of item shipment serial numbers associated with the shipment, if applicable.")
    label_price_cents: Optional[int] = Field(None, alias="label_price_cents", description="The price of the shipment label in cents, if applicable.")
    label_price_currency: Optional[str] = Field(None, alias="label_price_currency", description="The currency of the shipment label price, if applicable.")
    length: Optional[int] = Field(None, alias="length_cm", description="The length of the shipment in centimeters, if applicable.")
    order_id: Optional[int] = Field(None, alias="order_id", description="The unique identifier of the order associated with the shipment.")
    order_items_shipments: Optional[List[OrderItemShipment]] = Field(None, alias="order_items_shipments", description="The list of order item shipments associated with the shipment, if applicable.")
    package_id: Optional[int] = Field(None, alias="package_id", description="The identifier of the package for the shipment, if applicable.")
    package_shipped: Optional[bool] = Field(None, alias="package_shipped", description="Indicates whether the package has been shipped.")
    shipping_method_id: Optional[int] = Field(None, alias="shipping_method_id", description="The identifier of the shipping method for the shipment, if applicable.")
    shipping_method_name: Optional[str] = Field(None, alias="shipping_method_name", description="The name of the shipping method for the shipment, if applicable.")
    shipping_ref: Optional[str] = Field(None, alias="shipping_ref", description="The reference of the shipping for the shipment, if applicable.")
    total_weight: Optional[int] = Field(None, alias="total_weight_grams", description="The total weight of the shipment in grams, if applicable.")
    tracking_url: Optional[str] = Field(None, alias="tracking_url", description="The tracking URL for the shipment, if applicable.")
    updated_at: Optional[str] = Field(None, alias="updated_at", description="The date and time when the shipment was last updated.")
    supplier_name: Optional[str] = Field(None, alias="supplier_name", description="The name of the supplier for the shipment, if applicable.")
    user_id: Optional[int] = Field(None, alias="user_id", description="The unique identifier of the user associated with the shipment, if applicable.")
    width: Optional[int] = Field(None, alias="width_cm", description="The width of the shipment in centimeters, if applicable.")
    sscc_barcode: Optional[str] = Field(None, alias="sscc_barcode", description="The SSCC barcode for the shipment, if applicable.")

class OrderBase(BaseModel):
    id: int = Field(..., alias="id")
    origin_ref: Optional[str] = Field(None, alias="origin_ref")
    source: Optional[str] = Field(None, alias="source")
    state: Optional[str] = Field(None, alias="state")
    created_at: Optional[str] = Field(None, alias="created_at")
    updated_at: Optional[str] = Field(None, alias="updated_at")
    source_ref: Optional[str] = Field(None, alias="source_ref")
    origin: Optional[str] = Field(None, alias="origin")
    shipping_address_id: Optional[int] = Field(None, alias="shipping_address_id")
    custom_state: Optional[str] = Field(None, alias="custom_state")
    origin_created_at: Optional[str] = Field(None, alias="origin_created_at")
    shipped_at: Optional[str] = Field(None, alias="shipped_at")
    closed_at: Optional[str] = Field(None, alias="closed_at")
    state_changed_at: Optional[str] = Field(None, alias="state_changed_at")
    chosen_delivery_service: Optional[str] = Field(None, alias="chosen_delivery_service")
    relay_ref: Optional[str] = Field(None, alias="relay_ref")
    payment_medium: Optional[str] = Field(None, alias="payment_medium")
    total_price_currency: Optional[str] = Field(None, alias="total_price_currency")
    total_shipping_tax_included_currency: Optional[str] = Field(None, alias="total_shipping_tax_included_currency")
    total_discount_tax_included_currency: Optional[str] = Field(None, alias="total_discount_tax_included_currency")
    total_discount_tax_included_cents: Optional[int] = Field(None, alias="total_discount_tax_included_cents")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True,
    }

class Order(OrderBase):
    billing_address: Optional[Address] = Field(None, alias="billing_address", description="The billing address associated with the order.")
    closed_at: Optional[str] = Field(None, alias="closed_at", description="The date and time when the order was closed.")
    custom_state: Optional[str] = Field(None, alias="custom_state", description="The custom state of the order, if applicable.")
    earliest_chosen_delivery_at: Optional[str] = Field(None, alias="earliest_chosen_delivery_at", description="The earliest delivery date chosen for the order.")
    earliest_delivery_at: Optional[str] = Field(None, alias="earliest_delivery_at", description="The earliest delivery date for the order.")
    earliest_shipped_at: Optional[str] = Field(None, alias="earliest_shipped_at", description="The earliest shipped date for the order.")
    external_computed_carrier_service: Optional[CarrierService] = Field(None, alias="external_computed_carrier_service", description="The carrier service computed by the external system for the order.")
    initial_order_id: Optional[int] = Field(None, alias="initial_order_id", description="The initial order ID from the external system, if applicable.")
    latest_chosen_delivery_at: Optional[str] = Field(None, alias="latest_chosen_delivery_at", description="The latest delivery date chosen for the order.")
    latest_delivery_at: Optional[str] = Field(None, alias="latest_delivery_at", description="The latest delivery date for the order.")
    latest_shipped_at: Optional[str] = Field(None, alias="latest_shipped_at", description="The latest shipped date for the order.")
    mapped_carrier: Optional[str] = Field(None, alias="mapped_carrier", description="The carrier mapped to the order, if applicable.")
    mapped_products: Optional[List[MappedProduct]] = Field(None, alias="mapped_products", description="The products mapped to the order, if applicable.")
    order_documents: Optional[List[OrderDocument]] = Field(None, alias="order_documents", description="The documents associated with the order, if applicable.")
    order_events_attributes: Optional[List[OrderEvent]] = Field(None, alias="order_events_attributes", description="The attributes of the order events, if applicable.")
    order_items: Optional[List[OrderItem]] = Field(None, alias="order_items", description="The items associated with the order, if applicable.")
    order_tags: Optional[List[OrderTag]] = Field(None, alias="order_tags", description="The tags associated with the order, if applicable.")
    origin: Optional[str] = Field(None, alias="origin", description="The origin of the order (e.g., external system name).")
    payment_medium: Optional[str] = Field(None, alias="payment_medium", description="The payment medium used for the order (e.g., credit card, PayPal, etc.).")
    shipments: Optional[List[Shipment]] = Field(None, alias="shipments", description="The shipments associated with the order, if applicable.")
    shipping_address: Optional[Address] = Field(None, alias="shipping_address", description="The shipping address associated with the order.")
    total_price_cents: Optional[float] = Field(None, alias="total_price_cents", description="The total price of the order in cents, including tax.")
    total_shipping_cents: Optional[float] = Field(None, alias="total_shipping_cents", description="The total shipping cost for the order in cents, including tax.")
    total_shipping_currency: Optional[str] = Field(None, alias="total_shipping_currency", description="The currency of the total shipping cost for the order, if applicable.")
    total_shipping_tax_cents: Optional[float] = Field(None, alias="total_shipping_tax_cents", description="The total tax amount for the shipping cost of the order in cents.")
    total_shipping_tax_currency: Optional[str] = Field(None, alias="total_shipping_tax_currency", description="The currency of the total tax amount for the shipping cost of the order, if applicable).")
    total_shipping_tax_included_cents: Optional[float] = Field(None, alias="total_shipping_tax_included_cents", description="The total shipping cost including tax for the order in cents.")
    total_tax_cents: Optional[float] = Field(None, alias="total_tax_cents", description="The total tax amount for the order in cents.")
    total_tax_currency: Optional[str] = Field(None, alias="total_tax_currency", description="The currency of the total tax amount for the order, if applicable.")
    total_weight: Optional[float] = Field(None, alias="total_weight", description="The total weight of the order in grams, if applicable.")
    total_without_tax_cents: Optional[float] = Field(None, alias="total_without_tax_cents", description="The total price of the order without tax in cents.")
    total_without_tax_currency: Optional[str] = Field(None, alias="total_without_tax_currency", description="The currency of the total price of the order without tax, if applicable.")
    order_dispatch_id: Optional[int] = Field(None, alias="order_dispatch_id", description="The unique identifier of the order dispatch associated with the order, if applicable.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }
    
class OrderSummary(OrderBase):
    earliest_shipped_at: Optional[str] = Field(None, alias="earliest_shipped_at", description="The earliest shipped date for the order, if applicable.")
    latest_shipped_at: Optional[str] = Field(None, alias="latest_shipped_at", description="The latest shipped date for the order, if applicable.")
    earliest_delivery_at: Optional[str] = Field(None, alias="earliest_delivery_at", description="The earliest delivery date for the order, if applicable.")
    latest_delivery_at: Optional[str] = Field(None, alias="latest_delivery_at", description="The latest delivery date for the order, if applicable.")
    earliest_chosen_delivery_at: Optional[str] = Field(None, alias="earliest_chosen_delivery_at", description="The earliest delivery date chosen for the order, if applicable.")
    latest_chosen_delivery_at: Optional[str] = Field(None, alias="latest_chosen_delivery_at", description="The latest delivery date chosen for the order, if applicable.")
    fulfilled_by_marketplace: Optional[bool] = Field(None, alias="fulfilled_by_marketplace", description="Indicates whether the order is fulfilled by the marketplace, if applicable.")
    total_price_cents: Optional[int] = Field(None, alias="total_price_cents", description="The total price of the order in cents, including tax, if applicable.")
    total_without_tax_cents: Optional[int] = Field(None, alias="total_without_tax_cents", description="The total price of the order without tax in cents, if applicable.")
    total_tax_cents: Optional[int] = Field(None, alias="total_tax_cents", description="The total tax amount for the order in cents, if applicable.")
    total_shipping_tax_included_cents: Optional[int] = Field(None, alias="total_shipping_tax_included_cents", description="The total shipping cost including tax for the order in cents, if applicable.")
    total_shipping_cents: Optional[int] = Field(None, alias="total_shipping_cents", description="The total shipping cost for the order in cents, if applicable.")
    total_shipping_tax_cents: Optional[int] = Field(None, alias="total_shipping_tax_cents", description="The total tax amount for the shipping cost of the order in cents, if applicable.")
    total_weight: Optional[int] = Field(None, alias="total_weight", description="The total weight of the order in grams, if applicable.")
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }
    
class OrderCreate(BaseModel):
    billing_address_id: Optional[int] = Field(None, alias="billing_address_id", description="The unique identifier of the billing address associated with the order, if applicable.")
    chosen_delivery_service: Optional[str] = Field(None, alias="chosen_delivery_service", description="The delivery service chosen for the order, if applicable.")
    earliest_chosen_delivery_at: Optional[str] = Field(None, alias="earliest_chosen_delivery_at", description="The earliest delivery date chosen for the order, if applicable.")
    earliest_delivery_at : Optional[str] = Field(None, alias="earliest_delivery_at", description="The earliest delivery date for the order, if applicable.")
    earliest_shipped_at: Optional[str] = Field(None, alias="earliest_shipped_at", description="The earliest shipped date for the order, if applicable.")
    invoice_ref: Optional[int] = Field(None, alias="invoice_ref", description="The reference of the invoice for the order, if applicable.")
    latest_chosen_delivery_at: Optional[str] = Field(None, alias="latest_chosen_delivery_at", description="The latest delivery date chosen for the order, if applicable.")
    latest_delivery_at: Optional[str] = Field(None, alias="latest_delivery_at", description="The latest delivery date for the order, if applicable.")
    latest_shipped_at: Optional[str] = Field(None, alias="latest_shipped_at", description="The latest shipped date for the order, if applicable.")
    order_documents: Optional[List[OrderDocument]] = Field(None, alias="order_documents", description="The documents associated with the order, if applicable.")
    order_items_attributes: List[OrderItemCreate] = Field(..., alias="order_items_attributes", description="The items associated with the order, if applicable.")
    origin: str = Field(..., alias="origin", description="The origin of the order (e.g., external system name).")
    origin_created_at: str = Field(..., alias="origin_created_at", description="The date and time when the order was created in the external system, if applicable.")
    origin_ref: str = Field(..., alias="origin_ref", description="The reference of the order in the external system, if applicable.")
    payment_medium: Optional[str] = Field(None, alias="payment_medium", description="The payment medium used for the order (e.g., credit card, PayPal, etc.).")
    relay_ref: Optional[str] = Field(None, alias="relay_ref", description="The reference of the relay for the order, if applicable.")
    shipped_at: Optional[str] = Field(None, alias="shipped_at", description="The date and time when the order was shipped, if applicable.")
    shipping_address_id: int = Field(None, alias="shipping_address_id", description="The unique identifier of the shipping address associated with the order, if applicable.")
    source: str = Field(None, alias="source", description="The source of the order (e.g., external system name).")
    source_ref: str = Field(None, alias="source_ref", description="The reference of the order in the source system, if applicable.")
    tags_to_add: Optional[List[str]] = Field(None, alias="tags_to_add", description="The list of tags to add to the order, if applicable.")
    total_price_cents: Optional[int] = Field(None, alias="total_price_cents", description="The total price of the order in cents, including tax, if applicable.")
    total_price_currency: Optional[str] = Field(None, alias="total_price_currency", description="The currency of the total price for the order, if applicable.")
    totla_shipping_tax_cents: Optional[int] = Field(None, alias="total_shipping_tax_cents", description="The total tax amount for the shipping cost of the order in cents, if applicable.")
    total_shipping_tax_currency: Optional[str] = Field(None, alias="total_shipping_tax_currency", description="The currency of the total tax amount for the shipping cost of the order, if applicable).")
    total_shipping_tax_included_cents: Optional[int] = Field(None, alias="total_shipping_tax_included_cents", description="The total shipping cost including tax for the order in cents, if applicable.")
    total_shipping_tax_included_currency: Optional[str] = Field(None, alias="total_shipping_tax_included_currency", description="The currency of the total shipping cost including tax for the order, if applicable.")
    total_tax_cents: Optional[int] = Field(None, alias="total_tax_cents", description="The total tax amount for the order in cents, if applicable.")
    total_tax_currency: Optional[str] = Field(None, alias="total_tax_currency", description="The currency of the total tax amount for the order, if applicable.")
    total_weight: Optional[int] = Field(None, alias="total_weight", description="The total weight of the order in grams, if applicable.")
    order_events_attributes: Optional[List[OrderEvent]] = Field(None, alias="order_events_attributes", description="The attributes of the order events, if applicable.")
    empty_key: Optional[str] = Field(None, alias="", description="An empty key to allow for additional fields in the order creation request, if applicable.") # Exist cause Shippingbo API need an empty key field
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class OrderDetails(Order):
    billing_address_id: Optional[int] = Field(None, alias="billing_address_id", description="The unique identifier of the billing address associated with the order, if applicable.")
    computed_prices: Optional[dict] = Field(None, alias="computed_prices", description="The computed prices for the order, containing details such as price breakdowns, discounts, etc.")
    fullfilled_by_marketplace: Optional[bool] = Field(None, alias="fulfilled_by_marketplace", description="Indicates whether the order is fulfilled by the marketplace, if applicable.")
    invoice_ref: Optional[int] = Field(None, alias="invoice_ref", description="The reference of the invoice for the order, if applicable.")
    order_items_attributes: list = Field(..., alias="order_items_attributes", description="The items associated with the order, if applicable.")
    preparation_order_at: Optional[str] = Field(None, alias="preparation_order_at", description="The date and time when the order is scheduled for preparation, if applicable.")
    tags_to_add: Optional[List[str]] = Field(None, alias="tags_to_add", description="The list of tags to add to the order, if applicable.")
    empty_key: Optional[str] = Field(None, alias="", description="An empty key to allow for additional fields in the order creation response, if applicable.") # Exist cause Shippingbo API need an empty key field
    
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "validate_assignment": True
    }

class OrderAttribute(BaseModel):
    state: str = Field(..., alias="state", description="The state of the order attribute (e.g., pending, processing, shipped, etc.).")
class SuborderItem(BaseModel):
    item_id: int = Field(..., alias="item_id", description="Id of the parent OrderItem.")
    product_id: int = Field(..., alias="product_id", description="Id of the product associated with the suborder item.")
    quantity: int = Field(..., alias="quantity", description="Quantity of the product in the suborder item.")
    sku: str = Field(..., alias="sku", description="The SKU of the product associated with the suborder item.")
    title: str = Field(..., alias="title", description="The title or name of the suborder item.")

class SuborderNumber(BaseModel):
    numberOfTheItem: SuborderItem = Field(..., alias="numberOfTheItem", description="The unique number of the suborder item, used for tracking and reference purposes.")
    order_attributes: Optional[OrderAttribute] = Field(None, alias="order_attributes", description="The attributes of the order associated with the suborder item, if applicable.")