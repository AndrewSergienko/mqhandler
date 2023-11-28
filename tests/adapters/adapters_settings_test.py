import pytest


class TestSettingsAdapter:
    @pytest.mark.asyncio
    async def test_get_env(self, settings_repo):
        assert await settings_repo.get("TEST_ENV") == "TEST_VALUE"

    @pytest.mark.asyncio
    async def test_get_env_with_invalid_name(self, settings_repo):
        assert await settings_repo.get("INVALID_ENV") is None

    @pytest.mark.asyncio
    async def test_get_env_with_invalid_name_and_raise_exc(
        self, settings_repo
    ):
        with pytest.raises(ValueError):
            await settings_repo.get("INVALID_ENV", raise_exc=True)
