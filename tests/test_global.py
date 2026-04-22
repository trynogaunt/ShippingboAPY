import pytest
from shippingboapy.models.types import parse_shippingbo_datetime, serialize_shippingbo_datetime
    
def test_parse_serialize_datetime():

    dt_str = "2019-08-24T14:15:22Z"
    dt = parse_shippingbo_datetime(dt_str)
    assert dt.year == 2019
    assert dt.month == 8
    assert dt.day == 24
    assert dt.hour == 14
    assert dt.minute == 15
    assert dt.second == 22
    assert dt.microsecond == 0
    
    dt_str_serialized = serialize_shippingbo_datetime(dt)
    assert dt_str_serialized == dt_str