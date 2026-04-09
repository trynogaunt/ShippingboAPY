from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shippingboapy.client import Client

class ProductRessource:
    def __init__(self, client: Client):
        self.client = client
    
    async def list()