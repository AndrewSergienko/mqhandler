import pytest


class TestSettingsAdapter:
    @pytest.mark.asyncio
    async def test_get_env(self, context):
        assert await context.settings.get("TEST_ENV") == "TEST_VALUE"

    @pytest.mark.asyncio
    async def test_get_env_with_invalid_name(self, context):
        assert await context.settings.get("INVALID_ENV") is None

    @pytest.mark.asyncio
    async def test_get_env_with_invalid_name_and_raise_exc(self, context):
        with pytest.raises(ValueError):
            await context.settings.get("INVALID_ENV", raise_exc=True)
