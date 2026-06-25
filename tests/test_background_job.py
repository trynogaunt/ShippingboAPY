import pytest


@pytest.mark.asyncio
async def test_get_background_job_file(mock_client, httpx_mock, minimal_pdf):
    httpx_mock.add_response(
        url="https://stoplight.io/mocks/shippingbo/api/757519129/background_jobs/123/file",
        content=minimal_pdf,
        headers={"Content-Type": "application/pdf"},
    )
    result = await mock_client.background_jobs.get_file(123)
    assert result.startswith(b"%PDF-")