from typing import Annotated
from datetime import datetime
from pydantic import BeforeValidator, PlainSerializer

def parse_shippingbo_datetime(value: str | datetime | None) -> datetime:
    """Parse a Shippingbo datetime string into a datetime object."""
    if value is None or isinstance(value, datetime):
        return value
    if value is None:
        return None
    return datetime.fromisoformat(value)

def serialize_shippingbo_datetime(value: datetime | None) -> str | None:
    """Serialize a datetime object into a Shippingbo datetime string."""
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=datetime.timezone.utc)
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")

ShippingboDateTime = Annotated[datetime, BeforeValidator(parse_shippingbo_datetime), PlainSerializer(serialize_shippingbo_datetime, return_type=str)]