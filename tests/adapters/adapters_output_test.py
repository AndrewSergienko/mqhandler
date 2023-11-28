import pytest


class TestLoggerAdapter:
    @pytest.mark.asyncio
    async def test_info(self, output_adapter):
        await output_adapter.info("Test message")
