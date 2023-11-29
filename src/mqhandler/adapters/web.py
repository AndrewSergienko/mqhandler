from typing import Protocol

import aiohttp


class WebProto(Protocol):
    async def post(self, url: str, data: dict) -> int:
        """Send a POST request to the url."""
        pass


class WebAdapter(WebProto):
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def post(self, url: str, data: dict) -> int:
        async with self.session.post(url, data=data) as conn:
            return conn.status
