import pytest


class TestWebAdapter:
    @pytest.mark.asyncio
    async def test_post(self, web_adapter, port, server_app, aiohttp_server):
        url = f"http://127.0.0.1:{port}"
        await aiohttp_server(server_app, port=port)
        response = await web_adapter.post(url, {"test_key": "test_value"})

        assert response == 200
