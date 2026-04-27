import pytest
from shippingboapy.models.kit_component import KitComponentCreate, KitComponentUpdate, KitComponent

@pytest.mark.asyncio
async def test_kit_component_create(mock_client):
    kit_component_create = KitComponentCreate(
        kit_product_id=1,
        product_id=2,
        quantity=3
    )

    
    kit_component = await mock_client.kit_components.create(kit_component_create)
    
    assert isinstance(kit_component, KitComponent)
    
@pytest.mark.asyncio
async def test_kit_component_get(mock_client):
    kit_component = await mock_client.kit_components.get(1)
    assert isinstance(kit_component, KitComponent)

@pytest.mark.asyncio
async def test_kit_component_list(mock_client):
    kit_components = await mock_client.kit_components.list(1)
    assert isinstance(kit_components, list)
    assert all(isinstance(item, KitComponent) for item in kit_components)

@pytest.mark.asyncio
async def test_kit_component_update(mock_client):
    kit_component_update = KitComponentUpdate(
        quantity=5
    )
    
    kit_component = await mock_client.kit_components.update(1, kit_component_update)
    assert isinstance(kit_component, KitComponent)

@pytest.mark.asyncio
async def test_kit_component_delete(mock_client):
    result = await mock_client.kit_components.delete(1)
    assert result is True