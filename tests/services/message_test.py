from dataclasses import asdict
from pathlib import Path

import pytest

from mqhandler.domain.dto import TgMessage
from mqhandler.services import message


class TestMessageServices:
    @pytest.mark.asyncio
    async def test_output_message(self, fake_context, tg_message):
        await message.output_message(fake_context, tg_message)

        assert fake_context.output.result == str(tg_message)

    @pytest.mark.asyncio
    async def test_send_message_to_web(self, fake_context, tg_message):
        await message.send_message_to_web(fake_context, tg_message)
        url = await fake_context.settings.get("EXTERNAL_API_URL")

        assert fake_context.web.result == {
            "url": url,
            "data": asdict(tg_message),
        }

    @pytest.mark.asyncio
    async def test_set_message(self, fake_context, tg_message):
        await message.set_message(fake_context, tg_message)

    @pytest.mark.asyncio
    async def test_get_message(self, fake_context):
        tg_message = await message.get_message(fake_context)

        assert isinstance(tg_message, TgMessage)

    @pytest.mark.asyncio
    async def test_message_file_path(self, fake_context):
        file_path = await message.message_file_path(fake_context)
        expected_value = (
            fake_context.root_path
            / await fake_context.settings.get("FILE_PATH")
        )
        assert file_path == expected_value
