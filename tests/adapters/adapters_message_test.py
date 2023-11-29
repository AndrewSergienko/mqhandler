import json
from dataclasses import asdict

import pytest

from mqhandler.domain.dto import TgMessage


class TestTgMessageAdapter:
    @pytest.mark.asyncio
    async def test_get_message(
        self,
        tg_message,
        tg_message_repo,
        create_test_file,
        test_file_path,
        clear_test_file,
    ):
        message = await tg_message_repo.get_message(test_file_path)

        assert isinstance(message, TgMessage)
        assert message == tg_message

    @pytest.mark.asyncio
    async def test_set_message(
        self, tg_message, tg_message_repo, test_file_path
    ):
        await tg_message_repo.set_message(test_file_path, tg_message)

        with open(test_file_path, "r") as f:
            data = json.loads(f.read())

        tg_message_dct = asdict(tg_message)
        tg_message_dct["time"] = tg_message.time.isoformat()

        assert data == tg_message_dct
