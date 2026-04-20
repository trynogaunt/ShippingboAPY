import pytest
from shippingboapy.models.pack_component import PackComponent, PackComponentCreate

@pytest.mark.asyncio
async def test_create_pack_component(mock_client):
    pack_component_create = PackComponentCreate(
        component_product_id=123,
        pack_product_id=456,
        quantity=2,
    )
    
    created_pack_component = await mock_client.pack_components.create(pack_component_create, headers={"Prefer": "code=200, dynamic=true"})
    
    assert created_pack_component is not None
    assert isinstance(created_pack_component, PackComponent)
    assert isinstance(created_pack_component.component_product_id, int)
    assert isinstance(created_pack_component.pack_product_id, int)
    assert isinstance(created_pack_component.quantity, int)

@pytest.mark.asyncio
async def test_get_pack_component(mock_client):
    pack_component_id = 123
    pack_component = await mock_client.pack_components.get(pack_component_id, headers={"Prefer": "code=200, dynamic=true"})
    
    assert pack_component is not None
    assert isinstance(pack_component, PackComponent)
    assert isinstance(pack_component.id, int)


@pytest.mark.asyncio
async def test_update_pack_component(mock_client):
    pack_component_id = 123
    pack_component_update = PackComponent(
        id=pack_component_id,
        component_product_id=123,
        pack_product_id=456,
        quantity=2,
    )
    
    updated_pack_component = await mock_client.pack_components.update(pack_component_id, pack_component_update, headers={"Prefer": "code=200, dynamic=true"})
    
    assert updated_pack_component is not None
    assert isinstance(updated_pack_component, PackComponent)
    assert isinstance(updated_pack_component.id, int)
    assert isinstance(updated_pack_component.component_product_id, int)
    assert isinstance(updated_pack_component.pack_product_id, int)
    assert isinstance(updated_pack_component.quantity, int)

@pytest.mark.asyncio
async def test_delete_pack_component(mock_client):
    pack_component_id = 123
    deleted_pack_component = await mock_client.pack_components.delete(pack_component_id, headers={"Prefer": "code=200, dynamic=true"})
    
    assert deleted_pack_component is not None
    assert isinstance(deleted_pack_component, PackComponent)
    assert isinstance(deleted_pack_component.id, int)