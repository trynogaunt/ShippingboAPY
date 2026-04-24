import pytest
from shippingboapy.models.dangerous_good_product_information import DangerousGoodProductInformation, DangerousGoodProductInformationCreate, DangerousGoodProductInformationUpdate

@pytest.mark.asyncio
async def test_create_dangerous_good_product_information(mock_client):
    dangerous_good_product_information_create = DangerousGoodProductInformationCreate(
        category="Test Category",
        class_code="Test Class Code",
        coefficient=1.0,
        label_code="Test Label Code",
        onu_code="UN1234",
        packaging_group="I",
        packaging_type="Box",
        package_code_identification="Test Package Code",
        tunnel_code="Test Tunnel Code",
        unit="KG",
        product_id="1234",
        dhl_description="Test DHL Description",
        dhl_economy_select_ref="Test DHL Economy Select Ref",
        dhl_ref="Test DHL Ref",
        environmentally_hazardous=True,
        gross_weight=10.0,
        limited_quantity=False,
        onu_description="Test ONU Description",
        quantity=5.0,
        product_description="Test Product Description"
    )
    dangerous_good_product_information = await mock_client.dangerous_good_product_informations.create(dangerous_good_product_information_create)
    assert dangerous_good_product_information is not None
    assert isinstance(dangerous_good_product_information, DangerousGoodProductInformation)
    assert isinstance(dangerous_good_product_information.id, int)
    
@pytest.mark.asyncio
async def test_list_dangerous_good_product_informations(mock_client):
    dangerous_good_product_informations = await mock_client.dangerous_good_product_informations.list()
    
    assert dangerous_good_product_informations is not None
    assert isinstance(dangerous_good_product_informations, list)
    assert all(isinstance(item, DangerousGoodProductInformation) for item in dangerous_good_product_informations)
    
@pytest.mark.asyncio
async def test_get_dangerous_good_product_information(mock_client):
    dangerous_good_product_information = await mock_client.dangerous_good_product_informations.get(1)
    
    assert dangerous_good_product_information is not None
    assert isinstance(dangerous_good_product_information, DangerousGoodProductInformation)
    assert isinstance(dangerous_good_product_information.id, int)
    assert isinstance(dangerous_good_product_information.onu_code, str)
    assert isinstance(dangerous_good_product_information.packaging_group, str)

@pytest.mark.asyncio
async def test_update_dangerous_good_product_information(mock_client):
    dangerous_good_product_information_update = DangerousGoodProductInformationUpdate(
        category="Test Category",
        class_code="Test Class Code",
        coefficient=1.0,
        label_code="Test Label Code",
        onu_code="UN1234",
        packaging_group="I",
        packaging_type="Box",
        package_code_identification="Test Package Code",
        tunnel_code="Test Tunnel Code",
        unit="KG",
        product_id="1234",
        dhl_description="Test DHL Description",
        dhl_economy_select_ref="Test DHL Economy Select Ref",
        dhl_ref="Test DHL Ref",
        environmentally_hazardous=True,
        gross_weight=10.0,
        limited_quantity=False,
        onu_description="Test ONU Description",
        quantity=5.0,
        product_description="Test Product Description"
    )
    dangerous_good_product_information = await mock_client.dangerous_good_product_informations.update(1, dangerous_good_product_information_update)
    
    assert dangerous_good_product_information is not None
    assert isinstance(dangerous_good_product_information, DangerousGoodProductInformation)
    assert isinstance(dangerous_good_product_information.id, int)
    assert isinstance(dangerous_good_product_information.onu_code, str)
    assert isinstance(dangerous_good_product_information.packaging_group, str)

async def test_delete_dangerous_good_product_information(mock_client):
    result = await mock_client.dangerous_good_product_informations.delete(1)
    
    assert result is True