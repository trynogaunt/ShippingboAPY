from __future__ import annotations
from typing import TYPE_CHECKING
from pypdf import PdfReader
from pypdf.errors import PdfReadError
import 
if TYPE_CHECKING:
    from shippingboapy.client import Client

def is_valid_pdf(file_path: str) -> bool:
    """
    Check if the provided file is a valid PDF.

    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        bool: True if the file is a valid PDF, False otherwise.
    """
    try:
        PdfReader(file_path)
        return True
    except PdfReadError:
        return False

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
        if is_valid_pdf(data):
            return data
        else:
            raise ValueError(f"The file retrieved for background job ID {background_job_id} is not a valid PDF.")
    