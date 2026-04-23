import pytest
from shippingboapy.models.address import Address, AddressCreate, AddressUpdate

@pytest.mark.asyncio
async def test_list_addresses(mock_client):
    addresses = await mock_client.address.list()
    
    assert isinstance(addresses, list)
    for address in addresses:
        assert isinstance(address, Address)

@pytest.mark.asyncio
async def test_get_address(mock_client):
    address = await mock_client.address.get(1)

    assert address is not None
    assert isinstance(address, Address)

@pytest.mark.asyncio
async def test_create_address(mock_client):
    address_test = {
        "apartement_number": "12B",
        "building": "Résidence Les Lilas",
        "city": "Strasbourg",
        "civility": "M.",
        "company_name": "Acme Logistics SARL",
        "country": "FR",
        "email": "jean.dupont@example.com",
        "eori_importer": "FR123456789012345",
        "firstname": "Jean",
        "fullname": "Jean Dupont",
        "instructions": "Sonner à l'interphone, code 4829A",
        "lastname": "Dupont",
        "phone1": "+33388123456",
        "phone2": "+33612345678",
        "place_name": "Entrée principale",
        "state": "Grand Est",
        "street1": "15 rue du Faubourg National",
        "street2": "Bâtiment C",
        "street3": None,
        "street4": "3ème étage",
        "vat_importer": "FR12345678901",
        "zip": "67000",
    }
    address_create = AddressCreate(**address_test)
    new_address = await mock_client.address.create(address_create)

    assert new_address is not None
    assert isinstance(new_address, Address)

@pytest.mark.asyncio
async def test_update_address(mock_client):
    address_test = {
        "apartement_number": "12B",
        "building": "Résidence Les Lilas",
        "city": "Strasbourg",
        "civility": "M.",
        "company_name": "Acme Logistics SARL",
        "country": "FR",
        "email": ""
    }
    address_update = AddressUpdate(**address_test)
    updated_address = await mock_client.address.update(1, address_update)
    assert updated_address is not None
    assert isinstance(updated_address, Address)