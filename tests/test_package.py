import pytest

@pytest.mark.asyncio
async def get_package(mock_client):
    package_id = 1  # Replace with a valid package ID for testing
    package = await mock_client.packages.get(package_id)
    assert package is not None
    assert package.id == package_id