from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shippingboapy.client import Client


class BackgroundJobResource:
    def __init__(self, client: Client):
        self.client = client

    async def get_file(self, background_job_id: int) -> dict:
        """
        Retrieve a specific background job by its unique identifier.

        Args:
            background_job_id (int): The unique identifier of the background job to retrieve.

        Returns:
            dict: The background job object corresponding to the provided ID.

        Raises:
            HTTPError: If the request to the API fails or returns an error status code.
        """
        data = await self.client._download("GET", f"/background_jobs/{background_job_id}/file")
        
        if data is None:
            return None

        return data
    