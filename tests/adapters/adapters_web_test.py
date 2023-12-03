import os

import pytest


class TestWebAdapter:
    @pytest.mark.asyncio
    @pytest.mark.skip  # failed to run a test in the GitHub Actions pipeline
    async def test_post(self, web_adapter):
        url = os.environ.get("EXTERNAL_API_URL")
        response = await web_adapter.post(url, {"test_key": "test_value"})

        assert response == 200
