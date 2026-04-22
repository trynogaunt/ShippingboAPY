from typing import Annotated
from datetime import datetime
from pydantic import BeforeValidator

def parse_shippingbo_datetime(value: str | datetime | None) -> datetime:
    """Parse a Shippingbo datetime string into a datetime object."""
    if value is None or isinstance(value, datetime):
        return value
    if value is None:
        return None
    
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

ShippingboDateTime = Annotated[datetime, BeforeValidator(parse_shippingbo_datetime)]