from datetime import datetime

import pytest

from mqhandler.domain.dto import TgMessage


class TestDtoTgMessage:
    @pytest.mark.asyncio
    async def test_create_message(self):
        assert TgMessage(
            username="test_username", text="test_text", time=datetime.now()
        )

    @pytest.mark.asyncio
    async def test_message_str(self, tg_message):
        assert isinstance(str(tg_message), str)
