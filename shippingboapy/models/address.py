from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from shippingboapy.models.types import ShippingboDateTime

class Address(BaseModel):
    apartement_number: Optional[str] = Field(None, alias="apartement_number", description="The number of the apartment, if applicable.")
    building: Optional[str] = Field(None, alias="building", description="The building name or number, if applicable.")
    city: str = Field(..., alias="city", description="The city of the address.")
    civility: Optional[str] = Field(None, alias="civilitity", description="The civility of the recipient (e.g., Mr, Ms, Company).")
    company_name: Optional[str] = Field(None, alias="company_name", description="The name of the company, if applicable.")
    country: str = Field(..., alias="country", description="The country of the address.")
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the address was created.")
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
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the address was last updated.")
    vat_importer: Optional[str] = Field(None, alias="vat_importer", description="The VAT number of the importer, if applicable.")
    zip: Optional[str] = Field(None, alias="zip", description="The postal code of the address.")

    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }   
    
class AddressCreate(BaseModel):
    apartement_number: Optional[str] = Field(None, alias="apartement_number", description="The number of the apartment, if applicable.")
    building: Optional[str] = Field(None, alias="building", description="The building name or number, if applicable.")
    city: str = Field(..., alias="city", description="The city of the address.")
    civility: Optional[str] = Field(None, alias="civilitity", description="The civility of the recipient (e.g., Mr, Ms, Company).")
    company_name: Optional[str] = Field(None, alias="company_name", description="The name of the company, if applicable.")
    country: str = Field(..., alias="country", description="The country of the address.")
    created_at: Optional[ShippingboDateTime] = Field(None, alias="created_at", description="The date and time when the address was created.")
    email: Optional[str] = Field(None, alias="email", description="The email address associated with the address.")
    eori_importer: Optional[str] = Field(None, alias="eori_importer", description="The EORI number of the importer, if applicable.")
    firstname: Optional[str] = Field(None, alias="firstname", description="The first name of the recipient.")
    fullname: Optional[str] = Field(None, alias="fullname", description="The full name of the recipient.")
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
    updated_at: Optional[ShippingboDateTime] = Field(None, alias="updated_at", description="The date and time when the address was last updated.")
    vat_importer: Optional[str] = Field(None, alias="vat_importer", description="The VAT number of the importer, if applicable.")
    zip: Optional[str] = Field(None, alias="zip", description="The postal code of the address.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }

class AddressUpdate(BaseModel):
    address_kind: Optional[str] = Field("", alias="address_kind", description="The kind of the address (e.g., shipping, billing), if applicable.")
    client_ref: Optional[str] = Field("", alias="client_ref", description="A client reference for the address, if applicable.")
    prefill_origin: Optional[str] = Field("", alias="prefill_origin", description="The origin to prefill the address with, if applicable.")
    apartement_number: Optional[str] = Field("", alias="apartement_number", description="The number of the apartment, if applicable.")
    building: Optional[str] = Field("", alias="building", description="The building name or number, if applicable.")
    city: str = Field(..., alias="city", description="The city of the address.")
    civility: Optional[str] = Field("", alias="civility", description="The civility of the recipient (e.g., Mr, Ms, Company).")
    company_name: Optional[str] = Field("", alias="company_name", description="The name of the company, if applicable.")
    country: str = Field(..., alias="country", description="The country of the address.")
    email: Optional[str] = Field("", alias="email", description="The email address associated with the address.")
    eori_importer: Optional[str] = Field("", alias="eori_importer", description="The EORI number of the importer, if applicable.")
    firstname: Optional[str] = Field("", alias="frstname", description="The first name of the recipient.") # Note: The alias "frstname" is intentional to match the expected field name in the API request for updating an address, which may differ from the field name used in the Address model.
    fullname: Optional[str] = Field("", alias="fullname", description="The full name of the recipient.")
    instructions: Optional[str] = Field("", alias="instructions", description="Special instructions for the delivery, if applicable.")
    lastname: Optional[str] = Field("", alias="lastname", description="The last name of the recipient.")
    phone1: Optional[str] = Field("", alias="phone", description="The phone number associated with the address.")
    phone2: Optional[str] = Field("", alias="phone2", description="An additional phone number associated with the address, if applicable.")
    place_name: Optional[str] = Field("", alias="place_name", description="The name of the place, if applicable.")
    state: Optional[str] = Field("", alias="state", description="The state or province of the address.")
    street1: Optional[str] = Field("", alias="street1", description="The first line of the street address.")
    street2: Optional[str] = Field("", alias="street2", description="The second line of the street address, if applicable.")
    street3: Optional[str] = Field("", alias="street3", description="The third line of the street address, if applicable.")
    street4: Optional[str] = Field("", alias="street4", description="The fourth line of the street address, if applicable.")
    vat_importer: Optional[str] = Field("", alias="vat_importer", description="The VAT number of the importer, if applicable.")
    zip: Optional[str] = Field("", alias="zip", description="The postal code of the address.")
    
    model_config = {
        "extra": "allow",
        "populate_by_name": True,
        "validate_assignment": True
    }