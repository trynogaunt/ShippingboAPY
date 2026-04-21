import pytest
from shippingboapy.models.order_document import OrderDocument, OrderDocumentCreate

@pytest.mark.asyncio
async def test_get_order_document(mock_client):
    
    order_document = await mock_client.order_documents.get("doc_123")
    
    assert isinstance(order_document, OrderDocument)
    assert isinstance(order_document.id, str)
    assert isinstance(order_document.type, str)
    assert isinstance(order_document.package_ids, list)
    assert isinstance(order_document.error_message, (str, type(None)))

@pytest.mark.asyncio
async def test_get_order_document_file(mock_client):
    data = await mock_client.order_documents.get_file("doc_123")
    assert isinstance(data, bytes)
    
@pytest.mark.asyncio
async def test_create_order_document(mock_client):
    
    order_document_create = OrderDocumentCreate(
        document_type="invoice",
        language="en",
        order_id=123,
        print_trigger=None,
        duplicate_on_partial_orders=False,
        type="invoice",
        uploaded_file=None
    )
    data = await mock_client.order_documents.create(order_document_create)
    
    if data is not None:
        assert isinstance(data, OrderDocument)
        assert isinstance(data.id, str)
        assert isinstance(data.type, str)
        assert isinstance(data.package_ids, list)
        assert isinstance(data.error_message, (str, type(None)))