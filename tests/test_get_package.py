import pytest
from shippingboapy.models.package import Package

@pytest.mark.asyncio
async def test_get_package(mock_client):
    package_id = 123
    package = await mock_client.packages.get(package_id)
    assert package is not None
    assert isinstance(package, Package)