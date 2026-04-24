import pytest


@pytest.mark.asyncio
async def test_get_background_job_file(mock_client):
    background_job_id = 123  # Replace with a valid background job ID for testing
    file_content = await mock_client.background_jobs.get_file(background_job_id)
    
    assert file_content is not None
    assert isinstance(file_content, bytes)  # Assuming the file content is returned as bytes